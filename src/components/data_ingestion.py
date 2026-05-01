import pandas as pd

class DataIngestion:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            print("Data loaded successfully")
            print("Shape:", df.shape)
            return df

        except Exception as e:
            print("Error in data ingestion:", e)
            raise e