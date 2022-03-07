# if second_direction == 'North':
    # print("You found an abandoned campfire!")
   # print("Nearby a tree you found a bucket")
    # return_previous = input("Do you want to go back? Type 'x' to go back or "
          #                  "choose one direction:\nNorth\nEast\nWest\nSouth\n")
# if return_previous == 'x':
    # print("You returned to your starting location")
# elif return_previous == 'North':
    # print("You cannot go there, there's too many snakes")

# Start of the game

print("You are in a forest")
print("Your mission is to obtain all the objects needed and to kill the dragon.")
print("The objects needed are as follows:\nWater Bucket\nKey\nMagical Sword\nRevolver\nBullets")

direction = input("Choose one direction:\nNorth\nEast\nWest\nSouth\n")
objects = ['Water Bucket', 'Key', 'Magical Sword', 'Revolver', 'Bullets']
objects_needed = ['']
total_objects = 5
corridor_choice = ''
if direction == "North":
    print("You are still in a forest")
elif direction == "East":
    print("You're at the sword's location, you need the water bucket to take the sword out though.")
    if "Water Bucket" in objects_needed:
        print("You use the water to dissolve the rock and you take out the sword from the mud")
        objects_needed = objects_needed + ['Magical Sword']
        objects_needed =  objects_needed.remove("Water Bucket")
    print("If you wish to go back, press 'x'")
elif direction == "West":
    print("You found a wild west house")
    print("You find some bullets and a gun on a chair nearby")
    print("You pick up the gun with the bullets and instantly go back")
    print("You're back to your original location")
    print("The West is off limits for you now")
elif direction == 'South':
    print("You found a castle and you enter to try and find the key")
    print("There's three corridors:")
    corridor_choice = input("Do you wish to go Left, Right or Center?: ")
