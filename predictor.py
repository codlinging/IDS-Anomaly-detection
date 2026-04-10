# predictor.py
from model_manager import get_ai_model

def analyze_traffic(traffic_df):
    """Runs the AI model against the traffic data and returns results."""
    model = get_ai_model()
    
    # We need to drop the fake IP strings before feeding data to the ML model
    features_only = traffic_df.drop(columns=["Source_IP", "Dest_IP"])
    
    # Ensure we only pass the exact number of features the model expects
    expected_features = model.n_features_in_
    test_traffic = features_only.iloc[:, :expected_features]
    
    predictions = model.predict(test_traffic)
    
    # Add predictions back into the dataframe for the dashboard to display
    traffic_df["Is_Anomaly"] = predictions
    traffic_df["Status"] = traffic_df["Is_Anomaly"].apply(
        lambda x: "🚨 Attack" if x == 1 else "✅ Safe"
    )
    
    return traffic_df