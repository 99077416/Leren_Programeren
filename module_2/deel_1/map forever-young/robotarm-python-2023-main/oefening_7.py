from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

for i in range(5):
    for a in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if i < 4:
        for a in range(0,2):
            robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
