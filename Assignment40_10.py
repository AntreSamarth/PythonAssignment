import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Data = pd.read_csv("student_performance_ml.csv")

X = Data[["StudyHours",
          "Attendance",
          "PreviousScore",
          "AssignmentsCompleted",
          "SleepHours"]]

Y = Data["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

Model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

Model.fit(X_train,Y_train)

TrainPrediction = Model.predict(X_train)
TestPrediction = Model.predict(X_test)

TrainAccuracy = accuracy_score(Y_train,TrainPrediction)
TestAccuracy = accuracy_score(Y_test,TestPrediction)

print("Training Accuracy :",TrainAccuracy*100,"%")
print("Testing Accuracy :",TestAccuracy*100,"%")