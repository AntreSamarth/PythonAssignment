import pandas as pd
import matplotlib.pyplot as plt

def main():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    amit = df[df['Name'] == 'Amit']

    subjects = ['Math', 'Science', 'English']

    marks = [
        amit['Math'].values[0],
        amit['Science'].values[0],
        amit['English'].values[0]
    ]

    plt.plot(subjects, marks, marker='o')

    plt.title("Amit's Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.show()


if __name__ == "__main__":
    main()