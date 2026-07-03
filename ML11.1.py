# Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def main():
    No = int(input("Enter the Number : "))

    Count = 0

    for i in range(1, No + 1):
        if No % i == 0:
            Count = Count + 1

    if Count == 2:
        print("It is Prime Number")
    else:
        print("It is not prime number")                                                                                    

if __name__=="__main__":
    main()