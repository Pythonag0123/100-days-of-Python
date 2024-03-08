import random
paper='''   _______
        ---'   ____)____
                  ______)
                 _______)
                ________)
        ---.___________)'''
scissor='''
            _______
        ---'   ____)____
                ________)
              ___________)
            (_____)
      ---.__(____) '''
rock='''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)'''
lis=[paper,rock,scissor]
User_Choice=int(input("ENTER YOUR CHOICE:0 for paper,1 for rock and 2 for scissors"))
if User_Choice==0:
    print(paper)
elif User_Choice==1:
    print(rock)
elif User_Choice==2:
    print(scissor)
Computer_Choice=random.choice(lis)
print(Computer_Choice)
if User_Choice == 0 and Computer_Choice == rock:
    print("You won!")
elif User_Choice == 1 and Computer_Choice == scissor:
    print("You won!")
elif User_Choice == 2 and Computer_Choice == paper:
    print("You won!")
elif User_Choice == 0 and Computer_Choice == scissor:
    print("You lose!")
elif User_Choice == 1 and Computer_Choice == paper:
    print("You lose!")
elif User_Choice == 2 and Computer_Choice == rock:
    print("You lose!")
else:
    print("It's a tie!")
   

            
    
