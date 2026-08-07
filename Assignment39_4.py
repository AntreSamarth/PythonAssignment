import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

Prediction = Model.predict(X_test)

CM = confusion_matrix(Y_test, Prediction)

print("Confusion Matrix :")
print(CM)

Display = ConfusionMatrixDisplay(confusion_matrix=CM,
                                 display_labels=["Fail", "Pass"])

Display.plot()

plt.show()

TN = CM[0][0]
FP = CM[0][1]
FN = CM[1][0]
TP = CM[1][1]

print("True Positive :", TP)
print("True Negative :", TN)
print("False Positive :", FP)
print("False Negative :", FN)