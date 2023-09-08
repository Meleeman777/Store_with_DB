
"""
@api {get} /products Get list of products

@apiName GetProductList
@apiGroup Product
@apiPermission none
@apiHeader {String} Authorization       The token can be generated from your user profile
@apiParam {Number}    page              Which 'page' of paginated results to return.
@apiParam {Number}    per_page          Number of items returned per page

@apiExample {bash} Curl example
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" "https://api.myapp.com/v2/products"

@apiSuccess {Object[]} products               List of products
@apiSuccess {Number}   products.id            id of product
@apiSuccess {String}   products.name          name of the product
@apiSuccess {Number}   products.price         price of the product
@apiSuccess {String}   products.description   product`s description
@apiSuccess {String}   products.category      product`s category

@apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
         - "products": [
        {
                "id": 111,
		"name": "keyboard",
		"price": 200,
		"description": "gaming keyboard",
		"catergory": "keyboards"
		}
        {
		...
		}
        ]  

@apiError UserNotFound   The <code>id</code> of the User was not found.
@apiError (500 Internal Server Error) InternalServerError The server encountered an internal error

@apiErrorExample Response (example):
     HTTP/1.1 401 Not Authenticated
     {
       "error": "NoAccessRight"
     }
"""
 
 
"""
@api {put} /products/:id Change Product Information
@apiName PutProductInfo
@apiGroup Product
@apiPermission admin
@apiHeader {String} Authorization       The token can be generated from your user profile
@apiParam {Number}  id            The ID of the app.

@apiBody {String}   name          name of the product
@apiBody {Number}   price         price of the product
@apiBody {String}   description   product`s description
@apiBody {String}   category      product`s category
@apiExample {bash} Curl example
 curl -X PUT \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $TOKEN" \
-d '{"name":"keyboard", "price":"300", "description":"best gaming keyboard", "category": "Keyboards"}` \
"https://api.myapp.com/v2/products/123"
@apiSuccess {Object[]} product       product
@apiSuccess {Number}   id            id of product
@apiSuccess {String}   name          name of the product
@apiSuccess {Number}   price         price of the product
@apiSuccess {String}   description   product`s description
@apiSuccess {String}   category      product`s category 
@apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
    {
         - "product": {
            "id": 123,
            "name": "keyboard",
            "price": 300,
            "description": "best gaming keyboard",
            "category": "Keyboards"
            }     
    }

@apiError NoAccessRight Only authenticated Admins can access the data.
@apiError ProductNotFound   The <code>id</code> of the Product was not found.
@apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
@apiErrorExample Response (example):
     HTTP/1.1 404 The resource was not found
     {
       "error": "The resource you requested could not be found."
     }
"""

"""
@api {post} /add-to-cart     Add Product to cart
@apiName AddtoCart
@apiGroup Product
@apiPermission none
@apiHeader {String} Authorization       The token can be generated from your user profile
@apiBody   {Object[]} items                   cart items
@apiBody   {Number} items.id                  id of product
@apiBody   {String} items.name                name of the product
@apiBody   {number} items.amount              name of the product
@apiBody   {Number} items.price               price of the product

@apiExample {bash} Curl example
 curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $TOKEN" \
-d '{"id":"123", "name": "keyboard", "amount": "1", "price": "300"}' \
"https://api.myapp.com/v2/add-to-cart"

@apiSuccess   {Object[]} orderInfo                  Order information
@apiSuccess   {String}   orderInfo.name             name of the product
@apiSuccess   {Number}   orderInfo.amount           name of the product
@apiSuccess   {Number}   orderInfo.price            price of the product
@apiSuccess   {Number}   orderInfo.sum              Order amount


@apiSuccessExample {json} Success-Res  ponse:
     HTTP/1.1 200 OK
       "orderInfo": {
            "name": "keyboard",
            "amount": 1,
            "price": 300,
            "sum": 300
     }
@apiError NoAccessRight Only authenticated Admins can access the data.
@apiError UserNotFound   The <code>id</code> of the User was not found.
@apiError (500 Internal Server Error) InternalServerError The server encountered an internal error

@apiErrorExample Response (example):
     HTTP/1.1 401 Not Authenticated
     {
       "error": "NoAccessRight"
     }
"""
