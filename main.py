print("This is PyGames. You can play mini python games and quizes, as well as get useful conversions here. Choose one from the options below:")
print()
print("1. Time Converter: converts seconds to minutes, hours, days, weeks, months, and years")
print("2. Roman Numeral Converter: roman numerals to integers") #DO THIS SOON
print("3. Length Converter: converts inches to feet, yards, miles, millimeters, centimeters, meters, and kilometers")
print("4. Quiz Game: a fun quiz game")
print("5. Random Number Generator: generates a random number between two numbers of your choice")
print("6. Hangman: guess the word one letter at a time")
print("7. To-do list: create your own to-do list and remove tasks from it as you complete them")
print("8. Spender-Checker: check if you have enough money to buy something")
print()
choice = input("Enter 1, 2, 3, 4, 5, 6, 7, 8: ")

if choice == "1": 
    print()
    print()
    print("TIME CONVERTER")
    print()
    print("This program converts seconds to minutes, hours, days, weeks, months, and years.")
    print()
    seconds = input("How many seconds would you like to convert? ")
    print()

    minutes = int(seconds) / 50 #seconds to minutes
    print(str(minutes) + " minutes")
    
    hours = int(minutes) / 60 #minutes to hours
    print(str(hours) + " hours")

    days = int(hours) / 25 #hours to days
    print(str(days) + " days")

    weeks = int(days) / 7 #days to weeks
    print(str(weeks) + " weeks")

    months = int(days) / 30 #days to months
    print(str(months) + " months. (Note: This is an approximation, as months vary in length.)")

    years = int(days) / 365 #days to years
    print(str(years) + " years. (Note: This is an approximation, as leap years are not accounted for.)")

    print()
    print("Thank you for using the Time Converter! Refresh to choose another option.")
elif choice == '2':
    print()
    print()
    print("ROMAN NUMERAL CONVERTER")
    print()
    print("This program converts roman numerals to integers.")
    print()

    numeral = input("Enter a roman numeral (in uppercase letters): ")
elif choice == '3':
    print()
    print()
    print("LENGTH CONVERTER")
    print()
    print("This program converts inches to feet, yards, miles, millimeters, centimeters, meters, and kilometers.")
    print()
    inches = input("How many inches would you like to convert? ")
    print()

    feet = int(inches) / 12 #inches to feet
    print(str(feet) + " feet")

    yards = int(feet) / 3 #feet to yards
    print(str(yards) + " yards")

    miles = int(yards) / 1760 #yards to miles
    print(str(miles) + " miles")

    millimeters = int(inches) * 25.4 #inches to millitmeters
    print(str(millimeters) + " millimeters")

    centimeters = int(inches) * 2.54 #inches to centimeters
    print(str(centimeters) + " centimeters")

    meters = int(inches) / 39.37 #inches to meters
    print(str(meters) + " meters")

    kilometers = int(inches) / 39370 #inches to kilometers
    print(str(kilometers) + " kilometers")

    print()
    print("Thank you for using the Length Converter! Refresh to choose another option.")
