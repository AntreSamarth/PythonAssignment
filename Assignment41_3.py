import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

def main():
    Border = "-" * 50

    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    df.dropna(inplace=True)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    # Split data into training and testing

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("X_train Shape : ", X_train.shape)
    print("X_test Shape  : ", X_test.shape)

    print("Y_train Shape : ", Y_train.shape)
    print("Y_test Shape  : ", Y_test.shape)

    print(Border)

    # Feature Scaling

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature Scaling Completed")

    print(Border)

    # Create KNN model

    model = KNeighborsClassifier(n_neighbors=5)

    # Train model

    model.fit(X_train_scaled, Y_train)

    print("Model Training Completed")

    print(Border)


if __name__ == "__main__":
    main()