# Loan Approval Prediction API

This project provides a REST API for predicting loan approvals using a machine learning model. The API is built using Flask and the model is saved using a scikit-learn pipeline.

## Prerequisites

- Docker
- Docker Compose (optional)

## Project Structure

.
├── app
│ ├── init.py
│ ├── views.py
│ ├── loan_approval_model.pkl
├── requirements.txt
├── Dockerfile
├── run.py
└── README.md

## Setup

### 1. Clone the Repository

\`\`\`bash
git clone <repository-url>
cd <repository-directory>
\`\`\`

### 2. Prepare the Environment

Ensure you have Docker installed on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### 3. Build the Docker Image

\`\`\`bash
docker build -t loan_approval_api .
\`\`\`

### 4. Run the Docker Container

\`\`\`bash
docker run -p 5002:5000 loan_approval_api
\`\`\`

- **5002:5000**: Maps port 5002 on your local machine to port 5000 in the Docker container.

### 5. Access the API

You can access the API at \`http://localhost:5002\`.

## API Usage

### Predict Loan Approval

#### Endpoint

\`POST /predict\`

#### Request

Send a POST request with JSON payload containing the required features.

##### Example Request

\`\`\`bash
curl -X POST http://localhost:5002/predict -H "Content-Type: application/json" -d '{
    "no_of_dependents": 2,
    "education": "Graduate",
    "self_employed": "No",
    "income_annum": 9600000,
    "loan_amount": 29900000,
    "loan_term": 12,
    "cibil_score": 778,
    "residential_assets_value": 2400000,
    "commercial_assets_value": 17600000,
    "luxury_assets_value": 22700000,
    "bank_asset_value": 8000000,
    "income_to_loan_ratio": 0.321,
    "total_assets_value": 50700000,
    "loan_to_asset_ratio": 0.59,
    "dependents_to_income_ratio": 0,
    "loan_term_category": "Medium Term",
    "employment_education_interaction": "No_Graduate",
    "asset_to_income_ratio": 5.281,
    "annual_loan_payment": 2491666.667,
    "debt_to_income_ratio": 3.115,
    "average_asset_value": 12675000,
    "loan_payment_burden": 3.115,
    "asset_income_interaction": 486720000000000,
    "log_income_annum": 3.853,
    "log_loan_amount": 1469444.444,
    "loan_term_income_to_loan_ratio": 3.853,
    "loan_to_asset_annual_loan_payment": 399520000000000
}'
\`\`\`

#### Response

\`\`\`json
{
    "prediction": 1
}
\`\`\`

- \`prediction\`: The prediction result (e.g., 1 for approved, 0 for rejected).




