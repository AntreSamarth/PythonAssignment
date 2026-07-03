# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def main():
    No = int(input("Enter the Number : "))

    Sum = 0

    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        print("It is perfect number")
    else:
        print("It is Not perfect number")            

if __name__=="__main__":
    main()