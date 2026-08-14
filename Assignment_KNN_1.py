import math

def CalculateDistance(P1, P2):
    Distance = math.sqrt(
        (P1['X'] - P2['X']) ** 2 +
        (P1['Y'] - P2['Y']) ** 2
    )

    return Distance


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

    # Calculate distance from all points

    for Point in Data:
        Point['Distance'] = CalculateDistance(Point, NewPoint)

    # Sort according to distance

    SortedData = sorted(
        Data,
        key=lambda Point: Point['Distance']
    )

    # Select K = 3 nearest neighbours

    K = 3
    Nearest = SortedData[:K]

    print(Border)
    print("Nearest Neighbours:")
    print(Border)

    for Point in Nearest:
        print(
            Point['Point'],
            "- Distance:",
            round(Point['Distance'], 2),
            "- Label:",
            Point['Label']
        )

    # Majority Voting

    Votes = {}

    for Point in Nearest:
        Label = Point['Label']

        if Label in Votes:
            Votes[Label] = Votes[Label] + 1
        else:
            Votes[Label] = 1

    # Find maximum votes

    Prediction = max(Votes, key=Votes.get)

    print(Border)
    print("Voting Result:")
    print(Border)

    for Label in Votes:
        print(Label, ":", Votes[Label])

    print(Border)
    print("Predicted Class:", Prediction)
    print(Border)


def main():
    MarvellousKNN()


if __name__ == "__main__":
    main()