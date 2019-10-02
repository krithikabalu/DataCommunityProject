FROM sequenceiq/hadoop-docker:latest
RUN yum -y install wget; yum clean all
RUN wget http://apachemirror.wuchna.com/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
RUN mv sqoop-1.4.7.bin__hadoop-2.6.0 /usr/lib/sqoop
ENV SQOOP_HOME /usr/lib/sqoop
ENV PATH $PATH:$SQOOP_HOME/bin
ENV SQOOP_HOME /usr/lib/sqoop
RUN mv $SQOOP_HOME/conf/sqoop-env-template.sh $SQOOP_HOME/conf/sqoop-env.sh
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.7.jre7.jar
RUN mv postgresql-42.2.7.jre7.jar /usr/lib/sqoop/lib