import math


def CalculateDistance(P1, P2):
    Distance = math.sqrt(
        (P1['X'] - P2['X']) ** 2 +
        (P1['Y'] - P2['Y']) ** 2
    )

    return Distance


def PredictClass(Data, NewPoint, K):

    for Point in Data:
        Point['Distance'] = CalculateDistance(Point, NewPoint)

    SortedData = sorted(
        Data,
        key=lambda Point: Point['Distance']
    )

    Nearest = SortedData[:K]

    Votes = {}

    for Point in Nearest:
        Label = Point['Label']

        if Label in Votes:
            Votes[Label] = Votes[Label] + 1
        else:
            Votes[Label] = 1

    Prediction = max(Votes, key=Votes.get)

    return Prediction


def MarvellousKNN():
    Border = "-" * 40

    Data = [
        {'Point': 'A', 'X': 1, 'Y': 2, 'Label': 'Red'},
        {'Point': 'B', 'X': 2, 'Y': 3, 'Label': 'Red'},
        {'Point': 'C', 'X': 3, 'Y': 1, 'Label': 'Blue'},
        {'Point': 'D', 'X': 5, 'Y': 6, 'Label': 'Blue'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    X = float(input("Enter X coordinate: "))
    Y = float(input("Enter Y coordinate: "))

    NewPoint = {'X': X, 'Y': Y}

    K_values = [1, 3, 5]

    print(Border)
    print("Prediction Results")
    print(Border)

    for K in K_values:

        if K > len(Data):
            print("K =", K, "is greater than dataset size")
            continue

        Prediction = PredictClass(Data, NewPoint, K)

        print("K =", K, "->", Prediction)

    print(Border)


def main():
    MarvellousKNN()


if __name__ == "__main__":
    main()