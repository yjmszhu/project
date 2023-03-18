import random
num = random.randint(1,100)
guess = ""
guess != num
while True:
    guess = input("Can you guess the number between 1 to 100?")
    try:
        value = int(guess)
    except ValueError:
        print("Please enter a number.")
        continue
    if value == num:
        print("Bingo!")
        break
    if value > num:
        print("Too high!")
    else:
        print("Too low!")