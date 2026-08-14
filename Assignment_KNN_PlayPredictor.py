import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X, Y, K):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.5, random_state=42
    )

    model = KNeighborsClassifier(n_neighbors=K)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    return Accuracy


def MarvellousClassifier(DataPath):
    Border = "-" * 50

    # Step 1 : Get Data
    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df)
    print(Border)

    # Step 2 : Clean, Prepare and Manipulate Data
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(Border)

    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    # CSV column is Wether
    df['Wether'] = WeatherEncoder.fit_transform(df['Wether'])
    df['Temperature'] = TemperatureEncoder.fit_transform(df['Temperature'])
    df['Play'] = PlayEncoder.fit_transform(df['Play'])

    print(df)
    print(Border)

    # Separate input and output
    X = df[['Wether', 'Temperature']]
    Y = df['Play']

    # Step 3 : Train Data
    print("Step 3 : Train Data")
    print(Border)

    K = 3

    model = KNeighborsClassifier(n_neighbors=K)

    model.fit(X, Y)

    print("Model training completed")
    print(Border)

    # Step 4 : Test Data
    print("Step 4 : Test Data")
    print(Border)

    print("Available Weather values:")
    print("Sunny, Overcast, Rainy")

    print("Available Temperature values:")
    print("Hot, Mild, Cool")

    Weather = input("Enter Weather: ")
    Temperature = input("Enter Temperature: ")

    WeatherValue = WeatherEncoder.transform([Weather])[0]
    TemperatureValue = TemperatureEncoder.transform([Temperature])[0]

    TestData = [[WeatherValue, TemperatureValue]]

    Result = model.predict(TestData)

    FinalResult = PlayEncoder.inverse_transform(Result)

    print("Predicted Result:", FinalResult[0])

    print(Border)

    # Step 5 : Calculate Accuracy
    print("Step 5 : Calculate Accuracy")
    print(Border)

    for K in range(1, 6):

        Accuracy = CheckAccuracy(X, Y, K)

        print(
            "K =", K,
            "Accuracy =", Accuracy * 100, "%"
        )

    print(Border)


def main():
    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")


if __name__ == "__main__":
    main()