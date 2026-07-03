# Write a program which accepts marks and displays grade.
# Condition Example:

# ≥75 → Distinction
# ≥60 → First Class
# ≥50 → Second Class
# <50 → Fail

def main():
    Marks = int(input("Enter the Marks : "))

    if Marks >= 75:
        print("In Distinction")
    elif Marks >= 60:
        print("In First class")
    elif Marks >= 50:
        print("In second class")  
    else:
        print("Fail")      

if __name__=="__main__":
    main()