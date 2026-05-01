import joblib
import pandas as pd

class PredictionPipeline:

    def __init__(self):
        self.model = joblib.load("artifacts/model.pkl")
        self.scaler = joblib.load("artifacts/scaler.pkl")
        self.features = joblib.load("artifacts/feature_columns.pkl")

    def predict(self, data):

        # Convert input to DataFrame
        if isinstance(data, dict):
            data = pd.DataFrame([data])

        # Ensure ALL required features exist
        for col in self.features:
            if col not in data.columns:
                data[col] = 0  # safe default for missing values

        # Keep correct column order
        data = data[self.features]

        # Apply scaling (same as training)
        data_scaled = self.scaler.transform(data)

        # Prediction
        prediction = self.model.predict(data_scaled)

        return prediction[0]