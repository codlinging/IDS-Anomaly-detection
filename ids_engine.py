import os
import shutil
import pandas as pd
import numpy as np
import joblib
from huggingface_hub import hf_hub_download

# Define the name of our local model file
LOCAL_MODEL_NAME = "local_ids_model.joblib"

def generate_mock_traffic():
    """Generates 5 rows of mock network traffic (41 features)."""
    print("[*] Generating mock network traffic data...")
    mock_data = np.random.rand(5, 41) 
    columns = [f"Feature_{i}" for i in range(1, 42)]
    return pd.DataFrame(mock_data, columns=columns)

def load_or_download_model():
    """
    Checks if the model exists locally. If not, downloads it from Hugging Face
    and saves a copy in the project folder for all future runs.
    """
    # 1. Check if we already downloaded it in a previous run
    if os.path.exists(LOCAL_MODEL_NAME):
        print(f"[*] Success: Found local model '{LOCAL_MODEL_NAME}'. Skipping download.")
        print("[*] Loading local model into memory...")
        return joblib.load(LOCAL_MODEL_NAME)
    
    # 2. If it doesn't exist, download it from Hugging Face
    print(f"[*] Local model not found. Contacting Hugging Face Hub...")
    repo_id = "merve/adult_income_rf" # Placeholder for testing
    filename = "sklearn_model.joblib"
    
    # Download the file to Hugging Face's temporary cache
    temp_model_path = hf_hub_download(repo_id=repo_id, filename=filename)
    
    # 3. Copy the file from the hidden cache into our project folder
    print(f"[*] Saving a permanent local copy as '{LOCAL_MODEL_NAME}'...")
    shutil.copy(temp_model_path, LOCAL_MODEL_NAME)
    
    # 4. Load the newly saved local model
    print("[*] Loading model into memory...")
    return joblib.load(LOCAL_MODEL_NAME)

def run_ids():
    traffic_df = generate_mock_traffic()
    
    # Use our new optimized loading function
    ai_model = load_or_download_model()
    
    print("\n[*] Analyzing traffic for anomalies...")
    
    expected_features = ai_model.n_features_in_
    test_traffic = traffic_df.iloc[:, :expected_features]
    
    predictions = ai_model.predict(test_traffic)
    
    print("\n--- IDS ALERT DASHBOARD ---")
    for index, prediction in enumerate(predictions):
        status = "🚨 ANOMALY DETECTED" if prediction == 1 else "✅ Normal Traffic"
        print(f"Packet #{index + 1}: {status}")

if __name__ == "__main__":
    run_ids()