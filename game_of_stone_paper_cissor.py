import random
p1=0
p2=0

for i in range(1,5):
    list=['stone','paper','scissor']
    user1=input("enter your choice(stone,paper,scissor) Rupak: ").lower()
    user2=random.choice(list)
    print("It is",user1,"vs",user2)
    if user1==user2:
        print("tie! match")
    elif user1=='stone' and user2=="scissor":
        print("match won by user1")
        p1+=1
    elif user1=="stone" and user2=="paper":
        print("match won by user2")
        p2+=1
    elif user1=="paper" and user2=="scissor":
        print("match won by user2")
        p2+=1
    elif user1=="paper" and user2=="stone":
        print("match won by user1")
        p1+=1
    elif user1=="scissor" and user2=="stone":
        print("match won by user2")
        p2+=1
    elif user1=="scissor" and user2=="paper":
        print("match won by user1")
        p1+=1
        
print("user1",p1,"times winner and user2 ",p2,"times winner")
if p1>p2:
    print("Congrulations winner is user1")
else:
    print("Congrulations winner is user2")
