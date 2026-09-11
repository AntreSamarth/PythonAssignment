"""
======================================================================
 Program     : Loan_Default.py
 Topic       : Deep Learning - Loan Default Prediction
 Description : Predicts the default risk of a loan applicant using
               MLPClassifier.
 Language    : Python
 Dataset     : Loan_Default.csv
======================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


def LoanDefault(DataPath):

    print("------------------------------------------------------------------")
    print("--------------------- 1) Load Dataset -----------------------------")
    print("------------------------------------------------------------------")

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully")


    print("------------------------------------------------------------------")
    print("-------------------- 2) Exploratory Analysis ---------------------")
    print("------------------------------------------------------------------")

    print("Shape of Dataset : ",df.shape)

    print("Columns : ")
    print(df.columns)

    print("First 5 Records : ")
    print(df.head())

    print("Dataset Information : ")
    print(df.info())


    print("------------------------------------------------------------------")
    print("---------------------- 3) Missing Values -------------------------")
    print("------------------------------------------------------------------")

    print(df.isnull().sum())


    print("------------------------------------------------------------------")
    print("---------------------- 4) Class Balance --------------------------")
    print("------------------------------------------------------------------")

    print("Default Class Distribution : ")
    print(df["Default"].value_counts())

    print("Percentage Distribution : ")
    print(df["Default"].value_counts(normalize=True) * 100)


    print("------------------------------------------------------------------")
    print("-------------------- 5) Encode Categorical -----------------------")
    print("------------------------------------------------------------------")

    Encoder1 = LabelEncoder()
    Encoder2 = LabelEncoder()

    df["PreviousDefault"] = Encoder1.fit_transform(
        df["PreviousDefault"]
    )

    df["HomeOwnership"] = Encoder2.fit_transform(
        df["HomeOwnership"]
    )

    print("Categorical features encoded successfully")

    print(df.head())


    print("------------------------------------------------------------------")
    print("---------------------- 6) Separate X and Y -----------------------")
    print("------------------------------------------------------------------")

    X = df.drop("Default",axis=1)
    Y = df["Default"]

    print("Independent Variables : ")
    print(X.head())

    print("Dependent Variable : ")
    print(Y.head())


    print("------------------------------------------------------------------")
    print("-------------------- 7) Train Test Split -------------------------")
    print("------------------------------------------------------------------")

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Training Data : ",X_train.shape)
    print("Testing Data : ",X_test.shape)


    print("------------------------------------------------------------------")
    print("---------------- 8) Stratified Splitting -------------------------")
    print("------------------------------------------------------------------")

    print("Stratified splitting maintains the same class")
    print("distribution in both training and testing data.")
    print("It is useful because the Default classes are imbalanced.")


    print("------------------------------------------------------------------")
    print("---------------------- 9) Feature Scaling -------------------------")
    print("------------------------------------------------------------------")

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.transform(X_test)

    print("Feature scaling completed")


    print("------------------------------------------------------------------")
    print("---------------------- 10) Create MLP -----------------------------")
    print("------------------------------------------------------------------")

    Model = MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    print("MLP Classifier created")
    print("Hidden Layers : ",(32,16))
    print("Activation : ","relu")
    print("Solver : ","adam")
    print("Maximum Iterations : ",1000)


    print("------------------------------------------------------------------")
    print("----------------------- 11) Train Model ---------------------------")
    print("------------------------------------------------------------------")

    Model.fit(X_train,Y_train)

    print("Model training completed")


    print("------------------------------------------------------------------")
    print("------------------------ 12) Accuracy -----------------------------")
    print("------------------------------------------------------------------")

    Y_Predicted = Model.predict(X_test)

    Accuracy = accuracy_score(Y_test,Y_Predicted)

    print("Testing Accuracy : ",Accuracy)


    print("------------------------------------------------------------------")
    print("--------------------- 13) Confusion Matrix ------------------------")
    print("------------------------------------------------------------------")

    Matrix = confusion_matrix(Y_test,Y_Predicted)

    print(Matrix)


    print("------------------------------------------------------------------")
    print("-------------------- 14) Classification Report --------------------")
    print("------------------------------------------------------------------")

    Report = classification_report(Y_test,Y_Predicted)

    print(Report)


    print("------------------------------------------------------------------")
    print("---------------------- 15) Evaluation Metrics ---------------------")
    print("------------------------------------------------------------------")

    Precision = precision_score(Y_test,Y_Predicted)
    Recall = recall_score(Y_test,Y_Predicted)
    F1 = f1_score(Y_test,Y_Predicted)

    print("Precision : ",Precision)
    print("Recall : ",Recall)
    print("F1 Score : ",F1)


    print("------------------------------------------------------------------")
    print("------------------------- 16) Training Loss -----------------------")
    print("------------------------------------------------------------------")

    print("Number of Iterations : ",Model.n_iter_)
    print("Final Training Loss : ",Model.loss_)


    plt.plot(Model.loss_curve_)

    plt.title("MLP Training Loss Curve")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")

    plt.show()


    print("------------------------------------------------------------------")
    print("-------------------- 17) Test New Applicant ----------------------")
    print("------------------------------------------------------------------")


    def PredictDefault(ApplicantData):

        Applicant = pd.DataFrame(
            [ApplicantData],
            columns=[
                "Age",
                "Income",
                "LoanAmount",
                "CreditScore",
                "EmploymentYears",
                "ExistingLoans",
                "MonthlyDebt",
                "LoanTerm",
                "PreviousDefault",
                "HomeOwnership"
            ]
        )

        Applicant["PreviousDefault"] = Encoder1.transform(
            Applicant["PreviousDefault"]
        )

        Applicant["HomeOwnership"] = Encoder2.transform(
            Applicant["HomeOwnership"]
        )

        Applicant = Scaler.transform(Applicant)

        Prediction = Model.predict(Applicant)

        if Prediction[0] == 0:
            print("Prediction : Low default risk")
        else:
            print("Prediction : High default risk")


    Applicant1 = [
        35,
        600000,
        300000,
        720,
        8,
        2,
        25000,
        60,
        "No",
        "Own"
    ]

    PredictDefault(Applicant1)


    print("------------------------------------------------------------------")
    print("------------------- 18) Hyperparameter Experiment -----------------")
    print("------------------------------------------------------------------")


    print("==================================================================")
    print("Experiment 1 : Activation Function")
    print("==================================================================")


    Activations = [
        "identity",
        "logistic",
        "tanh",
        "relu"
    ]

    for Activation in Activations:

        ExperimentModel = MLPClassifier(
            hidden_layer_sizes=(32,16),
            activation=Activation,
            solver="adam",
            max_iter=1000,
            random_state=42
        )

        ExperimentModel.fit(X_train,Y_train)

        ExperimentPrediction = ExperimentModel.predict(X_test)

        ExperimentAccuracy = accuracy_score(
            Y_test,
            ExperimentPrediction
        )

        print("Activation : ",Activation)
        print("Accuracy : ",ExperimentAccuracy)
        print()


    print("==================================================================")
    print("Experiment 2 : Hidden Layers")
    print("==================================================================")


    HiddenLayers = [
        (10,),
        (20,10),
        (50,25),
        (100,50,25)
    ]

    for HiddenLayer in HiddenLayers:

        ExperimentModel = MLPClassifier(
            hidden_layer_sizes=HiddenLayer,
            activation="relu",
            solver="adam",
            max_iter=1000,
            random_state=42
        )

        ExperimentModel.fit(X_train,Y_train)

        ExperimentPrediction = ExperimentModel.predict(X_test)

        ExperimentAccuracy = accuracy_score(
            Y_test,
            ExperimentPrediction
        )

        print("Hidden Layers : ",HiddenLayer)
        print("Accuracy : ",ExperimentAccuracy)
        print()


    print("==================================================================")
    print("Experiment 3 : Learning Rate")
    print("==================================================================")


    LearningRates = [
        0.001,
        0.01,
        0.1
    ]

    for LearningRate in LearningRates:

        ExperimentModel = MLPClassifier(
            hidden_layer_sizes=(32,16),
            activation="relu",
            solver="adam",
            learning_rate_init=LearningRate,
            max_iter=1000,
            random_state=42
        )

        ExperimentModel.fit(X_train,Y_train)

        ExperimentPrediction = ExperimentModel.predict(X_test)

        ExperimentAccuracy = accuracy_score(
            Y_test,
            ExperimentPrediction
        )

        print("Learning Rate : ",LearningRate)
        print("Accuracy : ",ExperimentAccuracy)
        print()


def main():

    Border = "-" * 40

    print(Border)
    print("Loan Default Prediction System")
    print(Border)

    LoanDefault("Loan_Default.csv")


if __name__ == "__main__":
    main()