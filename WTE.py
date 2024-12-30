#Ideas: choose a fighter, D&D-style battles (short, 1v1 or 2v1)

print("WHERE TO EAT V1")

print("Choose three potential spots.")

option1 = input("Option 1: ")
option1 = option1.upper()
option2 = input("Option 2: ")
option2 = option2.upper()
option3 = input("Option 3: ")
option3 = option3.upper()

print("Your options are:", option1, option2, option3)

if option1 != option2 != option3:
    print("All spots have an equal chance.")
else:
    print("Some spots have a greater chance than others.")

ready = str(input("Do you want me to decide? Y/N "))
ready = ready.lower()

if ready in ["y", "yes"]:
    print("You are going to:", option2)
else:
    print("Come back soon!")

