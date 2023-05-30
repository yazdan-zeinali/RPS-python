import random
print("hello welcome to RPS game!")
yourscore,systemscore=0,0
while True:
    yourchoice=input("rock(1) or paper(2) or scissor(3) or end game(4) :")
    systemchoice=random.randint(1,3) 
    if yourchoice=="1" and systemchoice==1:
        print("system choice:rock")
        print("equal this time!")
        print(f"{yourscore}-{systemscore}")
    elif yourchoice=="1"and systemchoice == 2:
        systemscore += 1
        print("system choice : paper")
        print("system win this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "1" and systemchoice == 3:
        yourscore += 1
        print("system choice : scissor")
        print("you win this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "2" and systemchoice == 1:
        yourscore += 1
        print("system choice : rock")
        print("you win this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "2" and systemchoice == 2:
        print("system choice : paper")
        print("equal this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "2" and systemchoice == 3:
        systemscore += 1
        print("system choice : scissor")
        print("system win this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "3" and systemchoice == 1:
        systemscore += 1
        print("system choice : rock")
        print("system win this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "3" and systemchoice == 2:
        yourscore += 1
        print("system choice : paper")
        print("you win this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "3" and systemchoice == 3:
        print("system choice : scissor")
        print("equal this time!")
        print(f"{yourscore} - {systemscore}")
    elif yourchoice == "4":
        print("good luck! ")
        break
    else:
        print("please enter correct number!")
if yourscore > systemscore:
    print("you win!")
elif yourscore < systemscore:
    print("system win!")
else:
    print("Equal")
print(f"Your score : {yourscore}\nSystem score : {systemscore}")
      