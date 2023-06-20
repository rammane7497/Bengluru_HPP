import os

BASE_PATH = os.getcwd()

CSV_PATH = os.path.join(BASE_PATH, r'csv_files/cleaned_banglore_hpp.csv')

MODEL_PATH = os.path.join(BASE_PATH, r'artifacts/ridge_regression_model.pkl')

PORT_NUMBER = 5001