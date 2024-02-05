from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

#Jouw python instructies zet je vanaf hier:
x = 9
for i in range(5):

    robotArm.grab()
    for i in range(x):
        robotArm.moveRight()
    robotArm.drop()
    x-=1
    for x in range(x):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()