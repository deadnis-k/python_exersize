age = int(input("what is your age? "))
answer = input("are you a student? (y/n) ")
if answer == "y":
    studant= True
else:
    studant= False


if age < 18 or studant == True:
    print("you get a discount")
else:
    print("you pay full price")
