from src.components.data_ingestion import DataIngestion

def main():
    ingestion = DataIngestion("data/data.csv")  # change path
    df = ingestion.load_data()

    print(df.head())

if __name__ == "__main__":
    main()