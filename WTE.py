print("WHERE TO EAT V1")

print("Choose three potential spots!")

option1 = input("Option 1: ")
option2 = input("Option 2: ")
option3 = input("Option 3: ")

print("Your options are:", option1, option2, option3)

if option1 == option2 == option3:
    print("All spots have an equal chance.")
else:
    print("Some spots have a greater chance than others.")

print("You are going to:", option2)
