from data_fetcher import fetch_all_data
from data_preprocessing import preprocess_data
from feature_engineering import extract_features
from modeling import train_model
import asyncio

def integrate_data_and_train():
    # Fetch all data
    data = asyncio.run(fetch_all_data())

    # Preprocess the data
    processed_data = preprocess_data(*data)

    # Extract features
    features = extract_features(processed_data)

    # Mock target variable (e.g., match outcome)
    labels = processed_data['match_outcome']  # Assuming match_outcome exists

    # Train the model
    model = train_model(features, labels)

    return model
