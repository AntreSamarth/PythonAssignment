import pandas as pd

Data = pd.read_csv("student_performance_ml.csv")

Result = Data["FinalResult"].value_counts()

Pass = Result[1]
Fail = Result[0]

TotalStudents = len(Data)

PassPercentage = (Pass / TotalStudents) * 100
FailPercentage = (Fail / TotalStudents) * 100

print("Passed Students :", Pass)
print("Failed Students :", Fail)

print("Pass Percentage :", PassPercentage)
print("Fail Percentage :", FailPercentage)

if abs(PassPercentage - FailPercentage) <= 10:
    print("Dataset is Balanced")
else:
    print("Dataset is Imbalanced")