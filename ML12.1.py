# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def main():
    Char = (input("Enter character : "))

    if Char == "a" or Char == "e" or Char == "i" or Char == "o" or Char == "u" or Char == "A" or Char == "E" or Char == "I" or Char == "O" or Char == "U":
        print("It is Vowel")

    else:
        print("It is Consonant")    

if __name__=="__main__":
    main()