FROM ouyi/hadoop-docker:latest
RUN yum -y install wget; yum clean all && yum -y install unzip; yum clean all
RUN yum -y install zlib; yum clean all && yum -y install zlib-devel; yum clean all
RUN yum -y update && yum groupinstall -y "development tools";yum clean all && yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel;yum clean all

RUN wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz && tar xf Python-3.6.3.tar.xz
RUN wget http://apachemirror.wuchna.com/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.7.jre7.jar
RUN wget http://www.java2s.com/Code/JarDownload/java-json/java-json.jar.zip
RUN wget http://apachemirror.wuchna.com/hive/hive-2.3.6/apache-hive-2.3.6-bin.tar.gz && tar -xvf apache-hive-2.3.6-bin.tar.gz
RUN wget http://archive.apache.org/dist/db/derby/db-derby-10.12.1.1/db-derby-10.12.1.1-bin.tar.gz && tar -xvf db-derby-10.12.1.1-bin.tar.gz
RUN wget https://repo1.maven.org/maven2/org/elasticsearch/elasticsearch-hadoop/7.0.0/elasticsearch-hadoop-7.0.0.jar

RUN unzip java-json.jar.zip

RUN mv sqoop-1.4.7.bin__hadoop-2.6.0 /usr/lib/sqoop
RUN mv /usr/lib/sqoop/conf/sqoop-env-template.sh /usr/lib/sqoop/conf/sqoop-env.sh
RUN mv postgresql-42.2.7.jre7.jar /usr/lib/sqoop/lib
RUN mv java-json.jar /usr/lib/sqoop/lib/java-json.jar
RUN mv apache-hive-2.3.6-bin /usr/local/hive
RUN mv db-derby-10.12.1.1-bin /usr/local/derby
RUN mv elasticsearch-hadoop-7.0.0.jar /usr/local/hive/lib
RUN cp /usr/local/hive/conf/hive-env.sh.template /usr/local/hive/conf/hive-env.sh
RUN cp /usr/local/hive/conf/hive-default.xml.template /usr/local/hive/conf/hive-site.xml

ENV SQOOP_HOME /usr/lib/sqoop
ENV AIRFLOW_HOME /root/airflow/
ENV HIVE_HOME /usr/local/hive
ENV DERBY_HOME /usr/local/derby
ENV PATH $PATH:$SQOOP_HOME/bin:$HIVE_HOME/bin:$DERBY_HOME/bin
ENV CLASSPATH $CLASSPATH:/usr/local/Hadoop/lib/*:.
ENV CLASSPATH $CLASSPATH:/usr/local/hive/lib/*:.

COPY import_data.sh /import_data.sh
COPY create_sqoop_job.sh /create_sqoop_job.sh

WORKDIR Python-3.6.3
RUN ./configure --prefix=/usr/local --enable-shared --enable-loadable-sqlite-extensions LDFLAGS="-Wl,-rpath /usr/local/lib"
RUN make && make altinstall && wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && python3.6 -m venv venv && source venv/bin/activate && pip install 'apache-airflow'
COPY workflow.py $AIRFLOW_HOME/dags/workflow.py
WORKDIR /
