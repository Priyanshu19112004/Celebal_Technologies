# Week 4 Assignment Report
# Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory

---

## Objective

The objective of this assignment was to gain practical experience with Microsoft Azure cloud services and develop an end-to-end data pipeline using Azure Blob Storage and Azure Data Factory (ADF). The assignment focused on cloud resource provisioning, secure storage management, metadata validation, data movement, and access control using Azure Identity and Access Management (IAM).

---

## Introduction

Microsoft Azure is a leading cloud computing platform that provides a wide range of services for data storage, processing, and analytics. Azure Data Factory (ADF) is a cloud-based data integration service that enables the creation of scalable and automated data pipelines for data ingestion and movement.

In this assignment, Azure Blob Storage was used as both the source and destination storage system, while Azure Data Factory was used to orchestrate the data pipeline. The project demonstrates the fundamental concepts of cloud-based data engineering and workflow automation.

---

## Technologies and Services Used

| Technology / Service | Purpose |
|---------------------|----------|
| Microsoft Azure | Cloud Computing Platform |
| Azure Resource Group | Resource Organization and Management |
| Azure Storage Account | Cloud Storage Management |
| Azure Blob Storage | Source and Destination Data Storage |
| Azure Data Factory (ADF) | Data Integration and Pipeline Orchestration |
| CSV File (Sample Superstore Dataset) | Input Dataset |
| Azure IAM | Access Control and Security |

---

## Task 1: Resource Group Creation

### Description
A Resource Group named **rg-rishikesh** was created in the Azure Portal to organize and manage all resources required for the project.

### Activities Performed
- Logged into Azure Portal
- Created a new Resource Group
- Selected the appropriate region
- Verified successful deployment

### Result
The Resource Group was successfully created and served as the central container for all Azure resources.

---

## Task 2: Azure Storage Configuration

### Description
Azure Blob Storage was configured to store source and destination files for the data pipeline.

### Activities Performed
- Created an Azure Storage Account
- Created two Blob Storage containers:
  - **input**
  - **output**
- Uploaded the **Sample - Superstore.csv** dataset to the input container

### Result
The storage environment was successfully configured, and the source dataset was made available for processing.

---

## Task 3: Azure Data Factory Setup

### Description
An Azure Data Factory instance named **adf-rishikesh** was created and configured.

### Activities Performed
- Created Azure Data Factory
- Explored the Author, Monitor, and Manage sections
- Created a Linked Service:
  - **LS_BlobStorage**
- Created Source Dataset
- Created Destination Dataset
- Configured the **Get Metadata** activity to validate source file information

### Result
Azure Data Factory was successfully connected to Azure Blob Storage, and all required datasets and services were configured.

---

## Task 4: Data Pipeline Development

### Description
A data pipeline was designed to copy data from the source container to the destination container after validating file metadata.

### Activities Performed
- Added the **Get Metadata** activity
- Added the **Copy Data** activity
- Configured source and destination datasets
- Connected activities to establish the execution flow

### Pipeline Workflow

```text
Source CSV File
        │
        ▼
Get Metadata Activity
        │
        ▼
Copy Data Activity
        │
        ▼
Destination (output.csv)
```

### Result
The pipeline was successfully developed and configured for automated data movement.

---

## Task 5: Pipeline Execution and Monitoring

### Description
The pipeline was executed and monitored using Azure Data Factory.

### Activities Performed
- Executed the pipeline using the Debug option
- Monitored activity execution status
- Verified successful completion of the pipeline
- Confirmed creation of the output file in the destination container

### Result
The pipeline executed successfully and transferred the data from the input container to the output container without errors.

---

## Task 6: Identity and Access Management (IAM)

### Description
Role-Based Access Control (RBAC) was implemented to provide secure access between Azure services.

### Roles Assigned

| Role | Purpose |
|--------|----------|
| Reader | Provides read-only access to Azure resources |
| Storage Blob Data Contributor | Allows Azure Data Factory to access Blob Storage data |

### Result
Required permissions were successfully assigned, enabling secure communication between Azure Data Factory and Azure Blob Storage.

---

## Results and Observations

| Component | Status |
|------------|----------|
| Resource Group Creation | Successful |
| Storage Account Configuration | Successful |
| Blob Containers Creation | Successful |
| Dataset Upload | Successful |
| Linked Service Configuration | Successful |
| Dataset Creation | Successful |
| Metadata Validation | Successful |
| Pipeline Development | Successful |
| Pipeline Execution | Successful |
| Output File Generation | Successful |
| IAM Role Assignment | Successful |

---

## Learning Outcomes

This assignment provided hands-on experience with:

- Azure Resource Group Management
- Azure Storage Account and Blob Storage Configuration
- Azure Data Factory Fundamentals
- Linked Services and Dataset Creation
- Metadata Validation using Get Metadata Activity
- Data Movement using Copy Data Activity
- Pipeline Monitoring and Debugging
- Azure Role-Based Access Control (RBAC)
- End-to-End Cloud Data Pipeline Development

---

## Conclusion

This assignment successfully demonstrated the implementation of an end-to-end cloud-based data pipeline using Microsoft Azure services. Azure Blob Storage was configured as the source and destination storage layer, while Azure Data Factory was used to orchestrate and automate the data movement process. Metadata validation was performed prior to data transfer, and appropriate IAM roles were assigned to ensure secure access between services.

The successful execution of the pipeline validated the complete workflow of data ingestion, validation, and transfer within the Azure ecosystem, providing practical exposure to cloud-based data engineering concepts and Azure platform services.

## Final Outcome

✅ Azure resources deployed successfully  
✅ Blob Storage configured successfully  
✅ Linked Services and Datasets created successfully  
✅ Metadata validation completed successfully  
✅ Data pipeline executed successfully  
✅ Data copied from source to destination successfully  
✅ Output file generated successfully  
✅ IAM permissions configured successfully
