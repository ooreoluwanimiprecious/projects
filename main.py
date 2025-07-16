#LEAP YEAR CALCULATOR

def leap_year_calculator():
    year = int(input("Hello, enter the year you'll love to check: "))
    if year.lower() != "quit":
        try:
            year = int(input("Hello, enter the year you'll love to check: "))
        except Exception as e:
            print(f"Enter a valid number")



        if year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year)
    else:
        check_leap_year= True
leap_year_calculator(year_user)

while
    leap_year_calculator()