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

    plt.boxplot(df['English'])

    plt.title("English Marks Distribution")
    plt.ylabel("English Marks")

    plt.show()


if __name__ == "__main__":
    main()