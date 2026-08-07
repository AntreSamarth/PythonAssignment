import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("student_performance_ml.csv")

plt.boxplot(Data["Attendance"])

plt.title("Box Plot of Attendance")
plt.ylabel("Attendance")

plt.show()