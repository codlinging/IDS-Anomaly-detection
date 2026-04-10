# train_custom_model.py
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from data_prep import load_and_preprocess_data
from config import LOCAL_MODEL_PATH

# --- TRAINING CONFIGURATION ---
# Change this to the name of your downloaded dataset
CUSTOM_DATASET_CSV = "my_custom_network_data.csv" 
# Change this to the name of the column that says "Attack" or "Normal" (usually 'label' or 'class')
TARGET_LABEL_COLUMN = "label" 

def train_model():
    print("=== CUSTOM MODEL TRAINING PIPELINE ===")
    
    # 1. Get the cleaned data
    X_train, X_test, y_train, y_test = load_and_preprocess_data(CUSTOM_DATASET_CSV, TARGET_LABEL_COLUMN)
    
    if X_train is None:
        return # Stop if data wasn't found
        
    # 2. Initialize the AI Model
    # Random Forest is highly accurate and fast for tabular network data
    print("[*] Initializing Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    
    # 3. Train the Model
    print("[*] Training the model... (This may take a few minutes depending on dataset size)")
    model.fit(X_train, y_train)
    
    # 4. Evaluate the Model
    print("[*] Evaluating model accuracy on test data...")
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    print(f"\n--- TRAINING RESULTS ---")
    print(f"Accuracy: {accuracy * 100:.2f}%\n")
    print("Detailed Classification Report:")
    print(classification_report(y_test, predictions))
    
    # 5. Save the Model
    print(f"\n[*] Saving trained model to {LOCAL_MODEL_PATH}...")
    joblib.dump(model, LOCAL_MODEL_PATH)
    
    print("[*] DONE! Your Streamlit app will now automatically use this custom model.")

if __name__ == "__main__":
    train_model()