# Credit Card Fraud Detection (Flask + ML)
This project is a Flask web app that helps detect fraudulent credit card transactions.
It uses a trained machine learning model (by default, a Random Forest) to analyze transaction details.

Users can:

- Enter transaction information through the web interface.

- Automatically generate the necessary features for the model.

- Get a clear prediction on whether the transaction is fraudulent or legitimate.

## Features
- **Simple Web Interface**
    Built with plain HTML and CSS, keeping the design clean and lightweight without external frameworks.

- **User Inputs**
    Accepts only two inputs from the user: Amount and Time of the transaction.

- **Automatic Feature Generation**
    Generates the additional V1–V28 anonymized features required by the machine learning model.

- **Clear Prediction Results**
    Displays a straightforward output: Fraudulent or Not Fraudulent.

- **Offline Friendly**
    Works entirely offline without relying on Bootstrap or external CDNs.

## Project Structure

```plaintext
fraud-detection-app/
│
├── app.py                 # Flask backend
├── model.pkl              # Trained Random Forest model (pre-saved)
│
├── templates/
│   └── index.html         # Frontend HTML
│
├── static/
│   └── style.css          # Custom styling
│
└── README.md              # Project documentation
```

# Installation & Setup

1. Clone or download this repository.

2. Create a Python virtual environment and activate it

3. Install required dependencies:

flask, scikit-learn, pandas, numpy and imbalanced-learn

4. Run the Flask app:

python app.py

5. Open your browser and go to:

http://127.0.0.1:5000

## How to Use

1. Enter Amount and Time of a transaction.

2. The app generates the other required features automatically.

3. Click Predict.

4. The app shows if the transaction is Fraud (red) or Not Fraud (green).

## How the Project Works

1. Dataset

    - The project uses the Credit Card Fraud Detection dataset from Kaggle (creditcard.csv).

    - Each row represents a credit card transaction.

    - Columns:

        - Time — seconds elapsed from the first transaction in the dataset.

        - Amount — transaction amount in the currency used.

        - Class — target variable: 0 = legitimate, 1 = fraud.

      - V1 to V28 — anonymized features obtained via PCA (Principal Component Analysis). These represent various properties of the transactions, but the exact meaning is hidden to protect sensitive data.

2. User Input

    - The web app asks the user to enter:

        - Amount — the transaction amount.

        - Time — seconds from the first transaction (as in the dataset).

    - All other features (V1–V28) are randomly generated for demonstration purposes. In a real dataset, these would come from pre-processed transaction data.

3. Data Processing

    - The features are scaled using StandardScaler to match the training distribution.

    - If retraining is needed, SMOTE is used to balance fraud vs legitimate transactions because fraud cases are very rare.

4. Model

    - A Random Forest Classifier is trained on the dataset using GridSearchCV to find optimal hyperparameters.

    - The model predicts whether a transaction is Fraudulent (1) or Legitimate (0).

5. Web App

    - The Flask app takes the user input, generates the random V1–V28, scales features, and feeds them to the model.

    - It displays:

        - The randomly generated V1–V28 values.

        - The model’s prediction: Fraudulent or Legitimate.

6. Limitations

    - The anonymized features (V1–V28) are random for demonstration, so predictions are illustrative only.

    - The model works offline and uses a small Random Forest, suitable for education and demo purposes only.

    - Fraud detection accuracy is limited because real transactions have structured V1–V28 values; random values don’t represent actual patterns.