🌐 Fraud Analytics System with Feature Engineering \& ML

An end-to-end fraud detection system built using:

Python for data cleaning, feature engineering, EDA \& ML

PostgreSQL for structured storage and SQL analytics

Machine Learning (Logistic Regression \& Random Forests)

Jupyter Notebooks for clean workflow documentation

This project demonstrates a complete industry-style data science workflow, including:

✔ Handling highly imbalanced data
✔ Creating meaningful engineered features
✔ Training ML models
✔ Evaluating performance with ROC-AUC, precision, recall, and feature importance

Dataset Credits:
🔗 https://www.kaggle.com/datasets/reemkasaab/fraud-detection

📁 Project Structure
fraud-detection-project/
│
├── data/
│   ├── data.csv                  # Original dataset
│   ├── cleaned\_data.csv          # After cleaning
│   └── engineered\_data.csv       # After feature engineering
│
├── notebooks/
│   ├── 01\_data\_loading\_and\_cleaning.ipynb
│   ├── 02\_sql\_exploration.ipynb
│   ├── 03\_eda.ipynb
│   ├── 04\_feature\_engineering.ipynb
│   └── 05\_model\_training.ipynb
│
├── models/
│   ├── random\_forest\_model.pkl   # Final ML model
│   └── scaler.pkl                # Scaler for inference
│
├── scripts/
│   └── load\_to\_postgres.py       # Inserts data into PostgreSQL
│
├── README.md
└── requirements.txt
🧹 Data Cleaning

Performed inside 01\_data\_loading\_and\_cleaning.ipynb

✔ Steps Completed

Removed duplicates

Converted timestamps (trans\_date\_trans\_time, dob)

Handled missing values

Dropped irrelevant or high-cardinality columns

first, last

street, city, state

job, trans\_num

Exported cleaned dataset as:

data/cleaned\_data.csv

These steps ensure clean and structured input for analysis and modeling.

🔍 Exploratory Data Analysis (EDA)

Performed inside 03\_eda.ipynb

Key Insights

📊 Fraud vs Non-Fraud Distribution

Dataset is highly imbalanced

Fraud cases are extremely rare

💰 Transaction Amount Analysis

Fraud transactions often involve extreme or unusual amounts

🛒 Fraud by Merchant Category

Some categories show a higher fraud proportion

⏱️ Time-of-Day Patterns

Fraud spikes at specific hours

Weekend behavior differs from weekdays

🔥 Correlation Heatmap

Shows relationships between numerical features like amount, distance, population, etc.

You may add screenshots by dragging images into GitHub README editor.

⚙ Feature Engineering

Performed inside 04\_feature\_engineering.ipynb

Feature engineering is a major strength of this project.

🕒 Time-Based Features

Extracted from trans\_date\_trans\_time:

hour

day

month

weekday

is\_weekend

👤 Customer Age

Calculated using:

age = current\_date - dob
📍 Haversine Distance (distance\_km)

Distance between customer coordinates and merchant coordinates.

Fraudulent transactions often occur far from the user’s typical location

This became one of the top features in Random Forest

🛍 Merchant Category Encoding

One-hot encoded the category column

🧹 Columns Dropped

Personal details (first, last, street, city, state)

High-cardinality fields (job, trans\_num)

Raw timestamps (after extracting useful parts)

💾 Final Output
data/engineered\_data.csv
🤖 Machine Learning Model Training

Performed inside 05\_model\_training.ipynb

Because of the imbalanced dataset, training required:

Stratification

Proper scaling

Class weighting

📏 Data Splitting \& Scaling

Used stratified train-test split:

train\_test\_split(..., stratify=y)

Scaled numeric features with:

StandardScaler()
📌 Models Trained
1️⃣ Logistic Regression (Baseline)

class\_weight="balanced"

max\_iter=500

Good interpretability

Establishes baseline metrics

2️⃣ Random Forest Classifier (Best Model)

Parameters:

n\_estimators = 200

max\_depth = 12

class\_weight = "balanced"

Random Forest performed the best on this dataset.

📈 Model Performance
🏆 Random Forest (Best Results)
Metric	Score
Accuracy	~0.99
Precision	High
Recall	High
F1-score	High
ROC-AUC	~0.98
📊 Sample Classification Report
precision    recall  f1-score   support
0              1.00       0.95      0.97      368549
1              0.86       0.35      0.50        4196
🔥 Feature Importance (Random Forest)

Top predictors include:

distance\_km

amt

hour

weekday

Encoded merchant categories

These help explain why the model predicts fraud.

💾 Model Saving \& Deployment Readiness

Exported with joblib:

models/
├── random\_forest\_model.pkl
└── scaler.pkl

These can be loaded for:

API deployment

Streamlit app

Batch inference

Real-time fraud scoring

Example usage:
import joblib

model = joblib.load("models/random\_forest\_model.pkl")
scaler = joblib.load("models/scaler.pkl")
🗄 SQL Integration (PostgreSQL)

Dataset imported into PostgreSQL using load\_to\_postgres.py.

Example SQL query:

SELECT city, amt, is\_fraud
FROM transactions
WHERE amt > 2000
ORDER BY trans\_date\_trans\_time DESC;

This demonstrates the backend integration typical in fraud detection systems.

🚀 How to Run This Project
1️⃣ Clone the Repository
git clone https://github.com/mayank260201/fraud-detection-project.git
cd fraud-detection-project
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Jupyter Notebooks
jupyter notebook

Run the notebooks in order:

01\_data\_loading\_and\_cleaning.ipynb

02\_sql\_exploration.ipynb

03\_eda.ipynb

04\_feature\_engineering.ipynb

05\_model\_training.ipynb

4️⃣ Load Data to PostgreSQL (Optional)
python scripts/load\_to\_postgres.py
5️⃣ Make Predictions
prediction = model.predict(scaled\_data)
🙌 Credits

Dataset author: Reem Kasaab
Source: https://www.kaggle.com/datasets/reemkasaab/fraud-detection

⭐ Final Notes

This project demonstrates an end-to-end, real-world fraud detection pipeline:

✔ Data Cleaning
✔ Exploratory Analysis
✔ SQL + Python Integration
✔ Feature Engineering
✔ Handling Imbalanced Data
✔ Machine Learning Modeling
✔ Model Saving for Deployment
✔ Completely Reproducible Pipeline

Roles this project aligns with:

Data Scientist

ML Engineer

Fraud Analyst

AI Engineer

Data Analyst

Feel free to open an issue or reach out if you'd like to collaborate. 🚀

