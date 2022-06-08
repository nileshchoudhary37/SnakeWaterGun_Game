#####......Snack Water Gun......GAME...........#####
#..................................................#
import random

def FindWinner(u,comp):
    if u==1 and comp==2:
        op="You Win!"
    elif u==1 and comp==3:
        op="You Loose!"
    elif u==2 and comp==1:
        op="You Loose!"
    elif u==2 and comp==3:
        op="You Win!"
    elif u==3 and comp==1:
        op="You Win!"
    elif u==3 and comp==2:
        op="You Loose!"
    else:
        op="tie!"
    return op
    
    

#Here assumption: s =1 ,w =2, g =3 
res="tie!"
while res=="tie!":
 randNo=random.randint(1,3)
 print("Computer's Turn:Snake(s ) , Water(w ) or Gun(g )")
 ch=input("Your's Turn:Snake(s ) , Water(w ) or Gun(g ) ?")
 if ch=='s':
  res=FindWinner(1,randNo)
 elif ch=='w':
  res=FindWinner(2,randNo)
 else:
  res=FindWinner(3,randNo)
 print(res)
 #####......................................................#
