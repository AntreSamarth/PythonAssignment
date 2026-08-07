import pandas as pd

Data = pd.read_csv("student_performance_ml.csv")

print("First 5 Records")
print(Data.head())

print("\nLast 5 Records")
print(Data.tail())

print("\nRows and Columns")
print(Data.shape)

print("\nColumn Names")
print(Data.columns)

print("\nData Types")
print(Data.dtypes)