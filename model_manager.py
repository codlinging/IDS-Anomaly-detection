# model_manager.py
import os
import shutil
import joblib
from huggingface_hub import hf_hub_download
from config import REPO_ID, MODEL_FILENAME, LOCAL_MODEL_PATH

def get_ai_model():
    """Loads the model from disk if it exists, otherwise downloads it."""
    if os.path.exists(LOCAL_MODEL_PATH):
        return joblib.load(LOCAL_MODEL_PATH)
    
    print(f"[*] Downloading {MODEL_FILENAME} from Hugging Face...")
    temp_model_path = hf_hub_download(repo_id=REPO_ID, filename=MODEL_FILENAME)
    
    # Save to local directory
    shutil.copy(temp_model_path, LOCAL_MODEL_PATH)
    
    return joblib.load(LOCAL_MODEL_PATH)