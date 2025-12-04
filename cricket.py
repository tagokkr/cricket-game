import random
import time

indTeam = ["Rohit Sharma", "Shubman Gill", "Virat Kohli", "Shreyas Iyer", "KL Rahul",
            "Axar Patel", "Hardik Pandya", "Washington Sundar", "Harshit Rana",
            "Jasprit Bumrah", "Mohammed Siraj"]

engTeam = ["Jamie Smith", "Ben Duckett", "Joe Root", "Harry Brook", "Jos Buttler",
            "Jacob Bethell", "Will Jacks", "Jamie Overton", "Brydon Carse",
            "Jofra Archer", "Adil Rashid"]

indBowl = ["slow left arm", "medium fast", "offbreak", "fast", "fast", "fast"]
engBowl = ["slow left arm", "offbreak", "fast", "fast", "fast", "legbreak"]

# xBowl [x+5] = xTeam [x]'s bowling style

batTeam = []
bowlTeam = []

call = ""
call2 = ""
tossresult = ""
decision = ""


print ("")
print ("Welcome to the Kia Oval, where England host India for what promises to be a thrilling contest!")
userteam = "i"
#userteam = input("Press 'e' to play as England, and 'i' to play as India. ")
#while userteam != "i" and userteam != "e":
#        print("Please try typing in the team name again.")
#       userteam = input("Press 'e' to play as England, and 'i' to play as India. ")

def xi ():
    if userteam == "i":
        print ("")
        print ("You are playing as India.")
        print ("Here is your playing XI:")
        for x in range (11):
            print (str(x+1) + ". " + (indTeam[x]))
        print ("")
        print ("... and here is England's XI :")
        for x in range (11):
            print (str(x+1) + ". " + (engTeam[x]))
    
    #elif userteam == "e":
    #   print ("")
    #    print ("You are playing as England.")
    #   print ("Here is your playing XI: ")
    #   for x in range (11):
    #       print (str(x+1) + ". " + (engTeam[x]))
    #   print ("")
    #   print ("... and here is India's XI:")
    #   for x in range (11):
    #       print (str(x+1) + ". " + (indTeam[x]))


print ("")
print ("It's time for the toss!")
time.sleep (2)
print ("")
print ("The two captains walk out to the middle...")
print ("Along with the match referee.")
time.sleep (2)
print ("")
print ("Harry Brook flips the coin...")
time.sleep (2)
print ("")
call = input("Rohit calls while the coin is in the air - choose heads or tails (h/t): ")
while call != "h" and call != "t":
    call = input("Invalid call -  choose heads or tails (h/t): ")
if call == "h":
    call = "heads"
elif call == "t":
    call = "tails"
tossresult = random.choice(["heads", "tails"])


print ("")
print ("Rohit calls " + call + ".")
time.sleep (2)
print ("")
print ("The coin falls to the ground...")
time.sleep (2)
print ("")
print ("The coin lands on " + tossresult + "!")
time.sleep (2)

if call == tossresult:
    print ("... meaning that Rohit has called correctly.")
    print ("")
    decision = input ("Press 'a' to bat first, or 'b' to bowl first: ")
    
    while decision != "a" and decision != "b":
        print("Please try typing in your decision again.")
        decision = input ("Press 'a' to bat first, or 'b' to bowl first: ")

    if decision == "a":
        print ("You have elected to bat first.")
        batTeam = indTeam
        bowlTeam = engTeam
        
    elif decision == "b":
        print ("You have elected to bowl first.")
        batTeam = engTeam
        bowlTeam = indTeam

else:
    print ("meaning that the coin falls in favour of Harry Brook and England.")
    oppDecision = random.choice (["a", "b"])
    time.sleep (2)
    print ("")
    if oppDecision == "a":
        print ("England have elected to bat first.")
        batTeam = engTeam
        bowlTeam = indTeam
        
    elif oppDecision == "b":
        print ("England have elected to bowl first.")
        batTeam = indTeam
        bowlTeam = engTeam
        

print ("The match is about to begin.")
print ("")
if batTeam == indTeam:
    print ("The Indian openers, " + indTeam [0] + " and " + indTeam [1] + " walk out to bat.")
elif batTeam == engTeam:
    print ("The English openers " + engTeam [0] + " and " + engTeam [1] + " walk out to bat.")


    

#xi () 

