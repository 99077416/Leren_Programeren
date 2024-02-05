from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

robotArm.moveRight()

for i in range(7):
    robotArm.grab()
    for a in range(8):
        robotArm.moveRight()
    robotArm.drop()
    if i < 6:
        for i in range(0,8):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()