while True:
    print("Welcome to Yesheng's Mad Libs!")

    adj1 = input("1st adjective")
    adj2 = input("2nd adjective")
    adj3 = input("3rd adjective")
    noun1 = input("1st noun")
    noun2 = input("2nd noun")
    noun3 = input("3rd noun")

    print("Yesheng felt like to buy some new {}. He reached the {} shop by his {} car. He noticed that there are only {} {}. He did not like them and bought {} and {}.". format(noun1,adj1, adj2, adj3, noun1, noun2, noun3))