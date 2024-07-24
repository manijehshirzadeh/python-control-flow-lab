# Exercise 1: Vowel or Consonant
def check_letter():
     letter = input("Enter a letter (a-z or A-Z): ").strip()
     if len(letter) != 1 or not letter.isalpha():
        print("Invalid entry. Please enter a single letter (a-z or A-Z).")
        return
     letter = letter.lower()
     vowels = 'aeiou'
     if letter in vowels:
          print(f"The letter {letter} is a vowel.")
     else:
       print(f"The letter {letter} is a consonant.")

check_letter()

