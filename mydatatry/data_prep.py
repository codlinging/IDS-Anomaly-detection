# data_prep.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_data(csv_file_path, target_column):
    """
    Loads a custom CSV dataset, encodes text to numbers, scales the data, 
    and splits it into training and testing sets.
    """
    print(f"[*] Loading dataset from {csv_file_path}...")
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"[!] Error: Could not find {csv_file_path}. Please ensure the file is in your folder.")
        return None, None, None, None

    print("[*] Cleaning and preprocessing data...")
    
    # 1. Separate features (X) and the target label (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # 2. Encode categorical (text) columns into numbers
    # AI models only understand numbers, so "TCP" becomes 0, "UDP" becomes 1, etc.
    label_encoders = {}
    for column in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[column] = le.fit_transform(X[column])
        label_encoders[column] = le 

    # 3. Split the data (80% for training the AI, 20% for testing it)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Scale the numerical data
    # This prevents huge numbers (like bytes transferred) from overpowering small numbers
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print(f"[*] Preprocessing complete. Training samples: {len(X_train)}, Testing samples: {len(X_test)}")
    return X_train, X_test, y_train, y_test