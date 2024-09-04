def extract_features(data):
    # Extract key features for predicting match outcome
    data['odds_diff'] = data['home_odds'] - data['away_odds']
    data['goal_diff'] = data['home_goals'] - data['away_goals']
    data['win_probability'] = 1 / data['home_odds']  # Example: win probability based on home odds

    # Advanced features: performance history, recent form, etc.
    data['recent_form'] = (data['home_goals'] + data['away_goals']) / data['total_goals']

    # Select important features
    features = data[['odds_diff', 'goal_diff', 'win_probability', 'recent_form']]

    return features
