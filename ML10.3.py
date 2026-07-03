# Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def main():
    No = int(input("Enter the number : "))
    
    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i

    print("Factorial is : ",Fact)

if __name__== "__main__":
    main()

