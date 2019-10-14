###### Steps to import data into hdfs from sqoop:

1. Make root of the project as your working directory

2. Run the docker compose file: ` docker-compose up`
           
3. sh into hadoop container: `docker exec -it <container-id> sh`

4. Run `sh /import_data.sh <table_name>`. In our case, table name is 'product'.

5. Insert new records into table

6. Run `sh /import_data.sh <table_name> <column_name> <last_id_value>`. In our case, table name is 'product', column name is 'id', last id value is 1003
