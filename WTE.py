#Ideas: choose a fighter, D&D-style battles (short, 1v1 or 2v1)

print("WHERE TO EAT V1")

#Asks how many options and displays integer answer
numOptions = int(input("How many options do you want to have? "))
print(f"You chose {numOptions} options.")

#Asks for option names and displays list in uppercase
options = [input(f"Option {i+1}: ") for i in range(numOptions)]
options = [s.upper() for s in options]
print("Your options are:", *options)

#Checks for duplicates and lets user know that some spots have a higher chance of being selected than others
def duplicates(list):
    return len(list) != len(set(list))

if duplicates(options):
    print("Some spots have a greater chance than others.")
else:
    print("All spots have an equal chance.")