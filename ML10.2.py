# Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def main():
    No1 = int(input("Enter the number : "))
    Sum = 0

    for i in range(1, No1+1):
        Sum = Sum + i

    print("Sum of first",No1,"Natural Numbers is : ",Sum)    

if __name__== "__main__":
    main()

