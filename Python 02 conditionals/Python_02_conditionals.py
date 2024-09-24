import random
from telnetlib import DO


print("Exercise 1")
#Exercise 1:
#First ask the user to input their age and store this in a variable. 
#Then output an appropriate message which confirms whether they are an adult or a child.

age = int(input("Enter your age: "))
if age < 18:
    print("You are a child.")
else:
    print("You are an adult.")    


print("\nExercise 2")
#Exercise 2
#Ask the user to enter two numbers and store these in variables respectively. Then display which one of the two numbers is greatest.
#Extension: Define this simple algorithm in a function that can be called to return the greater of the two numbers. Don't forget to call this function!

def compareNum():
    firstNumber = int(input("Enter the first number: "))  
    secondNumber = int(input("Enter the second number: "))
    
    if firstNumber > secondNumber:
        print(f"{firstNumber} is greater than {secondNumber}")
    elif secondNumber > firstNumber:
        print(f"{secondNumber} is greater than {firstNumber}")
    else:
        print("Both numbers are the same.")
        
compareNum()

print("\nExercise 3")
#Exercise 3:
#Write a program that uses a loop to print the numbers 1-10 to the screen. 
#Check that you know how to achieve this with both the 'while' loop and the 'for' loop so you know how the syntax differs.

i = 0
print("While loop:")
while i < 10:
    i += 1
    print(i)
    
print("\nFor loop:") 

for i in range(1,11):
    print(i)
    
print("\nExercise 4")
#Exercise 4:
#Write a program that will print only even numbers from a loop that repeats 10 times.
#Extension: Can you make a simple amendment to print only odd numbers?

for i in range(0,11):
    if i % 2 == 0:
        print(f"Even: {i}")
    else:
        print(f"Odd: {i}")


print("\nExercise 5")
#Exercise 5:
#Write a program that uses a loop to efficiently print the "seven times multiplication table". 
multiplicator = int(input("Enter a number to see its timetable: "))
                    
for i in range(1,13):
    print(f"{i} x {multiplicator} = {i * multiplicator}")


print("\nExercise 6")
#Exercise 6:
#Write a program that enables a student to enter a letter grade (A, B, C, D, E or F),
#then convert that to a university undergraduate classification (1st, 2:1, 2:2, 3rd, ordinary, fail).
#Extension 1: What happens if the user types in a lowercase letter?
#Does this affect the program? If so, how would you change the script?
#Extension 2: Can you place this conditional logic that converts grades to classifications in a function?

def convertGradeToClassification():
    grade = input("Enter the grade you recieved: ").capitalize()
    convertedGrade = None
    
    if grade == "A":
        convertedGrade = "1st"
    elif grade == "B":
        convertedGrade = "2:1"
    elif grade == "C":
        convertedGrade = "2:2"
    elif grade == "D":
        convertedGrade = "3rd"
    elif grade == "E":
        convertedGrade = "Ordinary"
    elif grade == "F":
        convertedGrade = "Fail"
    else:
        print("Invalid grade.")
        return
    
    print(f"Your converted grade is: {convertedGrade}")

convertGradeToClassification()


print("\nExercise 7")
#Exercise 7:
#Write a new program that asks the user to enter an exam mark (0-100).
#Write conditional statements to print out the grade they would achieve from this mark.
#Extension 1: Also define this logic as a function 'convert_mark_to_grade'
#Extension 2: Furthermore, also call the 'convert_grade_to_classification' function defined previously. 
#The user should be able to enter a single mark, which is then converted to a grade, which in turn is then converted to a degree classification.

def convertMarkToGrade():
    grade = None
    examMarks = int(input("Enter your exam marks (0-100): "))

    if examMarks < 0 or examMarks > 100: 
        print("Invalid marks. Please enter a value between 0 and 100.")
        return

    if examMarks < 40:
        grade = "F"
    elif examMarks >= 40 and examMarks <= 50:
        grade = "E"
    elif examMarks >= 51 and examMarks <= 60:
        grade = "D"
    elif examMarks >= 61 and examMarks <= 70:
        grade = "C"
    elif examMarks >= 71 and examMarks <= 80:
        grade = "B"
    elif examMarks >= 81 and examMarks <= 100:
        grade = "A"

    print(f"You have achieved Grade: {grade}")
    convertGradeToClassification()
