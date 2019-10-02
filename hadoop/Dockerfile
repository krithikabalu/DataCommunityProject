FROM sequenceiq/hadoop-docker:latest
RUN yum -y install wget; yum clean all
RUN wget http://apachemirror.wuchna.com/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.7.jre7.jar

RUN mv sqoop-1.4.7.bin__hadoop-2.6.0 /usr/lib/sqoop
RUN mv /usr/lib/sqoop/conf/sqoop-env-template.sh /usr/lib/sqoop/conf/sqoop-env.sh
RUN mv postgresql-42.2.7.jre7.jar /usr/lib/sqoop/lib

ENV SQOOP_HOME /usr/lib/sqoop
ENV PATH $PATH:$SQOOP_HOME/bin
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop

COPY import_data.sh /import_data.sh