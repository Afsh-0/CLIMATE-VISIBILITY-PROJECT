from src.pipeline.predict_pipeline import PredictionPipeline

def main():

    sample_data = {
        "DRYBULBTEMPF": 25.0,
        "RelativeHumidity": 60,
        "WindSpeed": 5.2,
        "WindDirection": 180,
        "SeaLevelPressure": 1013,
        "year": 2024,
        "month": 4,
        "hour": 10
    }

    pipeline = PredictionPipeline()
    result = pipeline.predict(sample_data)

    print("Prediction:", result)

if __name__ == "__main__":
    main()