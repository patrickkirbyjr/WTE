#Ideas: choose a fighter, D&D-style battles (short, 1v1 or 2v1)
import random

print("WHERE TO EAT V1")

#Asks how many options and displays integer answer
numOptions = int(input("How many options do you want to have? "))
print(f"You chose {numOptions} options. Input your spots.")

#Asks for option names and displays list in uppercase
options = [input(f"Option {i+1}: ") for i in range(numOptions)]
options = [s.upper() for s in options]
print("Your options are:", *options)

#Checks for duplicates and lets user know that some spots have a higher chance of being selected than others
def duplicates(list):
    return len(list) != len(set(list))

if duplicates(options):
    print("\033[91mSome spots have a greater chance than others.\033[0m")
else:
    print("All spots have an equal chance!")

choice = random.choice(options)

ready = str(input("Are you ready for your random choice? Y/N "))
ready = ready.lower()
if ready in ["y", "yes"]:
    print(f"Head to \033[34m{choice}!\033[0m")
else:
    print("Come back soon!")