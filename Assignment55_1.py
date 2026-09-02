import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score

#--------------------------------------------------------
# Step 1 : Load the dataset
#--------------------------------------------------------

print("-" * 50)
print("Step 1 : Load the dataset")
print("-" * 50)

df = pd.read_csv("Customer_Loan_Approval (1).csv")

print(df.head())

#--------------------------------------------------------
# Step 2 : Check for missing values
#--------------------------------------------------------

print("-" * 50)
print("Step 2 : Check for missing values")
print("-" * 50)

print(df.isnull().sum())

#--------------------------------------------------------
# Step 3 : Separate input and output variables
#--------------------------------------------------------

print("-" * 50)
print("Step 3 : Separate input and output variables")
print("-" * 50)

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

print("Shape of X : ", X.shape)
print("Shape of Y : ", Y.shape)

#--------------------------------------------------------
# Step 4 : Split dataset into training and testing
#--------------------------------------------------------

print("-" * 50)
print("Step 4 : Split dataset")
print("-" * 50)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("X_train : ", X_train.shape)
print("X_test  : ", X_test.shape)

#--------------------------------------------------------
# Step 5 : Feature Scaling
#--------------------------------------------------------

print("-" * 50)
print("Step 5 : Feature Scaling")
print("-" * 50)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature scaling completed")

#--------------------------------------------------------
# Step 6 : Train Logistic Regression
#--------------------------------------------------------

print("-" * 50)
print("Step 6 : Train Logistic Regression")
print("-" * 50)

LogisticModel = LogisticRegression()

LogisticModel = LogisticModel.fit(X_train, Y_train)

LogisticPrediction = LogisticModel.predict(X_test)

LogisticAccuracy = accuracy_score(
    Y_test,
    LogisticPrediction
)

print("Logistic Regression Accuracy : ",
      LogisticAccuracy * 100)

#--------------------------------------------------------
# Step 7 : Train Decision Tree
#--------------------------------------------------------

print("-" * 50)
print("Step 7 : Train Decision Tree")
print("-" * 50)

DecisionTreeModel = DecisionTreeClassifier(
    random_state=42
)

DecisionTreeModel = DecisionTreeModel.fit(
    X_train,
    Y_train
)

DecisionTreePrediction = DecisionTreeModel.predict(X_test)

DecisionTreeAccuracy = accuracy_score(
    Y_test,
    DecisionTreePrediction
)

print("Decision Tree Accuracy : ",
      DecisionTreeAccuracy * 100)

#--------------------------------------------------------
# Step 8 : Train KNN
#--------------------------------------------------------

print("-" * 50)
print("Step 8 : Train KNN")
print("-" * 50)

KNNModel = KNeighborsClassifier(
    n_neighbors=3
)

KNNModel = KNNModel.fit(X_train, Y_train)

KNNPrediction = KNNModel.predict(X_test)

KNNAccuracy = accuracy_score(
    Y_test,
    KNNPrediction
)

print("KNN Accuracy : ",
      KNNAccuracy * 100)

#--------------------------------------------------------
# Step 9 : Create Hard Voting Classifier
#--------------------------------------------------------

print("-" * 50)
print("Step 9 : Create Hard Voting Classifier")
print("-" * 50)

HardVotingModel = VotingClassifier(
    estimators=[
        ("Logistic", LogisticModel),
        ("DecisionTree", DecisionTreeModel),
        ("KNN", KNNModel)
    ],
    voting="hard"
)

HardVotingModel = HardVotingModel.fit(
    X_train,
    Y_train
)

HardVotingPrediction = HardVotingModel.predict(X_test)

HardVotingAccuracy = accuracy_score(
    Y_test,
    HardVotingPrediction
)

print("Hard Voting Accuracy : ",
      HardVotingAccuracy * 100)

#--------------------------------------------------------
# Step 10 : Create Soft Voting Classifier
#--------------------------------------------------------

print("-" * 50)
print("Step 10 : Create Soft Voting Classifier")
print("-" * 50)

SoftVotingModel = VotingClassifier(
    estimators=[
        ("Logistic", LogisticModel),
        ("DecisionTree", DecisionTreeModel),
        ("KNN", KNNModel)
    ],
    voting="soft"
)

SoftVotingModel = SoftVotingModel.fit(
    X_train,
    Y_train
)

SoftVotingPrediction = SoftVotingModel.predict(X_test)

SoftVotingAccuracy = accuracy_score(
    Y_test,
    SoftVotingPrediction
)

print("Soft Voting Accuracy : ",
      SoftVotingAccuracy * 100)

#--------------------------------------------------------
# Step 11 : Compare all models
#--------------------------------------------------------

print("-" * 50)
print("Step 11 : Model Accuracy Comparison")
print("-" * 50)

print("Model                  Accuracy")

print("Logistic Regression : ",
      LogisticAccuracy * 100)

print("Decision Tree       : ",
      DecisionTreeAccuracy * 100)

print("KNN                 : ",
      KNNAccuracy * 100)

print("Hard Voting         : ",
      HardVotingAccuracy * 100)

print("Soft Voting         : ",
      SoftVotingAccuracy * 100)