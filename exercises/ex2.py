name = input("Put your name: ")
hour = int(input('Put the hour: '))

user = True

while user:

    if hour <= 11:
        print(f"Good morning, {name}!")
        break
    elif hour <= 17:
        print(f"Good afternoon, {name}!")
        break
    else:
        print(f"Good evening, {name}!")
        break
