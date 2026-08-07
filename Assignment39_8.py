import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

Data = pd.read_csv("student_performance_ml.csv")

X = Data[["StudyHours",
          "Attendance",
          "PreviousScore",
          "AssignmentsCompleted",
          "SleepHours"]]

Y = Data["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

Model = DecisionTreeClassifier(random_state=42)

Model.fit(X_train, Y_train)

Prediction = Model.predict(X_test)

Accuracy = accuracy_score(Y_test, Prediction)

CM = confusion_matrix(Y_test, Prediction)

print("--------------------------------------")
print("Decision Tree Classifier")
print("--------------------------------------")

print("Accuracy :", Accuracy * 100, "%")

print("\nConfusion Matrix")
print(CM)

print("\nPrediction Results")

for Actual, Predicted in zip(Y_test.values, Prediction):

    print("Actual :", Actual, " Predicted :", Predicted)

print("--------------------------------------")

NewStudent = pd.DataFrame(
    [[6, 85, 78, 8, 7]],
    columns=["StudyHours",
             "Attendance",
             "PreviousScore",
             "AssignmentsCompleted",
             "SleepHours"]
)

Result = Model.predict(NewStudent)

if(Result[0] == 1):
    print("New Student Prediction : Pass")
else:
    print("New Student Prediction : Fail")

print("--------------------------------------")