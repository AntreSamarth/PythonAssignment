import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("student_performance_ml.csv")

plt.hist(Data["StudyHours"])

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()