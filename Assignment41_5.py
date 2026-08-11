import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def main():
    Border = "-" * 50

    print(Border)
    print("Step 5 : Calculate Accuracy")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    df.dropna(inplace=True)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    # Feature Scaling

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create Model

    model = KNeighborsClassifier(n_neighbors=5)

    # Train Model

    model.fit(X_train_scaled, Y_train)

    # Test Model

    Y_pred = model.predict(X_test_scaled)

    # Calculate Accuracy

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Actual Values : ")
    print(Y_test.to_list())

    print(Border)

    print("Predicted Values : ")
    print(Y_pred)

    print(Border)

    print("Accuracy : ", Accuracy * 100, "%")

    print(Border)


if __name__ == "__main__":
    main()