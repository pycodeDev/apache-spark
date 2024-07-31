from pyspark.sql import SparkSession

# Membuat sesi Spark
spark = SparkSession.builder \
    .appName("MySQL Spark Connector") \
    .config("spark.jars", "/opt/spark/jars/mysql-connector-j-9.0.0.jar") \
    .getOrCreate()

# URL JDBC untuk MySQL, ganti 'host.docker.internal' dengan IP yang tepat jika perlu
jdbc_url = "jdbc:mysql://host.docker.internal:3306/c45_project"

# Properti koneksi
connection_properties = {
    "user": "root",
    "password": "12345678",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Membaca tabel MySQL ke dalam DataFrame Spark
df = spark.read.jdbc(url=jdbc_url, table="tb_data", properties=connection_properties)

# Menampilkan data
df.show()
