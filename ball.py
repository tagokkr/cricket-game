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

batTeam = indTeam
bowlTeam = engTeam

no = 0  #over number
def over ():
    global no
    no = no + 1
    print ("England's Bowlers:")
    print ("")
    for i in range (6, 12):
        print (str(i) + ". " + (bowlTeam [i-1]) + " - " + (engBowl [i-6]))
    print ("")
    bowlerChoice = int(input("Choose a bowler to bowl the upcoming over. Select a number between 6 and 11: "))
    while bowlerChoice < 6 or bowlerChoice > 11:
        bowlerChoice = int(input("Invalid choice. Please choose a number between 6 and 11: "))
    bowlerChoice = bowlerChoice - 1
    style = bowlerChoice - 5
    print ("")
    print (engTeam [bowlerChoice] + " comes into the attack to bowl over " + str(no) + ". (Bowling style: " + engBowl [style] + ")")
    print ("")
    for i in range (6):
        if engBowl [style] == "fast":
            ballTypes = ["quick ball", "outswinger", "inswinger", "cutter", "slower ball", "yorker", "bouncer"]
            ballBowled = random.choices(ballTypes, weights = [45, 10, 15, 10, 10, 5, 5], k=1)
            if ballBowled[0] == "slower ball":
                ballSpeed = random.randint (110, 125)
            else: 
                ballSpeed = random.randint (135, 150)
            #print (ballBowled[0])
        
        elif engBowl [style] == "medium fast":
            ballTypes = ["outswinger", "inswinger", "cutter", "slower ball", "yorker"]
            ballBowled = random.choices(ballTypes, weights = [35, 25, 25, 10, 5], k=1)
            #print (ballBowled[0])
            if ballBowled[0] == "slower ball":
                ballSpeed = random.randint (105, 115)
            else: 
                ballSpeed = random.randint (125, 135)
        
        elif engBowl [style] == "offbreak":
            ballTypes = ["offspin", "arm ball", "doosra", "topspin"]
            ballBowled = random.choices(ballTypes, weights = [50, 30, 15, 5], k=1)
            ballSpeed = random.randint (80, 95)
            #print (ballBowled[0])
        
        elif engBowl [style] == "legbreak": 
            ballTypes = ["legspin", "googly", "topspin"]
            ballBowled = random.choices(ballTypes, weights = [45, 35, 20], k=1)
            ballSpeed = random.randint (80, 90)
            #print (ballBowled[0])      
        
        elif engBowl [style] == "slow left arm":
            ballTypes = ["offspin", "arm ball", "topspin"]
            ballBowled = random.choices(ballTypes, weights = [50, 25, 25], k=1)
            ballSpeed = random.randint (75, 90)
            #print (ballBowled[0])
        print ()
        print ((engTeam[bowlerChoice]) + ": " + (ballBowled[0]) + " at " + str(ballSpeed)  + " kmph")
        time.sleep (2)
        #ball()
    #ball is bowled 6 times in the over


def ball(style):
    if engBowl [style] == "fast":
        ballTypes = ["quick ball", "outswinger", "inswinger", "cutter", "slower ball", "yorker", "bouncer"]
        ballBowled = random.choices(ballTypes, weights = [45, 10, 15, 10, 10, 5, 5], k=1)
        if ballBowled[0] == "slower ball":
            ballSpeed = random.randint (110, 125)
        else: 
            ballSpeed = random.randint (135, 150)
        print (ballBowled[0])
    
    elif engBowl [style] == "medium fast":
        ballTypes = ["outswinger", "inswinger", "cutter", "slower ball", "yorker"]
        ballBowled = random.choices(ballTypes, weights = [35, 25, 25, 10, 5], k=1)
        print (ballBowled[0]) 
    
    elif engBowl [style] == "offbreak":
        ballTypes = ["offspin", "arm ball", "doosra", "topspin"]
        ballBowled = random.choices(ballTypes, weights = [50, 30, 15, 5], k=1)
        print (ballBowled[0])
    
    elif engBowl [style] == "legbreak": 
        ballTypes = ["legspin", "googly", "topspin"]
        ballBowled = random.choices(ballTypes, weights = [45, 35, 20], k=1)
        print (ballBowled[0])      
    
    elif engBowl [style] == "slow left arm":
        ballTypes = ["offspin", "arm ball", "topspin"]
        ballBowled = random.choices(ballTypes, weights = [50, 25, 25], k=1)
        print (ballBowled[0])
    
   

def innings():
    for index in range (20):  #20 overs
        over()


innings()

