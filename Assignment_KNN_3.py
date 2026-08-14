import math

def CalculateDistance(P1, P2):
    return math.sqrt((P1['StudyHours'] - P2['StudyHours']) ** 2 +
                     (P1['Attendance'] - P2['Attendance']) ** 2)


def MarvellousKNNClassifier():
    Data = [
        {'StudyHours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'StudyHours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'StudyHours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'StudyHours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    StudyHours = float(input("Enter Study Hours: "))
    Attendance = float(input("Enter Attendance: "))

    NewPoint = {
        'StudyHours': StudyHours,
        'Attendance': Attendance
    }

    # Calculate distance
    for Student in Data:
        Student['Distance'] = CalculateDistance(Student, NewPoint)

    # Sort according to distance
    SortedData = sorted(Data, key=lambda Student: Student['Distance'])

    # Select K nearest neighbours
    K = 3
    Nearest = SortedData[:K]

    # Voting
    Votes = {}

    for Student in Nearest:
        Result = Student['Result']
        Votes[Result] = Votes.get(Result, 0) + 1

    # Find majority class
    Prediction = max(Votes, key=Votes.get)

    print("\nNearest Neighbours:")

    for Student in Nearest:
        print(Student['Result'], "- Distance:",
              round(Student['Distance'], 2))

    print("\nPredicted Result:", Prediction)


def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()