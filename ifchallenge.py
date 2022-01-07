name = (input("What's your name?: "))
age = int(input("How old are you {} ?: ".format(name)))

if 18 <= age < 31:
    print("Welcome to your holiday!")
else:
    print("Sorry but you're not allowed")