# Cloud-Native Student Task Management System

## Overview
A serverless-style backend system that allows users to manage tasks securely and efficiently.

## Tech Stack
- Python (FastAPI)
- AWS Lambda
- API Gateway
- DynamoDB
- IAM

## API Endpoints
POST /task  
GET /tasks  
GET /task/{id}  
PUT /task/{id}  
DELETE /task/{id}  

## Run Locally
pip install -r requirements.txt
uvicorn app:app --reload

Open: http://127.0.0.1:8000/docs