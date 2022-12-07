import random as r

snake={67:5,32:10,98:2,54:44,72:66,92:83,42:19,22:8}
ladder={55:95,32:10,1:20,5:23,40:56,65:3,42:90,80:99}
#p indicates positon of player
p1=0
p2=0
def move(p):
     dice=r.randint(1,6)
     print(f"dice:{dice}")
     p+=dice
     if p in snake:
         print("\t snake bite \t")
         p=snake[p]
         print("position is:",p)
     elif p in ladder:
        print("climbing ladder")
        p=ladder[p]
        print("position is:",p)
         
     else:
        print("position is:",p)
     print("\n")
     return p
while True:
    a=(input("player 1 roll the dice \"a\":"))
    p1=move(p1)
    if p1>=100:
        print("game over \n player 1 won the game!!!")
        break
    b=(input("player 2 roll the dice \"b\":"))
    p2=move(p2)
    if p2>=100:
        print("game over \n player 2 won the game!!!")
        break
    
