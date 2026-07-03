import random 

print("===============================")
print("Welcome to the Realm! 🌟")
print("===============================")
name = input("What is your name, brave adventurer? ").strip().lower()



strength = 20
health = 20

print(f"\nWelcome, {name}! 🧙")
print(f"You are a brave adventurer with {strength} strength and {health} health.\n")
print("You come from a poor family in a small village. 🏡")
print("You must collect apples to help your family survive the harsh winter. 🍎")
print("The forest is full of dangerous creatures and obstacles. 🌲")
print("You must navigate the forest, gather apples, and return home safely. 🛣️\n")
print("There are animals and forest dwellers waiting to eat your apples and YOU! 🐺")
print("Your mother gives you 3 potions to choose from. 🧪")
print("Each potion changes your strength and health in a different way. ✨\n")
print("1. The warrior potion: gives you +5 strength but -5 health ⚔️")
print("2. The woodcutter potion: gives you +5 health but -5 strength 🪓")
print("3. The quiet walker potion: gives you -3 strength and +3 health 👣")

choice = ""

while choice not in ["1", "2", "3"]:
    choice = input("Which potion do you choose? (1, 2, or 3): ")
    print("----------------\n---------------------\n")

    if choice == "1":
        strength += 5
        health -= 5
        print(f"You chose the warrior potion! Your strength is now {strength} and your health is now {health}.")
    elif choice == "2":
        strength -= 5
        health += 5
        print(f"You chose the woodcutter potion! Your strength is now {strength} and your health is now {health}.")
    elif choice == "3":
        strength -= 3
        health += 3
        print(f"You chose the quiet walker potion! Your strength is now {strength} and your health is now {health}.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        print("Your strength and health remain the same.")





apples = 0
print("Let's go to the forest! 🌲")

print("---------------------------------------")
print("You are walking through the forest when you hear a rustling in the bushes. 🌳")
print("A wild boar! 🐗 It looks angry and is charging towards you!")

action = input("What do you want to do? Enter: fight, run or hide ").strip().lower()

if action == "fight":
    if strength > 15:
        print("You fought bravely and defeated the boar! 🏆")
        health -= 5
    else:
        print("You tried to fight the boar but it was too strong! 😢")
        health -= 10
elif action == "run":
    print("You ran away safely, but you dropped some apples. 🍎")
    health -= 2
elif action == "hide":
    print("You hid behind a tree and the boar ran away. 🏃‍♂️")
    health -= 1
else:
    print("Invalid action. You hesitated and the boar attacked you! 😱")
    health -= 10

print(f"Your health is now {health}.")

print("You continue your journey through the forest and find a clearing with a beautiful apple tree. 🍏")
print("But the apples are too high to reach. You need to find a way to get them down.")
action2 = input("What do you want to do? Enter: climb, shake or use your sword ").strip().lower()

if action2 == "climb":
    if strength > 15:
        print("You climbed the tree and picked some apples! 🍎")
        health -= 2
        apples += 5
    else:
        print("You tried to climb the tree but fell and got injured! 😢")
        health -= 10
elif action2 == "shake":
    print("You shook the tree and some apples fell down! 🍏")
    health -= 1
    apples += 3
elif action2 == "use your sword":
    print("You used your sword to cut down some apples! 🍎")
    health -= 3
    apples += 4
else:
    print("Invalid action. You stood still and missed your chance. 😅")

print(f"Your health is now {health}.")
print(f"You have {apples} apples.")

print("BONUS: YOU FOUND SOMETHING.")

list = ["A magical sword! 🗡️", "15 gold coins! 💰", "A treasure map! 🗺️"]

bonus_item = random.choice(list)
print(f"You found a {bonus_item}!")

print("You continue your journey through the forest and find a clearing with a beautiful apple tree. 🍏")
print("But it is inhaitated with a monkey! 🐒 The monkey is guarding the apples and looks very angry!")
print("The monkey is very strong and will attack you if you try to take the apples.")
action3 = input("What do you want to do? Enter: fight , talk to the monkey or move forward ").strip().lower()

if action3 == "fight":
    if strength > 10:
        print("You fought bravely and defeated the monkey! 🏆")
        health -= 5
        apples += 5
    else:
        print("You tried to fight the monkey but it was too strong! 😢")
        health -= 10
elif action3 == "talk to the monkey":
    print("You tried to talk to the monkey but it didn't understand you. 😅")
    print("But it attacked you with 3 apples! 🍎🍎🍎")
    apples += 3
    health -= 1
elif action3 == "move forward":
    print("You decided to move forward and avoid the monkey.")
    health -= 2


print(f"Your health is now {health}.")
print(f"You have {apples} apples.")

print("It getting darker and you must return home before it gets dark. 🌅")

print("you decide to take a shortcut through the forest. 🌲")
print("But the shortcut is full of dangerous creatures and obstacles. 🐍")
print("And you run into a man? He looks like a wizard! 🧙‍♂️")
print("No! he is a forest dweller! He looks very angry and is blocking your path. 😡")
print("he is eyeing your apples!")
print("what do you do?")
action4 = input("Enter: fight, run or talk to the forest dweller ").strip().lower()

if action4 == "fight":
    if strength > 10:
        print("You fought bravely and defeated the forest dweller! 🏆")
        health -= 5
    else:
        print("You tried to fight the forest dweller but it was too strong! 😢")
        health -= 10
        apples -= 3
elif action4 == "run":
    print("You ran away safely, but you dropped some apples. 🍎")
    health -= 2
    apples -= 2
elif action4 == "talk to the forest dweller":
    print("You tried to talk to the forest dweller and he understood you. 😅")
    print("he let you pass and even gave yousome of his apples! 🍎🍎🍎")
    apples += 3
    health -= 1


print("you sit down under a tree and rest for a while.  🌳  ")
print("you start counting your apples ")
if apples >= 10:
    print(f"You have {apples} apples!")
    print("You have enough apples to help your family survive the harsh winter! ❄️")
else : 
    print(f"You have {apples} apples!")
    print("You don't have enough apples to help your family survive the harsh winter. 😢")

   
    

cont = input("do you want to continue your apples journey or go home?\n enter continue or home: ").strip().lower()

if cont == "continue":
    print("You decide to continue your journey.")
    print("You continue your journey through the forest and find a clearing with a beautiful apple tree. 🍏")
    print("you decide you will get as many apples you can and head home since it is dark.")
    print("as you climb the tree , you find a nest with a baby bird! 🐦")
    print("awww! you say but the mother attack you with her beak.")
    print("you try to fight her off but she is too strong! 😢")
    action5 = input("What do you want to do? Enter: fight, run or talk to the mother bird ").strip().lower()
    if action5 == "fight":
        if strength > 10:
            print("You fought bravely and defeated the mother bird! 🏆")
            health -= 5
            apples += 5
        else:
            print("You tried to fight the mother bird but it was too strong! 😢")
            health -= 10
    elif action5 == "run":
        print("You ran away safely, but you dropped some apples. 🍎")
        health -= 2
        apples -= 2
    elif action5 == "talk to the mother bird":
        print("You tried to talk to the mother bird and she understood you. 😅")
        print("she let you pass and you collect 6 apples! 🍎🍎🍎")
        apples += 6
        health -= 1

        print("you climb down the tree and head home with your apples. 🏡")
        print("Your family is very happy to see you and your apples. 🍎")
        print(f"You have {apples} apples!")
    if apples >= 10:
        print(f"You have {apples} apples!")
        print("You have enough apples to help your family survive the harsh winter! ❄️")
        print("You continue your journey to home.")
        print("You finally reach home safely with your apples. 🏡")
        print("You won the game")
    else:
        print(f"You have {apples} apples!")
        print("You don't have enough apples to help your family survive the harsh winter. 😢")
        print("You continue your journey to home.")
        print("You finally reach home safely with your apples. 🏡")
        print("you lost the game. ")

elif cont == "home":
    print("You decide to go home.")
    print("You return home safely with your apples. 🏡")
    print("Your family is very happy to see you and your apples. 🍎")
    if apples >= 10:
        print("You have enough apples to help your family survive the harsh winter! ❄️")
        print("You won the game")
    else:
        print("You don't have enough apples to help your family survive the harsh winter. 😢")
        print("You lost the game. ")
