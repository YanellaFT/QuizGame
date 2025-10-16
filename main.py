print("This is PyGames. You can play mini python games and quizes, as well as get useful conversions here. Choose one from the options below:")
print()
print("1. Time Converter: converts seconds to minutes, hours, days, weeks, months, and years")
print("2. Rock, Paper, Scissor, Shoot! play with the computer")
print("3. Length Converter: converts inches to feet, yards, miles, millimeters, centimeters, meters, and kilometers")
print("4. Quiz Game: a fun quiz game")
print("5. Random Number Generator: generates a random number between two numbers of your choice")
print("6. Hangman: guess the word one letter at a time")
print("7. To-do list: create your own to-do list and remove tasks from it as you complete them")
print("8. Spender-Checker: check if you have enough money to buy something")
print("9. Multiplier: learn your multiplication table")
print("10. Roman Numeral Converter: add two roman numerals together, and get their result in both integer and roman form")
print()
choice = input("Enter 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10: ")

if choice == "1": #time converter
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
elif choice == '2': #rock, paper, scissor, shoot
    print()
    print()
    print("ROCK, PAPER, SCISSOR, SHOOT!")
    print()
    print("Play the classic rock, paper, scissor shoot game.")
    print()

    list = ['rock', 'paper', 'scissor']
    import random
    score = 0
    s = 0 #number of stalemates in first three rounds

    print()
    print("Enter either rock, paper, or scissor (all lowercase)")

    for x in range(3):
        print()
        user = input("Your turn: ")
        computer = random.choice(list)
        print("The computer chose: " + computer)
        
        if (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
            score = score + 1
            print("You won this round! Score: " + str(score) + "/3")
        elif user == computer:
            print("Stalemate. ")
            s = s + 1
        else:
            print("You lost this round. Score: " + str(score) + "/3")
            
    if s > 0:
        for x in range(s):
            print()
            user = input("Your turn: ")
            computer = random.choice(list)
            print("The computer chose: " + computer)
            
            if (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
                score = score + 1
                print("You won this round! Score: " + str(score) + "/3")
            elif user == computer:
                print("Stalemate.")
                print()
                user = input("Your turn: ")
                computer = random.choice(list)
                print("The computer chose: " + computer)
                if (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
                    score = score + 1
                    print("You won this round! Score: " + str(score) + "/3")
                elif user == computer:
                    print("Stalemate. ")
                else:
                    print("You lost this round. Score: " + str(score) + "/3")
            else:
                print("You lost this round. Score: " + str(score) + "/3")
    #figure out how to make it 3 rounds in case pic happens        
    if s == 3:
        for x in range(s + 1):
            print()
            user = input("Your turn: ")
            computer = random.choice(list)
            print("The computer chose: " + computer)
            
            if (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
                score = score + 1
                print("You won this round! Score: " + str(score) + "/3")
            elif user == computer:
                print("Stalemate.")
                print()
                user = input("Your turn: ")
                computer = random.choice(list)
                print("The computer chose: " + computer)
                if (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
                    score = score + 1
                    print("You won this round! Score: " + str(score) + "/3")
                elif user == computer:
                    print("Stalemate. ")
                else:
                    print("You lost this round. Score: " + str(score) + "/3")
            else:
                print("You lost this round. Score: " + str(score) + "/3")

    print("Thank you for playing Rock, Paper, Scissor, Shoot! Refresh to choose another option.")
elif choice == '3': #length converter
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
elif choice == '4': #quiz game
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
elif choice == '5': #random number generator
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
    print("The random number between " + minimum + " and " + maximum + " is " + str(randomNumber))
    print()
    print("Thank you for using the Random Number Generator! Refresh to choose another option.")
elif choice == '6': #hangman
    print()
    print()
    print("HANGMAN")
    print()
    print("Guess the letters in the word one at a time. You have seven attempts to guess the word correctly.")
    print()

    used = []

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
        used.append(guess1)
        print("Incorrect letters: " + str(used))
    
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
        used.append(guess2)
        print("Incorrect letters: " + str(used))
    
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
        used.append(guess3)
        print("Incorrect letters: " + str(used))

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
        used.append(guess4)
        print("Incorrect letters: " + str(used))

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
        used.append(guess5)
        print("Incorrect letters: " + str(used))

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
        used.append(guess6)
        print("Incorrect letters: " + str(used))

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
        used.append(guess7)
        print("Incorrect letters: " + str(used))
    
    print()
    if firstLetter == "P" and secondLetter == "Y" and thirdLetter == "T" and fourthLetter == "H" and fifthLetter == "O" and sixthLetter == "N":
        print("Congratulations! You guessed the word correctly: PYTHON")
        print("Thank you for playing Hangman! Refresh to choose another option.")
    else:
        print("Sorry, you did not guess the word correctly. Refresh to try again or choose another option.")
elif choice == '7': #to-do list
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


    #add task2
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


    #remove tasks
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
elif choice == '8': #spender-checker
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

        x=x+1

        print()
    
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
elif choice == '9': #multiplier
    print()
    print()
    print("MULTIPLIER")
    print()
    print("Learn your multiplication tables!")
    print()

    table = input("What multiplication table would you like to learn? (Enter 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12) ")
    i = 0

    if table == '2':
        for x in range(0, 25, 2):
            multiple = int(i)*int(table)
            print(str(i) + " times 2 is " + str(multiple))
            if multiple == 24:
                print()
                print("You finished the 2 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1

    elif table == '3':
        for x in range(0, 37, 3):
            multiple = int(i)*int(table)
            print(str(i) + " times 3 is " + str(multiple))
            if multiple == 36:
                print()
                print("You finished the 3 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '4':
        for x in range(0, 49, 4):
            multiple = int(i)*int(table)
            print(str(i) + " times 4 is " + str(multiple))
            if multiple == 48:
                print()
                print("You finished the 4 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '5':
        for x in range(0, 61, 5):
            multiple = int(i)*int(table)
            print(str(i) + " times 5 is " + str(multiple))
            if multiple == 60:
                print()
                print("You finished the 5 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '6':
        for x in range(0, 73, 6):
            multiple = int(i)*int(table)
            print(str(i) + " times 6 is " + str(multiple))
            if multiple == 72:
                print()
                print("You finished the 2 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '7':
        for x in range(0, 85, 7):
            multiple = int(i)*int(table)
            print(str(i) + " times 7 is " + str(multiple))
            if multiple == 84:
                print()
                print("You finished the 7 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '8':
        for x in range(0, 97, 8):
            multiple = int(i)*int(table)
            print(str(i) + " times 8 is " + str(multiple))
            if multiple == 96:
                print()
                print("You finished the 8 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '9':
        for x in range(0, 109, 9):
            multiple = int(i)*int(table)
            print(str(i) + " times 9 is " + str(multiple))
            if multiple == 108:
                print()
                print("You finished the 9 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '10':
        for x in range(0, 121, 10):
            multiple = int(i)*int(table)
            print(str(i) + " times 10 is " + str(multiple))
            if multiple == 120:
                print()
                print("You finished the 10 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '11':
        for x in range(0, 133, 11):
            multiple = int(i)*int(table)
            print(str(i) + " times 11 is " + str(multiple))
            if multiple == 132:
                print()
                print("You finished the 11 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
    elif table == '12':
        for x in range(0, 145, 12):
            multiple = int(i)*int(table)
            print(str(i) + " times 12 is " + str(multiple))
            if multiple == 144:
                print()
                print("You finished the 12 times table!")
                print("Thank you for using the Multiplier! Refresh to choose another option.")
            else: 
                input('Press ENTER to see next multiple')
            i += 1
elif choice == '10': #roman numeral converter
    print()
    print()
    print("ROMAN NUMERAL CONVERTER")
    print()
    print()
    print("Add two roman numerals together, and their their results in both integer and roman form.")
    print()



    roman1 = input("Enter a roman numeral: ")
    roman1 = roman1.upper() #check this to make sure it works
    roman1split = " ".join(roman1)
    roman1num = roman1split.split()
    #print(f"roman1split = {roman1split}")
    #print(f"roman1num = {roman1num}")

    roman1 = []

    #CHANGES ROMAN TO NUMBERS
    for i in range(len(roman1split)):
        
        if roman1split[i] == "I":
            #roman1num = roman1split.replace('I', '1') dont need this is append on a different list
            roman1.append(int(1))
            #print(roman1) this line to check if working       
        elif roman1split[i] == "V": 
            roman1.append(int(5))
            #print(roman1)
        elif roman1split[i] == "X":
            roman1.append(int(10))
            #print(roman1)
        elif roman1split[i] == "L":
            roman1.append(int(50))
            #print(roman1)
        elif roman1split[i] == "C":
            roman1.append(int(100))
            #print(roman1)
        elif roman1split[i] == "D":
            roman1.append(int(500))
            #print(roman1)
        elif roman1split[i] == "M":
            roman1.append(int(1000))
            #print(roman1)

    ''' dont think you need this...'''
    #ADDS EXTRA INDEXES FOR NEXT STEP
    if len(roman1) == 2:
        roman1.append(0)
    elif len(roman1) == 1:
        roman1.append(0)
        roman1.append(0)
   

    h = 0
    #CHECK FOR SUBTRACTING CASES
    for c in range(len(roman1)-1):
        if roman1[h] == 1 and roman1[h+1] == 5:
            roman1[h] = 4
            roman1[h+1] = 0 #check to see if .pop works doesnt seem to work with index problems
            #print(roman1) this line to check if working
        elif roman1[h] == 1 and roman1[h+1] == 10:
            roman1[h] = 9
            roman1[h+1] = 0
            #print(roman1)
        elif roman1[h] == 10 and roman1[h+1] == 50:
            roman1[h] = 40
            roman1[h+1] = 0 
            #print(roman1)
        elif roman1[h] == 10 and roman1[h+1] == 100: 
            roman1[h] = 90
            roman1[h+1] = 0
            #print(roman1)
        elif roman1[h] == 100 and roman1[h+1] == 500:
            roman1[h] = 400
            roman1[h+1] = 0 
            #print(roman1)
        elif roman1[h] == 100 and roman1[h+1] == 1000:
            roman1[h] = 900
            roman1[h+1] = 0
            #print(roman1)
        elif roman1[h] == 50 and roman1[h+1] == 100:
            roman1[h] = 50
            roman1[h+1] = 0
        h = h + 1
        
    number1 = sum(roman1)
    print(f"Integer value: {number1}")

    print()
    roman2 = input("Enter another roman numeral: ")
    roman2 = roman2.upper()
    roman2split = " ".join(roman2)
    roman2num = roman2split.split()
    #print(f"roman2split = {roman2split}")
    #print(f"roman2num = {roman2num}")
    
    roman2 = []

    j = 0
    #CHANGES ROMAN TO NUMBERS
    for b in range(len(roman2split)):
        if roman2split[j] == "I":
            roman2.append(int(1))
            #print(roman2)
        elif roman2split[j] == "V":
            roman2.append(int(5))
            #print(roman2)
        elif roman2split[j] == "X":
            roman2.append(int(10))
            #print(roman2)
        elif roman2split[j] == "L":
            roman2.append(int(50))
            #print(roman2)
        elif roman2split[j] == "C":
            roman2.append(int(100))
            #print(roman2)
        elif roman2split[j] == "D":
            roman2.append(int(500))
            #print(roman2)
        elif roman2split[j] =="M":
            roman2.append(int(1000))
            #print(roman2)
        j = j + 1


    ''' dont think you need this...'''
    #ADDS EXTRA INDEXES FOR NEXT STEP
    if len(roman2) == 2:
        roman2.append(0)
    elif len(roman2) == 1:
        roman2.append(0)
        roman2.append(0)

    k = 0
    #CHECK FOR SUBTRACTING ONES
    for a in range(len(roman2)-1):
        if roman2[k] == 1 and roman2[k+1] == 5:
            roman2[k] = 4
            roman2[k+1] = 0
        elif roman2[k] == 1 and roman2[k+1] == 10:
            roman2[k] = 9
            roman2[k+1] = 0
        elif roman2[k] == 10 and roman2[k+1] == 50:
            roman2[k] = 40
            roman2[k+1] = 0
        elif roman2[k] == 10 and roman2[k+1] == 100:
            roman2[k] = 90
            roman2[k+1] = 0
        elif roman2[k] == 100 and roman2[k+1] == 500:
            roman2[k] = 400
            roman2[k+1] = 0
        elif roman2[k] == 100 and roman2[k+1] == 1000:
            roman2[k] = 900
            roman2[k+1] = 0
        elif roman2[k] == 50 and roman2[k+1] == 100:
            roman2[k] = 50
            roman2[k+1] = 0
        k = k + 1

    #CONVERTS TO INTEGER
    number2 = sum(roman2)
    print(f"Integer value: {number2}")

    # ADDS THEM TOGETHER FOR TOTAL
    print()
    total = number1 + number2
    print("Adding them together you get: " + str(total))

    #CONVERTS BACK INTO BASE TEN
    x = len(str(total))
    #print()

    if x == 2:
        total = " ".join(str(total))
        totalSplit = str(total).split()
        totalSplit[0] = int(totalSplit[0])*10
        totalSplit[1] = int(totalSplit[1])*1
    elif x == 3:
        total = " ".join(str(total))
        totalSplit = str(total).split()
        totalSplit[0] = totalSplit[0]*100
        totalSplit[1] = int(totalSplit[1])*10
        totalSplit[2] = int(totalSplit[2])*1
    elif x == 4:
        total = " ".join(str(total))
        totalSplit = str(total).split()
        totalSplit[0] = int(totalSplit[0])*1000
        totalSplit[1] = int(totalSplit[1])*100
        totalSplit[2] = int(totalSplit[2])*10
        totalSplit[3] = int(totalSplit[3])*1
    elif x == 1:
        total = " ".join(str(total))
        totalSplit = str(total).split()
        totalSplit[0] = int(totalSplit[0])*1
    else:
        print("This number does not exist in roman numerals.")

    
    #CONVERTS BACK INTO ROMAN
    p = 0
    for y in range(len(totalSplit)):
        if totalSplit[p] == 1:
            totalSplit[p] = "I"
            p=p+1
        elif totalSplit[p] == 2:
            totalSplit[p] = "II"
            p=p+1
        elif totalSplit[p] == 3:
            totalSplit[p] = "III"
            p=p+1
        elif totalSplit[p] == 4:
            totalSplit[p] = "IV"
            p=p+1
        elif totalSplit[p] == 5:
            totalSplit[p] = "V"
            p=p+1
        elif totalSplit[p] == 6:
            totalSplit[p] = "VI"
            p=p+1
        elif totalSplit[p] == 7:
            totalSplit[p] = "VII"
            p=p+1
        elif totalSplit[p] == 8:
            totalSplit[p] = "VIII"
            p=p+1
        elif totalSplit[p] == 9:
            totalSplit[p] = "IX"
            p=p+1

        elif totalSplit[p] == 10:
            totalSplit[p] = "X"
            p=p+1
        elif totalSplit[p] == 20:
            totalSplit[p] = "XX"
            p=p+1
        elif totalSplit[p] == 30:
            totalSplit[p] = "XXX"
            p=p+1
        elif totalSplit[p] == 40:
            totalSplit[p] = "XL"
            p=p+1
        elif totalSplit[p] == 50:
            totalSplit[p] = "L"
            p=p+1
        elif totalSplit[p] == 60:
            totalSplit[p] = "LX"
            p=p+1
        elif totalSplit[p] == 70:
            totalSplit[p] = "LXX"
            p=p+1
        elif totalSplit[p] == 80:
            totalSplit[p] = "LXXX"
            p=p+1
        elif totalSplit[p] == 90:
            totalSplit[p] = "XC"
            p=p+1

        elif totalSplit[p] == 100:
            totalSplit[p] = "C"
            p=p+1
        elif totalSplit[p] == 200:
            totalSplit[p] = "CC"
            p=p+1
        elif totalSplit[p] == 300:
            totalSplit[p] = "CCC"
            p=p+1
        elif totalSplit[p] == 400:
            totalSplit[p] = "CD"
            p=p+1
        elif totalSplit[p] == 500:
            totalSplit[p] = "D"
            p=p+1
        elif totalSplit[p] == 600:
            totalSplit[p] = "DC"
            p=p+1
        elif totalSplit[p] == 700:
            totalSplit[p] = "DCC"
            p=p+1
        elif totalSplit[p] == 800:
            totalSplit[p] = "DCCC"
            p=p+1
        elif totalSplit[p] == 900:
            totalSplit[p] = "CM"
            p=p+1
        
        elif totalSplit[p] == 1000:
            totalSplit[p] = "M"
            p=p+1
        elif totalSplit[p] == 2000:
            totalSplit[p] = "MM"
            p=p+1
        elif totalSplit[p] == 3000:
            totalSplit[p] = "MMM"
            p=p+1
        
        else:
            totalSplit[p] = ""
            p=p+1
        
        #print(totalSplit)
    
    end = "".join(totalSplit)
    print(f"Which is {end} in roman numerals.")
    print()
    

    print("Thank you for using the Roman Numeral Converter! Refresh to choose another option.")
else:
    print("That was not an option. Please refresh and try again.")


