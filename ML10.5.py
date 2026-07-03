# Write a program which accepts one number and prints all odd numbers till that number
# Input: 10
# Output: 1 3 5 7 9
def main():
    No = int(input("Enetr the number : "))

    for i in range(1,No+1):
        if(i % 2 != 0):
            print(i, end = " ")
    
if __name__== "__main__":
    main()

