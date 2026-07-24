#count line in files 

def CountLines(filename):
    file = open(filename,"r")

    count = 0

    for line in file:
        count = count + 1

    file.close()

    return count

def main():
    name = input("Enter the file name : ")

    lines = CountLines(name)

    print("Total number of lines in",name, ":",lines)

if __name__=="__main__":
    main()