import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("student_performance_ml.csv")

PassStudents = Data[Data["FinalResult"] == 1]

FailStudents = Data[Data["FinalResult"] == 0]

PassAverage = PassStudents["AssignmentsCompleted"].mean()

FailAverage = FailStudents["AssignmentsCompleted"].mean()

plt.bar(["Pass","Fail"], [PassAverage, FailAverage])

plt.title("Average Assignments Completed")
plt.xlabel("Final Result")
plt.ylabel("Average Assignments")

plt.show()