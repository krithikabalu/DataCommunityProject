FROM sequenceiq/hadoop-docker:latest
RUN yum -y install wget; yum clean all && yum -y install unzip; yum clean all
RUN yum -y install zlib; yum clean all && yum -y install zlib-devel; yum clean all
RUN yum -y update && yum groupinstall -y "development tools";yum clean all && yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel;yum clean all

RUN wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz && tar xf Python-3.6.3.tar.xz
RUN wget http://apachemirror.wuchna.com/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.7.jre7.jar
RUN wget http://www.java2s.com/Code/JarDownload/java-json/java-json.jar.zip

RUN unzip java-json.jar.zip

RUN mv sqoop-1.4.7.bin__hadoop-2.6.0 /usr/lib/sqoop
RUN mv /usr/lib/sqoop/conf/sqoop-env-template.sh /usr/lib/sqoop/conf/sqoop-env.sh
RUN mv postgresql-42.2.7.jre7.jar /usr/lib/sqoop/lib
RUN mv java-json.jar /usr/lib/sqoop/lib/java-json.jar

ENV SQOOP_HOME /usr/lib/sqoop
ENV PATH $PATH:$SQOOP_HOME/bin
ENV AIRFLOW_HOME /root/airflow/

COPY import_data.sh /import_data.sh
COPY create_sqoop_job.sh /create_sqoop_job.sh

WORKDIR Python-3.6.3
RUN ./configure --prefix=/usr/local --enable-shared --enable-loadable-sqlite-extensions LDFLAGS="-Wl,-rpath /usr/local/lib"
RUN make && make altinstall && wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && python3.6 -m venv venv && source venv/bin/activate && pip install 'apache-airflow'
COPY workflow.py $AIRFLOW_HOME/dags/workflow.py
