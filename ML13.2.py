# Write a program which accepts radius of circle and prints area of circle.
def main():
    No = float(input("Enter the radius of circle : "))

    PI = 3.14
    Area = PI * No * No

    print("Area of circle is : ",Area)

if __name__=="__main__":
    main()