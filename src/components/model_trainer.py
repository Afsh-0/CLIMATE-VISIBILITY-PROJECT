import os
import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score

from sklearn.metrics import r2_score

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation


class ModelTrainer:

    def __init__(self):
        self.models = {
            "LinearRegression": LinearRegression(),
            "Ridge": Ridge(),
            "Lasso": Lasso(),
            "ElasticNet": ElasticNet(),
            "DecisionTree": DecisionTreeRegressor(),

            #IMPROVED RANDOM FOREST (IMPORTANT)
            "RandomForest": RandomForestRegressor(
                n_estimators=400,
                max_depth=18,
                min_samples_split=4,
                min_samples_leaf=1,
                random_state=42,
                n_jobs=-1
            )
        }

    def train_and_select_model(self, X_train, X_test, y_train, y_test):

        results = []

        for name, model in self.models.items():

            model.fit(X_train, y_train)

            pred = model.predict(X_test)

            #CROSS VALIDATION SCORE (IMPROVES ACCURACY RELIABILITY)
            cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring="r2")
            cv_score = cv_scores.mean()

            test_score = r2_score(y_test, pred)

            final_score = (cv_score + test_score) / 2

            results.append((name, final_score))

            print(f"{name} -> CV Score: {cv_score:.4f} | Test Score: {test_score:.4f}")

        results_df = pd.DataFrame(results, columns=["Model", "Score"])
        results_df = results_df.sort_values(by="Score", ascending=False)

        best_model_name = results_df.iloc[0]["Model"]
        best_model = self.models[best_model_name]

        print("\nBest Model Selected:", best_model_name)

        os.makedirs("artifacts", exist_ok=True)

        joblib.dump(best_model, "artifacts/model.pkl")

        print("Model saved successfully")


if __name__ == "__main__":

    # STEP 1: LOAD DATA
    ingestion = DataIngestion("data/data.csv")
    df = ingestion.load_data()

    # STEP 2: TRANSFORM DATA
    transformer = DataTransformation()
    X_train, X_test, y_train, y_test, features = transformer.transform_data(df)

    # STEP 3: TRAIN MODEL
    trainer = ModelTrainer()
    trainer.train_and_select_model(X_train, X_test, y_train, y_test)