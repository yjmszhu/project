def startroom():
	direction = ["front","back","left","right"]
	print("Now you are in start room, nothing special here, you are suggested to move to escape.")
	select = ""
	while select not in direction:
		select = input("Please enter only front/back/left/right.")
		if select == "front":
			saferoom1()
		elif select == "back":
			print("There is no door but just wall!")
			startroom()
		elif select == "left":
			saferoom3()
		elif select == "right":
			saferoom2()
		else:
			print("Invalid! Please enter only front/back/left/right.")

def saferoom1():
	direction = ["front","back","left","right"]
	print("Now you are in safe room 1, nothing special here, you are suggested to move to escape.")
	select = ""
	while select not in direction:
		select = input("Please enter only front/back/left/right.")
		if select == "front":
			saferoom5()
		elif select == "back":
			startroom()
		elif select == "left":
			print("There is no door but just wall!")
			saferoom1()
		elif select == "right":
			print("There is no door but just wall!")
			saferoom1()
		else:
			print("Invalid! Please enter only front/back/left/right.")

def saferoom2():
	direction = ["front","back","left","right"]
	print("Now you are in safe room 2, nothing special here, you are suggested to move to escape.")
	select = ""
	while select not in direction:
		select = input("Please enter only front/back/left/right.")
		if select == "front":
			saferoom4()
		elif select == "back":
			print("You are in flammable explosive room and triggered explosives inside, you are dead!")
			restart()
		elif select == "left":
			startroom()
		elif select == "right":
			print("There is no door but just wall!")
			saferoom2()
		else:
			print("Invalid! Please enter only front/back/left/right.")

def saferoom3():
	direction = ["front","back","left","right"]
	print("Now you are in safe room 3, nothing special here, you are suggested to move to escape.")
	select = ""
	while select not in direction:
		select = input("Please enter only front/back/left/right.")
		if select == "front":
			print("You are in lethal beast room and encountered the hungary beast, you are dead!")
			restart()
		elif select == "back":
			print("There is no door but just wall!")
			saferoom3()
		elif select == "left":
			print("You are in evil demon room, the demon took your soul, you are dead!")
			restart()
		elif select == "right":
			startroom()
		else:
			print("Invalid! Please enter only front/back/left/right.")

def saferoom4():
	direction = ["front","back","left","right"]
	print("Now you are in safe room 4, nothing special here, you are suggested to move to escape.")
	select = ""
	while select not in direction:
		select = input("Please enter only front/back/left/right.")
		if select == "front":
			print("You are in dragon room, dragon threw a fire ball on you, you are dead!")
			restart()
		elif select == "back":
			saferoom2()
		elif select == "left":
			print("There is no door but just wall!")
			saferoom4()
		elif select == "right":
			print("You are in lethal gas room and cannot stand the air here, you are dead!")
			restart()
		else:
			print("Invalid! Please enter only front/back/left/right.")

def saferoom5():
	direction = ["front","back","left","right"]
	print("Now you are in safe room 5, nothing special here, you are suggested to move to escape.")
	select = ""
	while select not in direction:
		select = input("Please enter only front/back/left/right.")
		if select == "front":
			print("Congratulations, you have found the exit and become free!")
			restart()
		elif select == "back":
			saferoom1()
		elif select == "left":
			print("There is no door but just wall!")
			saferoom5()
		elif select == "right":
			print("You are in dragon room, dragon threw a fire ball on you, you are dead!")
			restart()
		else:
			print("Invalid! Please enter only front/back/left/right.")

def restart():
	choice = ["yes", "no"]
	print ("Game is over, would you like to restart it?")
	select = ""
	while select not in choice:
		select = input("Please only enter yes/no.")
		if select == "yes":
			startroom()
		elif select == "no":
			print("Thank you for playing, goodbye!")
			exit()
		else:
			print("Invalid input!")

while True:
	print("Welcome to Basic Adventure Game!")
	print("You are now lost in a dungeon maze. You have to find your own way out or you will stay here forever!")
	startroom()