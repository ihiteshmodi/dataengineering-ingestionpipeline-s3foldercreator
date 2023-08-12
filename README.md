# dataengineering-ingestionpipeline-s3foldercreator

# AWS S3 Folder Creator

Welcome to Part 1 of our Data Ingestion Pipeline Project.

Overview:
Every business day, a folder is automatically generated with the current date (excluding on weekends). This folder serves as a drop location for clients to upload their files.

Project Structure:
The project is divided into two core components:

1. AWS CloudWatch:
   CloudWatch is set to trigger our AWS Lambda function daily at a specific time.

2. AWS Lambda:
   The Lambda function extracts today's date and dynamically generates a folder hierarchy:
   - Year: e.g., 2023
   - Month: e.g., July (represented as "07")
   - Day: e.g., 10

CloudWatch has been configured to execute the trigger exclusively on weekdays as neither the org nor the client is working on weekends.

Part 2 of the Project:
In the upcoming phase, we will extend the pipeline. This phase involves:

- Data Retrieval: The system will collect files from the designated drop location.
- Deduplication: The pipeline will  eliminate duplicates using a hash key if they exist between the currently ingested files and in snwoflake db.
- Data Processing: Processed data will be uploaded to the staging table for further validation.
- Database Integration: Validated data will be moved to the main table within Snowflake.

Our goal is to ensure an efficient and streamlined data processing flow, enabling updates while maintaining data integrity.

Stay tuned for further updates and enhancements!
