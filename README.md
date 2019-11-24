#### Steps to import data into hdfs from sqoop:

1. Make root of the project as your working directory

2. Run the docker compose file: ` docker-compose up`
           
3. sh into hadoop container: `docker exec -it <container-id> sh`

4. Run `sh /import_data.sh <table_name>`. In our case, table name is 'product'.

5. Insert new records into table

*Using Airflow*

1. Make Python-3.6.3 as working dir 

2. Activate python virtual env `source venv/bin/activate`

3. Initialize airflow db for storing state `airflow initdb`

4. Start web server through which we can track the dags: `airflow webserver -p 8080`

5. Run `sh /create_sqoop_job.sh <table_name> <column_name> <last_id_value>`. In our case, table name is 'product', column name is 'id', last id value is 1003

6. Run the scheduler: `airflow scheduler`

(To test the airflow, run `airflow test pricing import_pricing_data <yyyy-mm-dd>`]

*Hive and ELK*

1. cd into the hive home directory path and initialise the metastore for hive:
    `schematool -initSchema -dbType derby`
    
2. Add the following lines inside hive-site.xml

```
<property>
    <name>system:user.name</name>
    <value>usrname</value>
</property>
<property>
    <name>system:java.io.tmpdir</name>
    <value>/tmp/</value>
</property>
<property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:derby:/usr/local/hive/metastore_db;databaseName=metastore_db;create=true</value>
</property>
<property>
  <name>hive.aux.jars.path</name>
  <value>/usr/local/hive/lib/elasticsearch-hadoop-7.0.0.jar</value>
</property>
```
3. Run 'hive' and in the hive shell, execute the following statements sequentially:

- `CREATE EXTERNAL TABLE product_hdfs (id int, price int,name string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/product';`

- `CREATE EXTERNAL TABLE product_es (id bigint, price bigint, name string) STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler' TBLPROPERTIES('es.resource' ='pricing/product','es.nodes'= 'elasticsearch’);`

- `INSERT INTO TABLE product_es SELECT * FROM product_hdfs;`

4. Check imported data in elastic search: http://localhost:9200/pricing/_search

5. Finally, create visualisation in Kibana: http://localhost:5601/
