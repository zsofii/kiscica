name = input("Tell me your name: ")
print("Hello", name)

Value = int(input("Type a number between 1 and 10: "))
if (Value > 0) and (Value <= 10):
    print("You typed: ", Value)
else:
    print("The value you typed is incorrect!")

Value = input("Type less than 6 characters: ")
LetterNum = 1
for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
    if LetterNum > 6:
        print("The string is too long!")
        break

"""
print("1. Eggs")
print("2. Pancakes")
print("3. Waffles")
print("4. Oatmeal")
MainChoice = int(input("Choose a breakfast item: "))
if (MainChoice == 2):
    Meal = "Pancakes"
elif (MainChoice == 3):
    Meal = "Waffles"
if (MainChoice == 1):
    print("1. Wheat Toast")
    print("2. Sour Dough")
    print("3. Rye Toast")
    print("4. Pancakes")
    Bread = int(input("Choose a type of bread: "))
    if (Bread == 1):
        print("You chose eggs with wheat toast.")
    elif (Bread == 2):
        print("You chose eggs with sour dough.")
    elif (Bread == 3):
        print("You chose eggs with rye toast.")
    elif (Bread == 4):
        print("You chose eggs with pancakes.")
    else:
        print("We have eggs, but not that kind of bread.")

elif (MainChoice == 2) or (MainChoice == 3):
    print("1. Syrup")
    print("2. Strawberries")
    print("3. Powdered Sugar")
    Topping = int(input("Choose a topping: "))
    if (Topping == 1):
        print ("You chose " + Meal + " with syrup.")
    elif (Topping == 2):
        print ("You chose " + Meal + " with strawberries.")
    elif (Topping == 3):
        print ("You chose " + Meal + " with powdered sugar.")
    else:
        print ("We have " + Meal + ", but not thattopping.")

elif (MainChoice == 4):
    print("You chose oatmeal.")

else:
    print("We don't serve that breakfast item!")
 
"""