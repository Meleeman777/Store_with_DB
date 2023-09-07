package main

import (
    "encoding/json"
    "database/sql"
    "net/http"
    "fmt"
    "log"
    _ "github.com/lib/pq"
)

var db *sql.DB

type Product struct {
	Id int
	Name string
	Price int
	Description string
	Category string
}
type Products struct {
	Products []Product
}


type Order struct {
        Id int
        Name string
        Amount int
	Price int
}


func main() {
	var err error

	db, err = sql.Open("postgres", "host=127.0.0.1 user=api password=123456 dbname=api sslmode=disable")
        if err != nil {
            panic(err)
        }

	defer db.Close()

	fmt.Println("Starting...")
	http.HandleFunc("/v2/orders/add", addOrder)
	http.HandleFunc("/v2/products/", getProducts)
	log.Fatal(http.ListenAndServe(":7070", nil))

}

func addOrder(w http.ResponseWriter, r *http.Request) {
        if r.Method != "POST" {
                http.Error(w, "Method Not Allowed", 405)
        } else {
                decoder := json.NewDecoder(r.Body)
                var g_order Order

                err := decoder.Decode(&g_order)
                if err != nil {
                        panic(err)
                }

                query := fmt.Sprintf("INSERT INTO orders(name, amount, price) VALUES('%s', %d, %d) RETURNING id",g_order.Name, g_order.Amount, g_order.Price)

                fmt.Println("# INSERT QUERY: %s", query)
                rows, err := db.Query(query)
                if err != nil {
                        panic(err)
                }


                for rows.Next() {
                        var id int
                        err = rows.Scan(&id)
                        if err != nil {
                                panic(err)
                        }
                        fmt.Fprintf(w, "{\"id\":%d}", id)

                }

        }

}


func getProducts(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		http.Error(w, "Method Not Allowed", 405)
	} else {
		p_array := Products{}


		fmt.Println("# Quering")
		rows, err := db.Query("SELECT id,name,price,description,category from products")
		if err != nil {
			panic(err)
		}

	for rows.Next() {
		p_product := Product{}

		err = rows.Scan(&p_product.Id,&p_product.Name,&p_product.Price,&p_product.Description,&p_product.Category)
		if err != nil {
			panic(err)
		}
		p_array.Products = append(p_array.Products, p_product)
	}

	json.NewEncoder(w).Encode(p_array)
	}
}

