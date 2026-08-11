import pandas as pd

def main():
    Border = "-" * 50

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    print("Original Shape : ", df.shape)

    # Remove missing values
    df.dropna(inplace=True)

    print("Shape after cleaning : ", df.shape)

    print(Border)

    # Separate Independent and Dependent variables

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(Border)

    print("Input Features : ")
    print(X.columns.tolist())

    print(Border)

    print("Output Classes : ")
    print(Y.unique())

    print(Border)


if __name__ == "__main__":
    main()