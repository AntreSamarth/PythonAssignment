import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    scaler = MinMaxScaler()

    df['Math'] = scaler.fit_transform(df[['Math']])

    print(df)


if __name__ == "__main__":
    main()