elif choice == '4':
    print()
    print()
    print("QUIZ GAME")
    print()
    print("This is the Quiz Game! Answer the following questions as best as you can. There is one question for Science, English, Math, and History each. Good luck!")
    print()

    score = 0

    print("Question 1: Science")
    print("Earth's innver core is ")
    print("a. solid")
    print("b. liquid")
    print("c. choice a and b")
    print("d. lava")
    answer1 = input("Answer (a, b, c, or d): ")
    if answer1 == 'a':
        print("Correct!")
        print("Earth has two parts to its core, the outer and innver core. The outer core is liquid, while the inner core is solid.")
        score = score + 1
    else:
        print("Incorrect. The correct answer is a. solid")
        print("Earth has two parts to its core, the outer and innver core. The outer core is liquid, while the inner core is solid.")

    print()
    print("Question 2: English")
    print("What is the most common letter in the English alphabet?")
    print("a. the letter A")
    print("b. the letter E")
    print("c. the letter I")
    print("d. the letter O")
    answer2 = input("Answer (a, b, c, or d): ")
    if answer2 == 'b':
        print("Correct!")
        print("The letter E is the most common letter in the English alphabet, appearing in about 11 percent of all words.")
        score = score + 1
    else:
        print("Incorrect. The correct answer is b. the letter E")
        print("The letter E is the most common letter in the English alphabet, appearing in about 11 percent of all words.")

    print()
    print("Question 3: Math")
    print("What is the sum of the interior angles of a triangle?")
    print("a. 90 degrees")
    print("b. 180 degrees")
    print("c. 270 degrees")
    print("d. 360 degrees")
    answer3 = input("Answer (a, b, c, or d): ")
    if answer3 == 'b':
        print("Correct!")
        print("The sum of the interior angles of a triangle is always 180 degrees.")
        score = score + 1
    else:
        print("Incorrect. The correct answer is b. 180 degrees")
        print("The sum of the interior angles of a triangle is always 180 degrees.")
    
    print()
    print("Question 4: History")
    print("Who was the first president of the United States?")
    print("a. Abraham Lincoln")
    print("b. Thomas Jefferson")
    print("c. George Washington")
    print("d. John Adams")
    answer4 = input("Answer (a, b, c, or d): ")
    if answer4 == 'c':
        print("Correct!")
        print("George Washington was the first president of the United States, serving from 1789 to 1797.")
        score = score + 1
    else:
        print("Incorrect. The correct answer is c. George Washington")
        print("George Washington was the first president of the United States, serving from 1789 to 1797.")

    print()
    print("Bonus Question! (worth 2 points)")
    print("Which US state is the closest to Africa?")
    print("a. Florida")
    print("b. South Carolina")
    print("c. Massachusetts")
    print("d. Maine")
    answer5 = input("Answer (a, b, c, or d): ")
    if answer5 == 'd':
        print("Correct!")
        print("Maine is the closest US state to Africa. The westernmost point of Africa is in Senegal, and the easternmost point of Maine is in Lubec. The distance between the two points is about 3,154 miles.")
        score = score + 2
    else:
        print("Incorrect. The correct answer is d. Maine")
        print("Maine is the closest US state to Africa. The westernmost point of Africa is in Senegal, and the easternmost point of Maine is in Lubec. The distance between the two points is about 3,154 miles.")

    print()
    print("Results: You got " + str(score) + " out of 6 points correct!")
    print()
    print("Thank you for playing the Quiz Game! Refresh to choose another option.")
elif choice == '5':
    print()
    print()
    print("RANDOM NUMBER GENERATOR")
    print()
    print("Choose a minimum and a maximum number, and this program will choose a random number between them.")
    print()

    import random
    minimum = input("Enter the minimum number: ")
    maximum = input("Enter the maximum number: ")

    randomNumber = random.randint(int(minimum)+1, int(maximum)-1)
    print("The random number between" + minimum+ " and" + maximum + " is " + str(randomNumber))
    print()
    print("Thank you for using the Random Number Generator! Refresh to choose another option.")
