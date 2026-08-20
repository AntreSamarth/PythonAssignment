import math
import numpy as np
from sklearn.preprocessing import StandardScaler


def EuclideanDistance(P1, P2):

    return math.sqrt(np.sum((P1 - P2) ** 2))


def main():

    P1 = np.array([25, 20000])
    P2 = np.array([35, 80000])

    # Distance before scaling
    distance_before = EuclideanDistance(P1, P2)

    print("Distance before scaling :", distance_before)

    # Apply feature scaling
    data = np.array([
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ])

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    scaled_P1 = scaled_data[0]
    scaled_P2 = scaled_data[2]

    # Distance after scaling
    distance_after = EuclideanDistance(scaled_P1, scaled_P2)

    print("Distance after scaling :", distance_after)


if __name__ == "__main__":
    main()