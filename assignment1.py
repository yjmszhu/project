throw = ""
while True:
    throw = input("Do you want to roll the dice?")
    if throw !="no":
        import random
        face = random.randint(1,6)
        print(face)
        continue
    print("Fine,game over.")
    break