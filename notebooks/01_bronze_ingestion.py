# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %md
# MAGIC # 01 — Bronze ingestion
# MAGIC Reads the six source CSV files and writes raw Delta tables with ingestion metadata.
# MAGIC Update `source_path` to the location where you upload the project CSV files.

# COMMAND ----------

from pyspark.sql import functions as F

# Replace with your Unity Catalog Volume path after creating a catalog/schema/volume.
source_path = "/Volumes/retail360/bronze/retail_source/"
catalog_name = "retail360"
schema_name = "bronze"

# COMMAND ----------

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name}")

# COMMAND ----------

source_tables = [
    "customers",
    "customer_updates",
    "products",
    "orders",
    "order_items",
    "payments"
]

# COMMAND ----------

from pyspark.sql import functions as F

for table_name in source_tables:
    file_path = f"{source_path}/{table_name}.csv"

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
        .withColumn("_ingestion_timestamp", F.current_timestamp())
        .withColumn("_source_file", F.lit(file_path))
    )

    target_table = f"{catalog_name}.{schema_name}.{table_name}"
    (df.write
       .format("delta")
       .mode("append")
       .option("mergeSchema", "true")
       .saveAsTable(target_table))

    print(f"Loaded {table_name}: {df.count()} rows into {target_table}")