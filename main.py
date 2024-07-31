import sys
import os

# Get the parent directory
parent_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
from conn.spark_connection import get_spark_session

def main():
    spark = get_spark_session()
    
    # Lakukan operasi Spark Anda di sini
    df = spark.read.format("jdbc").options(
        url=spark.conf.get("spark.sql.jdbc.url"),
        driver="com.mysql.cj.jdbc.Driver",
        dbtable="tb_data",
        user=spark.conf.get("spark.sql.jdbc.user"),
        password=spark.conf.get("spark.sql.jdbc.password")
    ).load()

    df.show()

if __name__ == "__main__":
    main()
