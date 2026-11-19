# Retail360 Project Plan

## Milestones
1. Repository and source data setup
2. Bronze ingestion with metadata
3. Silver cleansing, deduplication and quarantine
4. Incremental processing and watermark control
5. SCD Type 1 and SCD Type 2 customer dimensions
6. Gold star schema and business aggregates
7. Data quality, audit logging and restartability
8. Databricks Workflows and CI/CD
9. Azure deployment architecture (ADF + ADLS Gen2 + Azure Databricks + Key Vault)
10. Power BI reporting and interview documentation

## Acceptance criteria
- Re-running a pipeline does not create duplicate business records.
- Invalid records are captured separately with rejection reasons.
- Incremental runs process only new/changed data.
- SCD Type 2 preserves historical customer versions.
- Gold facts reconcile to source orders and order items.
