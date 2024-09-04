import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(data):
    # Handle missing values by dropping or imputing
    data = data.dropna()

    # Correct noisy data, e.g., correcting extreme odds or incorrect scores
    data = data[(data['home_odds'] > 1) & (data['away_odds'] > 1)]

    return data

def preprocess_data(pinnacle_data, livescore_data, football_data):
    pinnacle_df = pd.DataFrame(pinnacle_data)
    livescore_df = pd.DataFrame(livescore_data)
    football_df = pd.DataFrame(football_data)

    # Clean the data
    pinnacle_df = clean_data(pinnacle_df)
    livescore_df = clean_data(livescore_df)
    football_df = clean_data(football_df)

    # Merge datasets
    merged_data = pd.concat([pinnacle_df, livescore_df, football_df], axis=1)

    # Feature Scaling using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(merged_data[['home_odds', 'away_odds', 'total_goals']])

    return pd.DataFrame(scaled_data, columns=['home_odds_scaled', 'away_odds_scaled', 'total_goals_scaled'])