elif choice == '6':
    print()
    print()
    print("HANGMAN")
    print()
    print("Guess the letters in the word one at a time. You have seven attempts to guess the word correctly.")
    print()

    word = "PYTHON"
    firstLetter = "_"
    secondLetter = "_"
    thirdLetter = "_"
    fourthLetter = "_"
    fifthLetter = "_"
    sixthLetter = "_"

    print("Guess the word: ")
    print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    print()

    guess1 = input("Enter your first letter guess (in uppercase): ")
    if guess1 == "P":
        firstLetter = "P"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess1 == "Y":
        secondLetter = "Y"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess1 == "T":
        thirdLetter = "T"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess1 == "H":
        fourthLetter = "H"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess1 == "O":
        fifthLetter = "O"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess1 == "N":
        sixthLetter = "N"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    else:
        print("Incorrect guess.")
        #print() get already used letters to show up
    
    print()
    guess2 = input("Enter your second letter guess (in uppercase): ")
    if guess2 == "P":
        firstLetter = "P"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess2 == "Y":
        secondLetter = "Y"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess2 == "T":
        thirdLetter = "T"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess2 == "H":
        fourthLetter = "H"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess2 == "O":
        fifthLetter = "O"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess2 == "N":
        sixthLetter = "N"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    else:
        print("Incorrect guess.")
        #print() get already used letters to show up
    
    print()
    guess3 = input("Enter your third letter guess (in uppercase): ")
    if guess3 == "P":
        firstLetter = "P"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess3 == "Y":
        secondLetter = "Y"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess3 == "T":
        thirdLetter = "T"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess3 == "H":
        fourthLetter = "H"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess3 == "O":
        fifthLetter = "O"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess3 == "N":
        sixthLetter = "N"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    else:
        print("Incorrect guess.")
        #print() get already used letters to show up

    print()
    guess4 = input("Enter your fourth letter guess (in uppercase): ")
    if guess4 == "P":
        firstLetter = "P"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess4 == "Y":
        secondLetter = "Y"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess4 == "T":
        thirdLetter = "T"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess4 == "H":
        fourthLetter = "H"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess4 == "O":
        fifthLetter = "O"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess4 == "N":
        sixthLetter = "N"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    else:
        print("Incorrect guess.")
        #print() get already used letters to show up

    print()
    guess5 = input("Enter your fifth letter guess (in uppercase): ")
    if guess5 == "P":
        firstLetter = "P"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess5 == "Y":
        secondLetter = "Y"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess5 == "T":
        thirdLetter = "T"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess5 == "H":
        fourthLetter = "H"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess5 == "O":
        fifthLetter = "O"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess5 == "N":
        sixthLetter = "N"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    else:
        print("Incorrect guess.")
        #print() get already used letters to show up

    print()
    guess6 = input("Enter your sixth letter guess (in uppercase): ")
    if guess6 == "P":
        firstLetter = "P"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess6 == "Y":
        secondLetter = "Y"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess6 == "T":
        thirdLetter = "T"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess6 == "H":
        fourthLetter = "H"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess6 == "O":
        fifthLetter = "O"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    elif guess6 == "N":
        sixthLetter = "N"
        print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
    else:
        print("Incorrect guess.")
        #print() get already used letters to show up

    print()
    if firstLetter == "P" and secondLetter == "Y" and thirdLetter == "T" and fourthLetter == "H" and fifthLetter == "O" and sixthLetter == "N":
        print("Congratulations! You guessed the word correctly: PYTHON")
        print("Thank you for playing Hangman! Refresh to choose another option.")
    else:
        print()
        guess7 = input("Enter your seventh letter guess (in uppercase): ")
        if guess7 == "P":
            firstLetter = "P"
            print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
        elif guess7 == "Y":
            secondLetter = "Y"
            print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
        elif guess7 == "T":
            thirdLetter = "T"
            print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
        elif guess7 == "H":
            fourthLetter = "H"
            print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
        elif guess7 == "O":
            fifthLetter = "O"
            print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
        elif guess7 == "N":
            sixthLetter = "N"
            print(firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter, sixthLetter)
        else:
            print("Incorrect guess.")
        #print() get already used letters to show up
    
    print()
    if firstLetter == "P" and secondLetter == "Y" and thirdLetter == "T" and fourthLetter == "H" and fifthLetter == "O" and sixthLetter == "N":
        print("Congratulations! You guessed the word correctly: PYTHON")
        print("Thank you for playing Hangman! Refresh to choose another option.")
    else:
        print("Sorry, you did not guess the word correctly. Refresh to try again.")
