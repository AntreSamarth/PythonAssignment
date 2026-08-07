import pandas as pd

Data = pd.read_csv("student_performance_ml.csv")

TotalStudents = len(Data)

PassedStudents = len(Data[Data["FinalResult"] == 1])

FailedStudents = len(Data[Data["FinalResult"] == 0])

print("Total Students :", TotalStudents)
print("Passed Students :", PassedStudents)
print("Failed Students :", FailedStudents)