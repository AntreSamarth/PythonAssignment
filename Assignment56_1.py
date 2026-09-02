import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


def MarvellousFraudDetection(DataPath):

    Border = "-" * 60

    # Step 1 : Load the dataset

    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Shape of Dataset : ", df.shape)

    print("First few records : ")
    print(df.head())

    print(Border)

    # Step 2 : Check for missing values

    print(Border)
    print("Step 2 : Check for Missing Values")
    print(Border)

    print(df.isnull().sum())

    print(Border)

    # Step 3 : Separate input and output variables

    print(Border)
    print("Step 3 : Separate Input and Output Variables")
    print(Border)

    X = df.drop("Fraud", axis=1)
    Y = df["Fraud"]

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print("Input Features : ")
    print(X.columns.tolist())

    print("Output Feature : Fraud")

    print(Border)

    # Step 4 : Split dataset for training and testing

    print(Border)
    print("Step 4 : Split Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
                                                        X,
                                                        Y,
                                                        test_size=0.2,
                                                        random_state=42,
                                                        stratify=Y
                                                        )

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)

    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)

    print(Border)

    # Step 5 : Decision Tree

    print(Border)
    print("Step 5 : Train Decision Tree")
    print(Border)

    DecisionTree = DecisionTreeClassifier(random_state=42)

    DecisionTree.fit(X_train, Y_train)

    Y_pred_DT = DecisionTree.predict(X_test)

    Accuracy_DT = accuracy_score(Y_test, Y_pred_DT)
    Precision_DT = precision_score(Y_test, Y_pred_DT, zero_division=0)
    Recall_DT = recall_score(Y_test, Y_pred_DT, zero_division=0)
    F1_DT = f1_score(Y_test, Y_pred_DT, zero_division=0)

    print("Accuracy : ", Accuracy_DT)
    print("Precision : ", Precision_DT)
    print("Recall : ", Recall_DT)
    print("F1 Score : ", F1_DT)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred_DT))

    # Step 6 : Bagging Classifier

    print(Border)
    print("Step 6 : Train Bagging Classifier")
    print(Border)

    Bagging = BaggingClassifier(
                                n_estimators=50,
                                random_state=42
                                )

    Bagging.fit(X_train, Y_train)

    Y_pred_Bagging = Bagging.predict(X_test)

    Accuracy_Bagging = accuracy_score(Y_test, Y_pred_Bagging)
    Precision_Bagging = precision_score(Y_test, Y_pred_Bagging, zero_division=0)
    Recall_Bagging = recall_score(Y_test, Y_pred_Bagging, zero_division=0)
    F1_Bagging = f1_score(Y_test, Y_pred_Bagging, zero_division=0)

    print("Accuracy : ", Accuracy_Bagging)
    print("Precision : ", Precision_Bagging)
    print("Recall : ", Recall_Bagging)
    print("F1 Score : ", F1_Bagging)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred_Bagging))

    # Step 7 : Random Forest

    print(Border)
    print("Step 7 : Train Random Forest")
    print(Border)

    RandomForest = RandomForestClassifier(
                                            n_estimators=100,
                                            random_state=42
                                            )

    RandomForest.fit(X_train, Y_train)

    Y_pred_RF = RandomForest.predict(X_test)

    Accuracy_RF = accuracy_score(Y_test, Y_pred_RF)
    Precision_RF = precision_score(Y_test, Y_pred_RF, zero_division=0)
    Recall_RF = recall_score(Y_test, Y_pred_RF, zero_division=0)
    F1_RF = f1_score(Y_test, Y_pred_RF, zero_division=0)

    print("Accuracy : ", Accuracy_RF)
    print("Precision : ", Precision_RF)
    print("Recall : ", Recall_RF)
    print("F1 Score : ", F1_RF)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred_RF))

    # Step 8 : AdaBoost

    print(Border)
    print("Step 8 : Train AdaBoost Classifier")
    print(Border)

    AdaBoost = AdaBoostClassifier(
                                    n_estimators=50,
                                    random_state=42
                                    )

    AdaBoost.fit(X_train, Y_train)

    Y_pred_Ada = AdaBoost.predict(X_test)

    Accuracy_Ada = accuracy_score(Y_test, Y_pred_Ada)
    Precision_Ada = precision_score(Y_test, Y_pred_Ada, zero_division=0)
    Recall_Ada = recall_score(Y_test, Y_pred_Ada, zero_division=0)
    F1_Ada = f1_score(Y_test, Y_pred_Ada, zero_division=0)

    print("Accuracy : ", Accuracy_Ada)
    print("Precision : ", Precision_Ada)
    print("Recall : ", Recall_Ada)
    print("F1 Score : ", F1_Ada)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred_Ada))

    # Step 9 : Voting Classifier

    print(Border)
    print("Step 9 : Train Voting Classifier")
    print(Border)

    Voting = VotingClassifier(
                                estimators=[
                                    ("DecisionTree", DecisionTreeClassifier(random_state=42)),
                                    ("RandomForest", RandomForestClassifier(n_estimators=100, random_state=42)),
                                    ("AdaBoost", AdaBoostClassifier(n_estimators=50, random_state=42))
                                ],
                                voting="soft"
                                )

    Voting.fit(X_train, Y_train)

    Y_pred_Voting = Voting.predict(X_test)

    Accuracy_Voting = accuracy_score(Y_test, Y_pred_Voting)
    Precision_Voting = precision_score(Y_test, Y_pred_Voting, zero_division=0)
    Recall_Voting = recall_score(Y_test, Y_pred_Voting, zero_division=0)
    F1_Voting = f1_score(Y_test, Y_pred_Voting, zero_division=0)

    print("Accuracy : ", Accuracy_Voting)
    print("Precision : ", Precision_Voting)
    print("Recall : ", Recall_Voting)
    print("F1 Score : ", F1_Voting)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred_Voting))

    # Step 10 : Final Comparison

    print(Border)
    print("Step 10 : Final Comparison")
    print(Border)

    print("Algorithm\t\tAccuracy\tPrecision\tRecall\t\tF1")

    print("Decision Tree\t\t", Accuracy_DT,
          "\t", Precision_DT,
          "\t", Recall_DT,
          "\t", F1_DT)

    print("Bagging\t\t\t", Accuracy_Bagging,
          "\t", Precision_Bagging,
          "\t", Recall_Bagging,
          "\t", F1_Bagging)

    print("Random Forest\t\t", Accuracy_RF,
          "\t", Precision_RF,
          "\t", Recall_RF,
          "\t", F1_RF)

    print("AdaBoost\t\t", Accuracy_Ada,
          "\t", Precision_Ada,
          "\t", Recall_Ada,
          "\t", F1_Ada)

    print("Voting\t\t\t", Accuracy_Voting,
          "\t", Precision_Voting,
          "\t", Recall_Voting,
          "\t", F1_Voting)

    print(Border)


def main():

    MarvellousFraudDetection("Fraudulent_Transaction_Detection.csv")


if __name__ == "__main__":
    main()