print("Welcome to my computer quiz!")


playing=input("Do you want to play?")
if playing.lower( ) != "yes":
    quit()

print("okay! Let's play :)")
score=0
answer=input("WHat does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("WHat does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("WHat does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("WHat does PsU stands for? ")
if answer.lower()=="power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("you got " + str(score) + " question correct !")
print("you got " + str((score/4)*100) + " %.")