import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Data = pd.read_csv("student_performance_ml.csv")

X = Data[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = Data["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

Model = DecisionTreeClassifier(random_state=42)

Model.fit(X_train,Y_train)

Prediction = Model.predict(X_test)

Correct = 0

for Actual,Predicted in zip(Y_test,Prediction):
    if Actual == Predicted:
        Correct = Correct + 1

ManualAccuracy = (Correct/len(Y_test))*100

print("Manual Accuracy :",ManualAccuracy,"%")
print("Sklearn Accuracy :",accuracy_score(Y_test,Prediction)*100,"%")