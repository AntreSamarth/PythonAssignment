import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Data = pd.read_csv("student_performance_ml.csv")

X = Data[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = Data["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

Model = DecisionTreeClassifier(random_state=42)

Model.fit(X_train,Y_train)

Students = pd.DataFrame([
[6,85,78,8,7],
[3,60,55,4,6],
[7,95,88,10,8],
[5,75,70,6,7],
[2,50,40,3,5]
],columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"])

Prediction = Model.predict(Students)

print(Students)
print()
print("Prediction :",Prediction)