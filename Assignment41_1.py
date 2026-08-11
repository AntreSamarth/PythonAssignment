import pandas as pd

def main():
    Border = "-" * 50

    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    print("First 5 records : ")
    print(df.head())

    print(Border)
    print("Dataset Shape : ", df.shape)

    print(Border)
    print("Column Names : ")
    print(df.columns.tolist())

    print(Border)


if __name__ == "__main__":
    main()