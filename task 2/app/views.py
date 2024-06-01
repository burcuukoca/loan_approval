from flask import Blueprint, request, jsonify
import pickle
import numpy as np
import logging
import pandas as pd

bp = Blueprint('main', __name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load the pipeline model
try:
    with open('app/loan_approval_model.pkl', 'rb') as file:
        model = pickle.load(file)
    logging.debug(f"Model loaded successfully: {model}")
    logging.debug(f"Model type: {type(model)}")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None

@bp.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded correctly"}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        # Convert the input data into a DataFrame to match the expected input format for the pipeline
        input_data = {
            'no_of_dependents': [float(data['no_of_dependents'])],
            'education': [data['education']],
            'self_employed': [data['self_employed']],
            'income_annum': [float(data['income_annum'])],
            'loan_amount': [float(data['loan_amount'])],
            'loan_term': [float(data['loan_term'])],
            'cibil_score': [float(data['cibil_score'])],
            'residential_assets_value': [float(data['residential_assets_value'])],
            'commercial_assets_value': [float(data['commercial_assets_value'])],
            'luxury_assets_value': [float(data['luxury_assets_value'])],
            'bank_asset_value': [float(data['bank_asset_value'])],
            'income_to_loan_ratio': [float(data['income_to_loan_ratio'])],
            'total_assets_value': [float(data['total_assets_value'])],
            'loan_to_asset_ratio': [float(data['loan_to_asset_ratio'])],
            'dependents_to_income_ratio': [float(data['dependents_to_income_ratio'])],
            'loan_term_category': [data['loan_term_category']],
            'employment_education_interaction': [data['employment_education_interaction']],
            'asset_to_income_ratio': [float(data['asset_to_income_ratio'])],
            'annual_loan_payment': [float(data['annual_loan_payment'])],
            'debt_to_income_ratio': [float(data['debt_to_income_ratio'])],
            'average_asset_value': [float(data['average_asset_value'])],
            'loan_payment_burden': [float(data['loan_payment_burden'])],
            'asset_income_interaction': [float(data['asset_income_interaction'])],
            'loan_term_income_to_loan_ratio': [float(data['loan_term_income_to_loan_ratio'])],
            'loan_to_asset_annual_loan_payment': [float(data['loan_to_asset_annual_loan_payment'])],
            'luxury_commercial_assets_value': [float(data['luxury_commercial_assets_value'])]
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame(input_data)
        logging.debug(f"Input DataFrame: {input_df}")

        # Verify the model and predict method
        logging.debug(f"Model has predict method: {hasattr(model, 'predict')}")

        # Make a prediction using the pipeline model
        prediction = model.predict(input_df)
        logging.debug(f"Prediction: {prediction}")

        # Ensure the prediction is a native Python type
        prediction_result = prediction[0]
        if isinstance(prediction_result, np.generic):
            prediction_result = prediction_result.item()

        return jsonify({"prediction": prediction_result})
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500
