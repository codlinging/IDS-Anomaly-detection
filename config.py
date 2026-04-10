# config.py
import os

# Model Settings
REPO_ID = "merve/adult_income_rf" # Placeholder tabular model
MODEL_FILENAME = "sklearn_model.joblib"
LOCAL_MODEL_PATH = os.path.join(os.getcwd(), "local_ids_model.joblib")

# Data Settings
NUM_FEATURES = 41 # NSL-KDD standard features
DEFAULT_ROWS = 20 # How many packets to simulate in the dashboard

# Dashboard Settings
APP_TITLE = "Real-Time AI Network Intrusion Detection"