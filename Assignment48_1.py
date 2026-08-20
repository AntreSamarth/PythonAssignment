def main():

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    # Mean of X
    mean_X = sum(X) / len(X)

    # Mean of Y
    mean_Y = sum(Y) / len(Y)

    # Calculate slope
    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X) ** 2)

    m = numerator / denominator

    # Calculate intercept
    c = mean_Y - (m * mean_X)

    # Regression equation
    print("Mean of X =", mean_X)
    print("Mean of Y =", mean_Y)

    print("Slope (m) =", m)
    print("Intercept (c) =", c)

    print("Regression Equation:")
    print("Y = ", m, "X +", c)

    # Predict Y for X = 6
    x = 6
    predicted_Y = (m * x) + c

    print("Predicted Y for X = 6 :", predicted_Y)


if __name__ == "__main__":
    main()