convertMarkToGrade()
    
print("\nExercise 8")
#Exercise 8:
#Write a guessing game program in Python.
#The game should randomly assign a number between 1 and 100 to a variable
#(without the user knowing the selected number) each time the game is run.
#The user must then guess the number selected and should be guided by whether their guess is greater or less than the randomly chosen number. 
#The program should record how many guess attempts it takes to correctly identify the number.



def guessingGame():
    randomNumber = random.randint(1, 100)
    guess = False
    attempts = 0
    
    while guess != True:
        
        guessNumber = int(input("Guess the random number between 1 and 100: "))
        attempts += 1
        
        if guessNumber < randomNumber:
            print("Your guess is too low. Try again.")
        elif guessNumber > randomNumber:
            print("Your guess is too high. Try again.")
        else:
            guess = True
            print(f"\nCongratulations! You've guessed the number {randomNumber} in {attempts} attempts")
            
guessingGame()

print("\nExercise 9")
#Exercise 9 (which extends Exercise 8 from 01 Python Basics):
#Extend the previous exercise below to ask the user to first select which conversion they want to make. 
#Either 'miles to feet' or 'feet to miles'.
#Once they have chosen, then run the appropriate code to make the selected conversion. 
#You may wish to use functions to separate code.

def returnMilesToFeet():
    milesInput = float(input("Enter the number of miles: "))
    feetConverted = milesInput * 5280
    
    print(f"{milesInput} miles is equal to {feetConverted} feet")
    
    feetInput = float(input("Enter the conversion result you were shown: "))
    milesConverted = feetInput / 5280
    print(f"{feetInput} feet is equal to {milesConverted} miles")

def returnFeetToMiles():
    feetInput = float(input("Enter the number of feet: "))
    milesConverted = feetInput / 5280
    
    print(f"{feetInput} feet is equal to {milesConverted} miles")
    
    milesInput = float(input("Enter the conversion result you were shown: "))
    feetConverted = milesInput * 5280
    print(f"{milesInput} miles is equal to {feetConverted} feet")

def conversionChoice():
    choice = input("Choose conversion type (1: Miles to Feet, 2: Feet to Miles): ")
    return choice

def startConversion():
    choice = conversionChoice()

    if choice == '1':
        returnMilesToFeet()
    elif choice == '2':
        returnFeetToMiles()
    else:
        print("Invalid choice. Please select either 1 or 2")


startConversion()


print("\nExercise 10")
#Exercise 10:
#To extend the previous unit conversion exercise, now add a third unit (for example 'metres').
#Amend your code to account for conversions between three (3) units. 
#Consider whether there are efficiencies that can be made to prevent duplication across functions.

def convert(distance, fromUnit, toUnit):
    if fromUnit == 'miles' and toUnit == 'feet':
        return distance * 5280
    elif fromUnit == 'miles' and toUnit == 'meters':
        return distance * 1609.34
    elif fromUnit == 'feet' and toUnit == 'miles':
        return distance / 5280
    elif fromUnit == 'feet' and toUnit == 'meters':
        return distance / 3.28084
    elif fromUnit == 'meters' and toUnit == 'miles':
        return distance / 1609.34
    elif fromUnit == 'meters' and toUnit == 'feet':
        return distance * 3.28084
    
def startConversion():
    print("1: Miles to Feet, 2: Miles to Meters, 3: Feet to Miles, 4: Feet to Meters, 5: Meters to Miles, 6: Meters to Feet")
    choice = input("Enter your choice (1-6): ")
    
    match choice:
        case '1':
            fromUnit = 'miles'
            toUnit = 'feet'
        case '2':
            fromUnit = 'miles'
            toUnit = 'meters'
        case '3':
            fromUnit = 'feet'
            toUnit = 'miles'
        case '4':
            fromUnit = 'feet'
            toUnit = 'meters'
        case '5':
            fromUnit = 'meters'
            toUnit = 'miles'
        case '6':
            fromUnit = 'meters'
            toUnit = 'feet'
        case _:
            print("Invalid choice.")
            return

    distance = float(input(f"Enter the number of {fromUnit}: "))
    result = convert(distance, fromUnit, toUnit)
    print(f"{distance} {fromUnit} is equal to {result} {toUnit}")

startConversion()