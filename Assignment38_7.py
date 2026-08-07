import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("student_performance_ml.csv")

plt.scatter(Data["StudyHours"], Data["PreviousScore"])

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.show()