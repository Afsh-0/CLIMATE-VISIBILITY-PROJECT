import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

class DataTransformation:

    def __init__(self):
        self.scaler = StandardScaler()

    def transform_data(self, df: pd.DataFrame):

        # ----------------------------
        # Feature Engineering
        # ----------------------------
        df['DATE'] = pd.to_datetime(df['DATE'])

        df['year'] = df['DATE'].dt.year
        df['month'] = df['DATE'].dt.month
        df['hour'] = df['DATE'].dt.hour

        df.drop('DATE', axis=1, inplace=True)

        # ----------------------------
        # Drop unwanted columns
        # ----------------------------
        df.drop(['WETBULBTEMPF', 'DewPointTempF', 'StationPressure', 'Precip'], axis=1, inplace=True)

        # ----------------------------
        # Split X and y
        # ----------------------------
        X = df.drop('VISIBILITY', axis=1)
        y = df['VISIBILITY']

        # Save feature order (IMPORTANT)
        feature_columns = list(X.columns)

        # ----------------------------
        # Train-test split
        # ----------------------------
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # ----------------------------
        # Scaling
        # ----------------------------
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)

        # ----------------------------
        # SAVE SCALER + FEATURES
        # ----------------------------
        os.makedirs("artifacts", exist_ok=True)

        joblib.dump(self.scaler, "artifacts/scaler.pkl")
        joblib.dump(feature_columns, "artifacts/feature_columns.pkl")

        print("Transformation completed")

        return X_train, X_test, y_train, y_test, feature_columns