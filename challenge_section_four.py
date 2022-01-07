available_options = "1, 2, 3, 4, 5"

option = input("Please choose your option from the list below:"
               "\n1. Minecraft\n2. Fortnite\n3. Studying\n4. Walking"
               "\n5. Exercising\nType 0 to exit\nUse numbers only: ")

if option in available_options:
    print("You chose {} as your hobby for today!!".format(option))

while option not in available_options:

    if option == 0:
        break
