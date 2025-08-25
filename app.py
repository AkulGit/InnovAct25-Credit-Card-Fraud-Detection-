import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

# Load dataset
df = pd.read_csv("creditcard.csv", sep='\t')  # use tab separator
print(df.columns)

target_col = "Class" 
X = df.drop(target_col, axis=1) #input features
y = df[target_col] #target variable

# train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#20% for testing, rest 80% for training.
#random state fixes random shuffling i.e produces reproducible results
#train variables train the model, test variables evaluate it.


#Scale features -> adjust measurements so that they're on the same scale so that the algorithm treats them equally
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# GridSearchCV for RandomForest
#definging the hyperparameters grid
param_grid = {
    "n_estimators": [50, 100, 150], #no of trees
    "max_depth": [None, 10, 20], #max depth of each tree
    "min_samples_split": [2, 5], #min samples required to split a node 
    "min_samples_leaf": [1, 2] #min samples required at a leaf node 
}

#finds best parameters, uses all cpu cores 
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, n_jobs=-1)
#trains Random forest for every combination of hyperparameters in the grid
grid.fit(X_train_scaled, y_train)

best_model = grid.best_estimator_

# Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    generated_features = None
    prediction = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        time = float(request.form["time"])

        # Randomly generate V1-V28
        v_features = {}
        for i in range(1, 29):
            col = f"V{i}"
            mean, std = X_train[col].mean(), X_train[col].std()
            v_features[col] = np.random.normal(mean, std)

        # Combine features
        features = [v_features[f"V{i}"] for i in range(1, 29)] + [amount, time]

        # Scale and predict
        features_scaled = scaler.transform([features])
        pred_class = best_model.predict(features_scaled)[0]
        prediction = "Fraud" if pred_class == 1 else "Not Fraud"

        generated_features = v_features

    return render_template("index.html", prediction=prediction, generated_features=generated_features)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
