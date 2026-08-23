import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

#-----------------------------------------------------------------------
# Step 1 : Load the dataset
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 1 : Load the dataset")
print("-" * 60)

df = pd.read_csv("breast_cancer.csv")

print("Shape of dataset : ", df.shape)

print()
print("First few records : ")
print(df.head())

#-----------------------------------------------------------------------
# Step 2 : Data Preprocessing
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 2 : Data Preprocessing")
print("-" * 60)

print("Missing values : ")
print(df.isnull().sum().sum())

# Separate features and target

X = df.drop("target", axis=1)
Y = df["target"]

print()
print("Shape of X : ", X.shape)
print("Shape of Y : ", Y.shape)

#-----------------------------------------------------------------------
# Step 3 : Exploratory Data Analysis
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 3 : Exploratory Data Analysis")
print("-" * 60)

print("Statistical summary : ")
print(X.describe())

print()
print("Target distribution : ")
print(Y.value_counts())

#-----------------------------------------------------------------------
# Step 4 : Visualization of feature correlations
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 4 : Feature Correlation Visualization")
print("-" * 60)

plt.figure(figsize=(12, 8))

plt.imshow(X.corr(), cmap="coolwarm", interpolation="nearest")

plt.colorbar()

plt.title("Feature Correlation Matrix")

plt.xticks(
    range(len(X.columns)),
    X.columns,
    rotation=90
)

plt.yticks(
    range(len(X.columns)),
    X.columns
)

plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------
# Step 5 : Split dataset for training and testing
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 5 : Split Dataset")
print("-" * 60)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("X_train shape : ", X_train.shape)
print("X_test shape  : ", X_test.shape)

print("Y_train shape : ", Y_train.shape)
print("Y_test shape  : ", Y_test.shape)

#-----------------------------------------------------------------------
# Step 6 : Feature Scaling
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 6 : Feature Scaling")
print("-" * 60)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature scaling completed successfully.")

#-----------------------------------------------------------------------
# Step 7 : Create Machine Learning Model
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 7 : Create Decision Tree Model")
print("-" * 60)

model = DecisionTreeClassifier(
    random_state=42
)

#-----------------------------------------------------------------------
# Step 8 : Train the model
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 8 : Train the Model")
print("-" * 60)

model = model.fit(X_train, Y_train)

print("Model training completed successfully.")

#-----------------------------------------------------------------------
# Step 9 : Prediction
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 9 : Prediction")
print("-" * 60)

Y_pred = model.predict(X_test)

print("Predicted values : ")
print(Y_pred)

#-----------------------------------------------------------------------
# Step 10 : Model Evaluation
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 10 : Model Evaluation")
print("-" * 60)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy : ", accuracy * 100)

print()
print("Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_pred))

print()
print("Classification Report : ")
print(classification_report(Y_test, Y_pred))

#-----------------------------------------------------------------------
# Step 11 : Final Conclusion
#-----------------------------------------------------------------------

print("-" * 60)
print("Step 11 : Final Conclusion")
print("-" * 60)

print("The Decision Tree model was successfully trained")
print("to classify breast cancer tumors.")

print("Target 0 : Malignant")
print("Target 1 : Benign")

print("Model Accuracy : ", accuracy * 100)