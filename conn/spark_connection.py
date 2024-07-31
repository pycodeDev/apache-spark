from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv
import yaml


# Load environment variables from .env file
def load_env_from_yml(file_path):
    with open(file_path, 'r') as file:
        env_vars = yaml.safe_load(file)
        for key, value in env_vars.items():
            os.environ[key] = value

def get_spark_session():
    load_env_from_yml('xconfig.yaml')

    mysql_url = os.getenv("MYSQL_URL")
    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")

    if not mysql_user or not mysql_password or not mysql_url:
        raise ValueError("Environment variables MYSQL_USER, MYSQL_PASSWORD, or MYSQL_URL are not set")

    spark = SparkSession.builder \
        .appName("MySparkApp") \
        .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.26") \
        .config("spark.driver.extraClassPath", "/opt/spark/jars/mysql-connector-j-9.0.0.jar") \
        .config("spark.executor.extraClassPath", "/opt/spark/jars/mysql-connector-j-9.0.0.jar") \
        .config("spark.sql.jdbc.url", mysql_url) \
        .config("spark.sql.jdbc.user", mysql_user) \
        .config("spark.sql.jdbc.password", mysql_password) \
        .getOrCreate()

    return spark
