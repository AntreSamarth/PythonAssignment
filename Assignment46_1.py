import pandas as pd
from sklearn.linear_model import LinearRegression


def MarvellousRegression(DataPath):

    Border = "-" * 50

    # Step 1 : Get Data
    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head())
    print("Shape of Dataset : ", df.shape)

    # Step 2 : Clean, Prepare and Manipulate Data
    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print("Columns : ", df.columns.tolist())
    print("Missing Values : ")
    print(df.isnull().sum())

    # Separate input and output
    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    # Step 3 : Train Data
    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    # First half for training
    X_train = X.iloc[:100]
    Y_train = Y.iloc[:100]

    print("Training Data Shape : ", X_train.shape)
    print("Training Target Shape : ", Y_train.shape)

    model = LinearRegression()

    model = model.fit(X_train, Y_train)

    print("Model training completed")

    # Step 4 : Test Data
    print(Border)
    print("Step 4 : Test Data")
    print(Border)

    # Remaining half for testing
    X_test = X.iloc[100:]
    Y_test = Y.iloc[100:]

    print("Testing Data Shape : ", X_test.shape)
    print("Testing Target Shape : ", Y_test.shape)

    # Step 5 : Prediction
    print(Border)
    print("Step 5 : Predicted Values and Expected Values")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Predicted Values\tExpected Values")
    print(Border)

    for predicted, expected in zip(Y_pred, Y_test):
        print(f"{predicted:.2f}\t\t\t{expected:.2f}")

    print(Border)


def main():

    MarvellousRegression("Advertising (1).csv")


if __name__ == "__main__":
    main()