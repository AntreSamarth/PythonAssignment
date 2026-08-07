import pandas as pd

Data = pd.read_csv("student_performance_ml.csv")

PassStudents = Data[Data["FinalResult"] == 1]
FailStudents = Data[Data["FinalResult"] == 0]

PassStudy = PassStudents["StudyHours"].mean()
FailStudy = FailStudents["StudyHours"].mean()

PassAttendance = PassStudents["Attendance"].mean()
FailAttendance = FailStudents["Attendance"].mean()

print("Average Study Hours of Passed Students :", PassStudy)
print("Average Study Hours of Failed Students :", FailStudy)

print()

print("Average Attendance of Passed Students :", PassAttendance)
print("Average Attendance of Failed Students :", FailAttendance)