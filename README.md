# CLIMATE VISIBILITY PROJECT (End-to-End ML Project)

## 📌 Overview
This project predicts weather visibility using machine learning based on meteorological features.

---

## 🚀 Features
- Data ingestion pipeline
- Feature engineering
- Multiple ML models comparison
- Random Forest best model selection
- Scalable prediction pipeline
- Production-style project structure

---

## 🏗️ Project Structure 
data/
notebooks/
config/
src/
static/
artifacts/
logs/
app.py
test.py
requirements.txt
setup.py
README.md

---

## 📊 Input Features

- DRYBULBTEMPF
- RelativeHumidity
- WindSpeed
- WindDirection
- SeaLevelPressure
- year
- month
- hour

---

## 🧠 Machine Learning Models Used
- Linear Regression
- Ridge Regression
- Decision Tree
- Random Forest (Best Model)

---

## ⚙️ How to Run This Project

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Train the model
python -m src.components.model_trainer

3. Run prediction
python test.py

## 📊 Results

- The model was trained and evaluated using multiple regression algorithms.
- Random Forest performed the best among all models.
- Final model provides stable predictions for weather visibility.
- Evaluation was done using R² score on test data.

## 📦 Output

The system takes weather parameters as input and predicts visibility as a numeric value.

Example:

Input:
- Temperature: 25°C
- Humidity: 60%
- Wind Speed: 5.2

Output:
- Predicted Visibility: 9.33

## 👨‍💻 Author

- Name: Afsha 
- Role: Data Science & Machine Learning Enthusiast  
- Focus: End-to-end ML systems and deployment-ready projects