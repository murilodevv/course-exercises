# Exercise 1
import numbers

user = True

while user:
    print("Welcome to the Number Game.")
    integer = input("Put an integer number: ")

    try:
        if int(integer) % 2 == 0:
            print("This number is even.")
            choose = input("Do you want play again? (Yes or No): ")
            if choose.lower() == 'no':
                print("Thanks for playing :)")
                break
            elif choose.lower() != 'no' and choose.lower() != 'yes':
                print("Error: invalid input.")
            else:
                continue
        else:
            print("This number is odd.")
            choose = input("Do you want play again? (Yes or No): ")
            if choose.lower() == 'no':
                print("Thanks for playing :)")
                break
            elif choose.lower() != 'no' and choose.lower() != 'yes':
                print("Error: invalid input.")
            else:
                continue
    except:
        print("The input is not a number.")

# Exercise 2

# TODO