# Quick Guide

## Installation

### Step 1: Clone this repository - https://gitlab.rebrainme.com/devops_users_repos/5229/dev/-/tree/dev06

### Step 2: Change file liquidbase.properties
 
```bash
# Here we use Postgresql, but you can change url on any of supported by liquibase databases.
url=jdbc:postgresql://localhost:5432/{your_database_name}
username={your_database_user}
password={your_database_user_password}
changeLogFile=db/changelog/db.changelog-master.xml
liquibase.hub.mode=off

```

### Step 3: Check /db/changelog directory

```bash
/v.1.0.0 
/v.1.1.0
db.changelog-master.xml
```

### Step 4: Check /db/changelog directory/{version}

changelog.xml ### included scripts
create-changeset-products-table.xml ### script for creating database
insert-changeset-products-table.xml ### script for inserting into database

### Step 5: Include necessary versions in your db.changelog-master.xml

```bash
<include file="v.1.0.0/changelog.xml" relativeToChangelogFile="true"/>
<include file="v.1.1.0/changelog.xml" relativeToChangelogFile="true"/>
```

### Step 6: Start the script

```bash
./liquibase update
```

Liquibase: Update has been successful.

```bash
api=> select * from databasechangelog;

 id | author |                         filename                         | 
----+--------+----------------------------------------------------------+
 1  | api    | db/changelog/v.1.0.0/create-changeset-products-table.xml | 
 2  | api    | db/changelog/v.1.0.0/insert-changeset-products-table.xml | 
 3  | api    | db/changelog/v.1.1.0/create-changeset-orders-table.xml   | 
 4  | api    | db/changelog/v.1.1.0/insert-changeset-orders-table.xml   | 
```


### PS: Rollback

Each script has rollback section


Example "insert-changeset-orders-table.xml":
   <rollback>
       <delete tableName="orders">
          <where>name = 'keyboard'</where>
       </delete>
   </rollback>

```bash
# will delete last changes (insert-changeset-orders-table.xml)
./liquibase rollbackCount 1 
#  will delete last 2 changes (insert-changeset-orders-table.xml and create-changeset-orders-table.xml)
./liquibase rollbackCount 2 
```
