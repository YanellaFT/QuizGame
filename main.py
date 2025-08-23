print("This is PyGames. You can play mini python games and quizes, as well as get useful conversions here. Choose one from the options below:")
print()
print("1. Time Converter: converts seconds to minutes, hours, days, weeks, months, and years")
print("2. Roman Numeral Converter: roman numerals to integers")
print("3. Length Converter: converts inches to feet, yards, miles, millimeters, centimeters, meters, and kilometers")
print("4. Quiz Game: a fun quiz game")
print()
choice = input("Enter 1, 2, 3, 4: ")

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