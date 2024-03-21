from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
x = 2
for i in range(4):

    robotArm.grab()
    for i in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(x):
        robotArm.moveLeft()
    x+=2
        

# Na jouw code wachten tot het sluiten van de window: 
robotArm.wait()