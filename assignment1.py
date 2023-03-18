import random
throw = ""
throw != "no"
while True:
    throw = input("Do you want to roll the dice?")
    
    if throw == "yes":
        face = random.randint(1,6)
        print(face)
    
    if throw == "no":
        print("Fine,game over.")
        break

    else:
        print("Please enter only yes or no.")