import pandas as pd

Data = pd.read_csv("student_performance_ml.csv")

AverageStudyHours = Data["StudyHours"].mean()

AverageAttendance = Data["Attendance"].mean()

MaximumScore = Data["PreviousScore"].max()

MinimumSleep = Data["SleepHours"].min()

print("Average Study Hours :", AverageStudyHours)

print("Average Attendance :", AverageAttendance)

print("Maximum Previous Score :", MaximumScore)

print("Minimum Sleep Hours :", MinimumSleep)