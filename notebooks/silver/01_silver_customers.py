# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Cell 1
# MAGIC %run ../../Project_SetUp

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Example: clean customers and keep the latest record per customer_id.
customers = spark.table(f"{catalog_name}.{bronze_schema}.customers")

w = Window.partitionBy("customer_id").orderBy(F.col("_ingestion_timestamp").desc())

silver_customers = (
    customers
    .withColumn("customer_name", F.trim("customer_name"))
    .withColumn("email", F.lower(F.trim("email")))
    .withColumn("city", F.initcap(F.trim("city")))
    .filter(F.col("customer_id").isNotNull())
    .withColumn("_rn", F.row_number().over(w))
    .filter(F.col("_rn") == 1)
    .drop("_rn")
)

(silver_customers.write.format("delta")
 .mode("overwrite")
 .option("overwriteSchema", "true")
 .saveAsTable(f"{catalog_name}.{silver_schema}.customers"))

display(silver_customers)