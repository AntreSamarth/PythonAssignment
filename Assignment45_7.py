import pandas as pd

def main():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df['Total'] = df['Math'] + df['Science'] + df['English']

    df['Status'] = df['Total'].apply(
        lambda x: 'Pass' if x >= 250 else 'Fail'
    )

    df.to_csv('Assignment45_FinalData.csv', index=False)

    print("DataFrame exported successfully.")
    print("File name: Assignment45_FinalData.csv")


if __name__ == "__main__":
    main()