def main():

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    # Regression equation
    m = 0.4
    c = 2.4

    # Predict all Y values
    Y_pred = []

    for x in X:
        predicted = (m * x) + c
        Y_pred.append(predicted)

    print("Actual Y values    :", Y)
    print("Predicted Y values :", Y_pred)

    # Calculate Mean Squared Error
    total_error = 0

    for i in range(len(Y)):
        error = Y[i] - Y_pred[i]
        total_error = total_error + (error ** 2)

    MSE = total_error / len(Y)

    print("Mean Squared Error :", MSE)

    # Calculate R2 Score
    mean_Y = sum(Y) / len(Y)

    total_sum_squares = 0
    residual_sum_squares = 0

    for i in range(len(Y)):
        total_sum_squares = total_sum_squares + ((Y[i] - mean_Y) ** 2)
        residual_sum_squares = residual_sum_squares + ((Y[i] - Y_pred[i]) ** 2)

    R2 = 1 - (residual_sum_squares / total_sum_squares)

    print("R2 Score :", R2)


if __name__ == "__main__":
    main()