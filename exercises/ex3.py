name = input("Put your name: ")
name_len = len(name)

if name_len <= 4:
    print("Your name is small.")
elif name_len == 5 or name_len == 6:
    print("Your name is normal.")
else:
    print("Your name is big.")
