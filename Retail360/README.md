# Retail360 — Enterprise Retail Data Engineering Platform

## Business objective
Build a retail analytics lakehouse that ingests customer, product, order, order-item and payment data; validates and transforms it through Bronze, Silver and Gold layers; and serves analytics-ready dimensional models.

## Technology
- Databricks Free Edition for initial development
- PySpark and Delta Lake
- GitHub for source control
- Azure Data Factory, ADLS Gen2, Azure Databricks and Key Vault in the Azure deployment phase
- Power BI for reporting

## Repository layout
```text
Retail360/
├── data/source/       # Small synthetic CSV datasets for development
├── notebooks/         # Databricks notebook source files
├── sql/               # DDL and analytical SQL
├── tests/             # Data quality checks
├── config/            # Table and pipeline configuration
├── docs/              # Architecture and runbook documentation
└── README.md
```

## Source datasets
- customers.csv
- customer_updates.csv
- products.csv
- orders.csv
- order_items.csv
- payments.csv

All records are synthetic and intended for learning.

## Initial execution plan
1. Upload `data/source` to a Databricks Volume or use the workspace file upload flow.
2. Set the source path in `notebooks/01_bronze_ingestion.py`.
3. Run Bronze ingestion.
4. Continue with Silver cleansing, incremental processing, SCD Type 2, Gold dimensional modelling and quality checks.

## Data model
- `silver_customers`, `silver_products`, `silver_orders`, `silver_order_items`, `silver_payments`
- `dim_customer`, `dim_product`, `dim_date`
- `fact_sales`

## Important
This starter uses small synthetic CSV files. It is a development seed, not a production dataset. Never commit secrets, access tokens, connection strings or real customer data.
