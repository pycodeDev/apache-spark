# Gunakan image dasar OpenJDK
FROM openjdk:8-jre-slim

# Menginstal dependencies yang diperlukan
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set ARG dan ENV untuk versi Spark dan Hadoop
ARG SPARK_VERSION=3.1.2
ARG HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Unduh dan ekstrak Apache Spark
RUN curl -sL "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | tar -xz -C /opt/ && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME

# Menambahkan JAR konektor MySQL (opsional jika diperlukan)
ADD mysql-connector/mysql-connector-j-9.0.0.jar $SPARK_HOME/jars/

# Entrypoint
ENTRYPOINT ["/opt/spark/bin/spark-class"]
