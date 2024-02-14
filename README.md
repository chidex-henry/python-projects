## Lambda and Python Project

This project focuses on utilizing a Python Lambda script to organize files in an Amazon S3 bucket based on the date they were uploaded. Below are the steps involved in setting up and executing the project:

### 1. Installation of Boto3

Boto3, the AWS SDK for Python, was installed. Boto3 allows for the creation, configuration, and management of AWS services such as Amazon EC2 and S3.

### 2. Creation of IAM User

An IAM user named "python-user" was created with programmatic access. The IAM user was configured to enable Python to authenticate and create AWS resources.

### 3. Creation of S3 Buckets

- An S3 bucket named "chidex-organize-s3-objects" was created to store all client files.
- Another S3 bucket named "chidex-lambda-organize-s3-objects" was created to store the zipped Python script for Lambda function execution.

<img width="307" alt="image" src="https://github.com/chidex-henry/python-projects/assets/77998377/1cdf5c0e-d10b-40e6-b182-8678d520c498">

### 4. GitHub Repository Setup

A GitHub repository was created to store Python files, and it was cloned to the local desktop. Changes were pushed from the local repository to the remote repository for version control.

### 5. Python Script Development

A Python script was developed to execute the tasks required for file organization within the S3 bucket. The script handles the logic of moving files to folders named YYYYMMDD/filename based on their upload dates.

### 6. Zipping and Storage of Python Script

The Python script was zipped and stored in the S3 bucket "chidex-lambda-organize-s3-objects" to enable the Lambda function to access and execute it.

<img width="451" alt="image" src="https://github.com/chidex-henry/python-projects/assets/77998377/ea0ba381-9ca0-46f3-9c46-3fd90539f58a">

### 7. IAM Role Creation

An IAM role named "organize-s3-objects" was created with permissions such as AmazonS3FullAccess and AWSLambdaBasicExecutionRole. This role allows the Lambda function to trigger the Python file stored in the S3 bucket.

<img width="345" alt="image" src="https://github.com/chidex-henry/python-projects/assets/77998377/7c2c380b-9841-48a4-a917-f48eac119381">

<img width="415" alt="image" src="https://github.com/chidex-henry/python-projects/assets/77998377/b4ba26c1-4156-4ebe-ac05-05aa94930bda">

### 8. Creation of Lambda Function

A Lambda function named "organize-s3-objects" was created. An S3 trigger was added to the Lambda function to execute the Python script when files are uploaded to the S3 bucket.

<img width="415" alt="image" src="https://github.com/chidex-henry/python-projects/assets/77998377/4c335ad6-c9db-4431-a556-47dab2817986">

### 9. Configuration and Testing

- The Python file was uploaded into the Lambda function, and the handler settings were updated accordingly.
- A test event for the Lambda function was created to simulate file uploads.
- The Lambda function was tested by uploading files into the S3 bucket, ensuring that all files were successfully organized into folders based on their upload dates.

By following these steps, the project successfully implemented a Python Lambda script to automate the organization of files within an Amazon S3 bucket based on their upload dates.

<img width="443" alt="image" src="https://github.com/chidex-henry/python-projects/assets/77998377/ec1079b2-2ec5-4733-ba1f-9babbc0f199c">

