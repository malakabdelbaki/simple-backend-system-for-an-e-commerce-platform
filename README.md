# Simple Backend System for an E-Commerce Platform

This project implements a scalable, event-driven backend architecture for processing e-commerce orders using AWS services.

## Architecture Overview

The system is designed using:
- Amazon SNS for publishing order events
- Amazon SQS for queueing order processing tasks
- AWS Lambda for serverless processing
- Amazon DynamoDB for order data persistence
- Amazon CloudWatch for observability and metrics

### 📌 Architecture Diagram

![Architecture Diagram](https://github.com/malakabdelbaki/simple-backend-system-for-an-e-commerce-platform/blob/main/Cloud%20Assignment%202%20Arch%20diagram.png)

---

## Setup Instructions
You can deploy this project using **either of the two methods** below:

Option 1: Deploy Using CloudFormation using the template.yaml

Option 2: manual set up

### Manual set up Steps

#### 1️. Create DynamoDB Table

- **Table name**: `Orders`
- **Partition key**: `orderId` (String)
- **Additional attributes**:
- `userId` (String)
- `itemName` (String)
- `quantity` (Number)
- `status` (String)
- `timestamp` (String)

#### 2. Create SNS Topic

- **Topic name**: `OrderTopic`

#### 3. Create SQS Queues

- **DLQ name**: `OrderDLQ`
- **Standard Queue name**: `OrderQueue`
- Configure **Dead-Letter Queue**:
 - Assign `OrderDLQ` as the DLQ
 - Set `maxReceiveCount` to `3`
- **Subscribe** `OrderQueue` to `OrderTopic` (SNS → SQS subscription)

#### 4️. Create Lambda Function

- **Function name**: `ProcessOrderFunction`
- **Runtime**: Python 3.13
- **Handler**: e.g., `lambda_function.lambda_handler`
- **IAM Role**:
- Permissions for:
 - Reading from SQS
 - Writing to DynamoDB
 - Writing logs to CloudWatch
- **Trigger**: `OrderQueue` (SQS event source)
- Function code can be found in file lambda_function.py


