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

# Exercise 2: Old enough to vote?
def check_voting_eligibility():
     age = input("Please enter your age: ")
     if not age.isdigit():
         print ("Invalid input. Please enter a valid age as a number.")
     else:
        age = int(age)
     if age <0:
         print("Age cannot be negative. Please enter a valid age.")
     else:
        voting_age = 18 
     if age>= voting_age:
         print("You are eligible to vote!")      
     else:
         print("You are not yet eligible to vote.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Yearss
def calculate_dog_years():
     dog_age = input("Input a dog's age: ")
     if not dog_age.isdigit() or int(dog_age) < 0:
         print ("Invalid input. Please enter a valid age as a positive number.")
     else:
        dog_age = int(dog_age)
        
        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
             dog_years = 20 + (dog_age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")

calculate_dog_years()

# Exercise 4: Weather Advice
def weather_advice():
     cold_weather = input("Is it cold? (yes/no): ").strip().lower()
     rainy_weather = input("Is it raining? (yes/no): ").strip().lower()
        
     if cold_weather == "yes" and  rainy_weather == "yes" :
            print ("Wear a waterproof coat.")
     elif cold_weather == "yes" and rainy_weather == "no" :
            print ("Wear a warm coat.")
     elif cold_weather == "no" and rainy_weather == "yes" :
            print ("Carry an umbrella.")
     elif cold_weather == "no" and rainy_weather == "no" :
            print ("Wear light clothing.")  
     else:
        print("Invalid input. Please answer with yes or no.") 
     
weather_advice()
  