# 🛡️ Real-Time AI Network Intrusion Detection System (IDS)

An interactive, AI-driven dashboard that monitors simulated network traffic and detects anomalies using Machine Learning. Built with Python, Scikit-Learn, and Streamlit.

## 📖 Project Overview
Traditional Intrusion Detection Systems (IDS) rely on strict signature-based rules. This project takes a modern approach by utilizing a **Random Forest Machine Learning Classifier** to analyze network packet behavior (based on the NSL-KDD dataset features) and identify zero-day anomalies that standard firewalls might miss.

### ✨ Features
* **Real-Time Traffic Simulation:** Generates mock network packets with 41 distinct features.
* **AI Anomaly Detection:** Uses a trained Machine Learning model to classify traffic as "Safe" or an "Attack".
* **Interactive Dashboard:** Built with Streamlit to visualize traffic distribution, total packets analyzed, and a real-time incident log.
* **Custom Training Pipeline:** Includes backend scripts to ingest raw CSV data, preprocess it, and train a custom local model.

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Serialization:** Joblib

## 🗂️ Project Structure
```text
├── app.py                  # Main Streamlit dashboard UI
├── config.py               # Global settings and configurations
├── data_generator.py       # Simulates live network traffic for the dashboard
├── data_prep.py            # Preprocesses custom CSV datasets for training
├── model_manager.py        # Loads the AI model into memory
├── predictor.py            # The bridge between the data and the AI model
├── train_custom_model.py   # Pipeline to train a new AI model from scratch
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation