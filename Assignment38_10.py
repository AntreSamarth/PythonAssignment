import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("student_performance_ml.csv")

PassStudents = Data[Data["FinalResult"] == 1]

FailStudents = Data[Data["FinalResult"] == 0]

PassSleep = PassStudents["SleepHours"].mean()

FailSleep = FailStudents["SleepHours"].mean()

plt.bar(["Pass", "Fail"], [PassSleep, FailSleep])

plt.title("Average Sleep Hours")
plt.xlabel("Final Result")
plt.ylabel("Average Sleep Hours")

plt.show()