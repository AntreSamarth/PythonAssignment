"""
======================================================================
 Program     : Employee_Attrition.py
 Topic       : Deep Learning - Employee Attrition Prediction
 Description : Predicts whether an employee is likely to stay or leave
               using MLPClassifier.
 Language    : Python
 Dataset     : Employee_Attrition.csv
======================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


def EmployeeAttrition(DataPath):

    print("------------------------------------------------------------------")
    print("--------------------- 1) Load the Dataset ------------------------")
    print("------------------------------------------------------------------")

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully")


    print("------------------------------------------------------------------")
    print("------------------- 2) Dataset Information ----------------------")
    print("------------------------------------------------------------------")

    print("Shape of Dataset : ",df.shape)
    print("Columns : ",df.columns)
    print("First 5 Records : ")
    print(df.head())


    print("------------------------------------------------------------------")
    print("------------------- 3) Missing Values ---------------------------")
    print("------------------------------------------------------------------")

    print(df.isnull().sum())


    print("------------------------------------------------------------------")
    print("---------------- 4) Numerical and Categorical -------------------")
    print("------------------------------------------------------------------")

    NumericalFeatures = df.select_dtypes(include=["int64","float64"]).columns
    CategoricalFeatures = df.select_dtypes(include=["object"]).columns

    print("Numerical Features : ")
    print(NumericalFeatures)

    print("Categorical Features : ")
    print(CategoricalFeatures)


    print("------------------------------------------------------------------")
    print("------------------- 5) Encode OverTime --------------------------")
    print("------------------------------------------------------------------")

    df["OverTime"] = df["OverTime"].map({"No":0,"Yes":1})

    print(df["OverTime"].head())


    print("------------------------------------------------------------------")
    print("------------------ 6) Encode Attrition --------------------------")
    print("------------------------------------------------------------------")

    df["Attrition"] = df["Attrition"].map({"No":0,"Yes":1})

    print(df["Attrition"].head())


    print("------------------------------------------------------------------")
    print("------------------ 7) Separate X and Y ---------------------------")
    print("------------------------------------------------------------------")

    X = df.drop("Attrition",axis=1)
    Y = df["Attrition"]

    print("Independent Variables : ")
    print(X.head())

    print("Dependent Variable : ")
    print(Y.head())


    print("------------------------------------------------------------------")
    print("------------------ 8) Train Test Split ---------------------------")
    print("------------------------------------------------------------------")

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Training Data : ",X_train.shape)
    print("Testing Data : ",X_test.shape)


    print("------------------------------------------------------------------")
    print("--------------------- 9) Feature Scaling -------------------------")
    print("------------------------------------------------------------------")

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.transform(X_test)

    print("Feature scaling completed")


    print("------------------------------------------------------------------")
    print("-------------------- 10) Create MLP ------------------------------")
    print("------------------------------------------------------------------")

    Model = MLPClassifier(
        hidden_layer_sizes=(64,32),
        max_iter=500,
        random_state=42
    )

    print("MLP Classifier created")
    print("Hidden Layers : 2")


    print("------------------------------------------------------------------")
    print("---------------------- 11) Train Model ----------------------------")
    print("------------------------------------------------------------------")

    Model.fit(X_train,Y_train)

    print("Model training completed")


    print("------------------------------------------------------------------")
    print("------------------- 12) Number of Iterations ---------------------")
    print("------------------------------------------------------------------")

    print("Number of Iterations : ",Model.n_iter_)


    print("------------------------------------------------------------------")
    print("-------------------- 13) Training Accuracy -----------------------")
    print("------------------------------------------------------------------")

    Y_train_Predicted = Model.predict(X_train)

    TrainAccuracy = accuracy_score(Y_train,Y_train_Predicted)

    print("Training Accuracy : ",TrainAccuracy)


    print("------------------------------------------------------------------")
    print("--------------------- 14) Testing Accuracy -----------------------")
    print("------------------------------------------------------------------")

    Y_test_Predicted = Model.predict(X_test)

    TestAccuracy = accuracy_score(Y_test,Y_test_Predicted)

    print("Testing Accuracy : ",TestAccuracy)


    print("------------------------------------------------------------------")
    print("--------------------- 15) Confusion Matrix -----------------------")
    print("------------------------------------------------------------------")

    Matrix = confusion_matrix(Y_test,Y_test_Predicted)

    print(Matrix)


    print("------------------------------------------------------------------")
    print("----------------------- 16) Loss Curve ----------------------------")
    print("------------------------------------------------------------------")

    plt.plot(Model.loss_curve_)

    plt.title("MLP Training Loss Curve")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")

    plt.show()


    print("------------------------------------------------------------------")
    print("------------------- 17) Prediction Function ----------------------")
    print("------------------------------------------------------------------")


    def PredictAttrition(employee_data):

        Employee = pd.DataFrame(
            [employee_data],
            columns=[
                "Age",
                "MonthlyIncome",
                "YearsAtCompany",
                "TotalWorkingYears",
                "DistanceFromHome",
                "JobSatisfaction",
                "WorkLifeBalance",
                "OverTime",
                "NumCompaniesWorked",
                "TrainingTimesLastYear"
            ]
        )

        Employee["OverTime"] = Employee["OverTime"].map({
            "No":0,
            "Yes":1
        })

        Employee = Scaler.transform(Employee)

        Prediction = Model.predict(Employee)

        if Prediction[0] == 0:
            print("Prediction : Employee is likely to stay")
        else:
            print("Prediction : Employee is likely to leave")


    print("------------------------------------------------------------------")
    print("-------------------- 18) Test New Employee -----------------------")
    print("------------------------------------------------------------------")

    Employee1 = [
        30,
        50000,
        5,
        8,
        10,
        3,
        3,
        "No",
        2,
        3
    ]

    PredictAttrition(Employee1)


    print("------------------------------------------------------------------")
    print("---------------- 19) Overfitting / Underfitting -----------------")
    print("------------------------------------------------------------------")

    print("Training Accuracy : ",TrainAccuracy)
    print("Testing Accuracy : ",TestAccuracy)

    if TrainAccuracy - TestAccuracy > 0.10:
        print("Model may be suffering from Overfitting")
    elif TrainAccuracy < 0.70 and TestAccuracy < 0.70:
        print("Model may be suffering from Underfitting")
    else:
        print("Model does not show significant Overfitting or Underfitting")


def main():

    Border = "-" * 40

    print(Border)
    print("Employee Attrition Prediction System")
    print(Border)

    EmployeeAttrition("Employee_Attrition.csv")


if __name__ == "__main__":
    main()