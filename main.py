print("This is PyGames. You can play mini python games and quizes, as well as get useful conversions here. Choose one from the options below:")
print()
print("1. Time Converter: converts seconds to minutes, hours, days, weeks, months, and years")
print("2. Roman Numeral Converter: roman numerals to integers")
print("3. Length Converter: converts inches to feet, yards, miles, millimeters, centimeters, meters, and kilometers")
print()
choice = input("Enter 1, 2, 3: ")

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

    centimeters = int(millimeters) * 10 #millimeters to centimeters
    print(str(centimeters) + " centimeters")

    meters = int(centimeters) * 100 #centimeters to meters
    print(str(meters) + " meters")

    kilometers = int(meters) / 1000 #meters to kilometers
    print(str(kilometers) + " kilometers")