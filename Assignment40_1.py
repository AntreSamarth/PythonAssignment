import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

Importance = Model.feature_importances_

for Name, Value in zip(X.columns, Importance):
    print(Name, ":", Value)

MaxIndex = Importance.argmax()
MinIndex = Importance.argmin()

print("\nMost Important Feature :", X.columns[MaxIndex])
print("Least Important Feature :", X.columns[MinIndex])