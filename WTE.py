#Ideas: choose a fighter, D&D-style battles (short, 1v1 or 2v1)
import random
from collections import Counter

print("WHERE TO EAT V1")
print("")

allsame = False

#Asks how many options and displays integer answer
numOptions = int(input("How many options do you want to have? "))
print(f"You chose {numOptions} options. Input your spots.")

#Asks for option names and displays list in uppercase
options = [input(f"Option {i+1}: ") for i in range(numOptions)]
options = [s.upper() for s in options]
print("")
#print("Your options are:", *options) #prints out a list

def display_options(options, numOptions): #displays options with counts
    print("Your options are: ")
    numOptions = len(options)
    counts = Counter(options)
    for value, count in counts.items():
        print(f"{value}: {count} count ({round(count/numOptions*100, 2)}% base chance)") #prints out counts of each place

#Checks for duplicates and lets user know that some spots have a higher chance of being selected than others
def check_duplicates(options):
    def duplicates(list):
        return len(list) != len(set(list))
    if duplicates(options):
        print("\033[91mSome spots have a greater chance than others.\033[0m")
    else:
        print("All spots have an equal chance!")

#Eliminate one choice
def remove_one_random(lst, num):
    if not lst:
        return None
    else:
        index = random.randint(0, len(lst) -1)
        num -= 1
        return lst.pop(index)

def process():
    display_options(options, numOptions)
    check_duplicates(options)
    print("")

#process()

display_options(options, numOptions)
check_duplicates(options)

if len(set(options)) == 1:
    print(f"Your only option is \033[91m{options[-1]}!\033[0m")
else:
    while len(options) > 1:
        ready = str(input("Are you ready to eliminate one option? Y/N "))
        print("")
        ready = ready.lower()
        if ready in ["y", "yes"]:
            remove_one_random(options, numOptions)
            process()
        else:
            #print(f"Go to \033[91m{options[-1]}!\033[0m")
            print("While error.")
