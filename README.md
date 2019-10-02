###### Steps to import data into hdfs from sqoop:

1. Make root of the project as your working directory

2. Run the docker compose file: ` docker-compose up`
           
3. sh into hadoop container: `docker exec -it <container-id> sh`

4. Run `sh /import_data.sh <table_name>`. In our case, table name is 'product'.
