from sklearn.metrics import classification_report


def main():

    actual = [1, 1, 1, 1, 0, 0, 0, 0]

    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    result = classification_report(actual, predicted)

    print(result)


if __name__ == "__main__":
    main()