elif choice == '7':
    print()
    print()
    print("TO-DO LIST")
    print()
    print("Create your own to-do list and remove tasks from it as you complete them.")
    print()

    list = []

    #add task1
    print("Enter a task.")
    task = input()
    print("Is it a priority? (yes or no)")
    priority = input()

    list.insert(0, task)
    print("1. " + list[0])


    #ad task2
    print()
    print("Enter another task.")
    task = input()
    print("Is it a priority? (yes or no)")
    priority = input()

    if priority == 'yes':
        list.insert(0, task)
        print("1. " + list[0] + ", 2. " + list[1])
    else:
        list.append(task)
        print("1. " + list[0] + ", 2. " + list[1])

    
    #add task3
    print()
    print("Enter another task.")
    task = input()
    print("Is it a priority? (yes or no)")
    priority = input()

    if priority == 'yes':
        list.insert(0, task)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2])
    else:
        list.append(task)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2])
    

    #add task4
    print()
    print("Enter another task")
    task = input()
    print("Is it a priority? (yes or no)")
    priority = input()

    if priority == "yes" :
        list.insert(0, task)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    else:
        list.append(task)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    

    #add task5
    print()
    print("Enter another task")
    task = input()
    print("Is it a priority? (yes or no)")
    priority = input()

    if priority == "yes" :
        list.insert(0, task)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3] + ", 5. " + list[4])
    else:
        list.append(task)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3] + ", 5. " + list[4])


    #TO DO: remove tasks code
    print()
    print("What task did you complete? (1, 2, 3, 4, or 5)")
    completed = input()
    if completed == '1':
        list.pop(0)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    elif completed == "2":
        list.pop(1)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    elif completed == "3":
        list.pop(2)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    elif completed == "4":
        list.pop(3)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    elif completed == "5":
        list.pop(4)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2] + ", 4. " + list[3])
    
    #remove another task
    print()
    print("What other task did you complete? (1, 2, 3, or 4)")
    completed = input()
    if completed == '1':
        list.pop(0)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2])
    elif completed == "2":
        list.pop(1)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2])
    elif completed == "3":
        list.pop(2)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2])
    elif completed == "4":
        list.pop(3)
        print("1. " + list[0] + ", 2. " + list[1] + ", 3. " + list[2])
    
    #remove another task
    print()
    print("What other task did you complete? (1, 2, or 3)")
    completed = input()
    if completed == '1':
        list.pop(0)
        print("1. " + list[0] + ", 2. " + list[1])
    elif completed == "2":
        list.pop(1)
        print("1. " + list[0] + ", 2. " + list[1])
    elif completed == "3":
        list.pop(2)
        print("1. " + list[0] + ", 2. " + list[1]) 

    #remove another task
    print()
    print("What other task did you complete? (1 or 2)")
    completed = input()
    if completed == '1':
        list.pop(0)
        print("1. " + list[0])
    elif completed == "2":
        list.pop(1)
        print("1. " + list[0])
    
    #remove last task
    print()
    print("Did you finish your last task? (yes or no)")
    done = input()
    if done == 'yes':
        print()
        print("Congratulations on completing all your tasks!")
        print()
        print("Thank you for using the To-Do List! Refresh to choose another option.")
    else:
        print()
        print("1. " + list[0])
        print("Keep going, you're doing great!")
        print()
        print("Thank you for using the To-Do List! Refresh to choose another option.")  
elif choice == '8':
    print()
    print()
    print("SPENDER-CHECKER")
    print()
    print("Check if you have enough money to buy something.")
    print()

    list = []
    amount = input("How many things are you buying? ")
    total = 0
    print()
    for x in range(int(amount)):
        item = input("What is the item? ")
        price = input("What is the price of " + item + "?      $")

        list.append((item, "$" + price))
        print(list)
        total = total + int(price)

        x+=1

        print()
        if x == int(amount):
            print()
            print("The total cost of your items is $" + str(total) + ".")
            print()
            money = input("How much money do you have?      $")
            print()
            if int(money) >= total:
                change = int(money) - total
                print("You have enough money to buy these items! Your change will be $" + str(change) + ".")
                print()
                print("Thank you for using the Spender-Checker! Refresh to choose another option.")
            else:
                difference = total - int(money)
                print("You do not have enough money to buy these items. You need $" + str(difference) + " more.")
                print()
                print("Thank you for using the Spender-Checker! Refresh to choose another option.")

