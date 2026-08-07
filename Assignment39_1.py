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

Model = DecisionTreeClassifier()

Model.fit(X_train, Y_train)

print("Decision Tree Model Trained Successfully")