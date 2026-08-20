import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


def main():

    # Dataset
    X = np.array([[1], [2], [3], [4], [5]])

    Y = np.array([20000, 25000, 30000, 35000, 40000])

    # Train Linear Regression model
    model = LinearRegression()

    model = model.fit(X, Y)

    # Predict salary for 6 years experience
    result = model.predict([[6]])

    print("Coefficient :", model.coef_[0])
    print("Intercept :", model.intercept_)

    print("Predicted Salary for 6 Years Experience :", result[0])

    # Plot data points
    plt.scatter(X, Y, label="Data Points")

    # Regression line
    Y_pred = model.predict(X)

    plt.plot(X, Y_pred, label="Regression Line")

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()