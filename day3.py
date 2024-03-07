#day3-project3
print("Welcome to the treasure island!\nYour mission is to find the treasure")
dir1=input("You are at the cross road.Where do you wanna go?'Left' or 'right'?").lower().strip()
if dir1=="left":
    dir2=input("You have arrived a lake ,there is an island.Do wanna 'wait' for boat or 'swim' across?").lower().strip()
    if dir2=="wait":
        choice=input("You have reached the island safely ,now here is a house with three doors,RED,YELLOW or BLUE .Choose one.").lower().strip()
        if choice=="blue":
            print("Congo you have won the game!!!")
        else:
            print("Game over")
    else:
        print("Game Over")
else:
    print("Game Over")


    
