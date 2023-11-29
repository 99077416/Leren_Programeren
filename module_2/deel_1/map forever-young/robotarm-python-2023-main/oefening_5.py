from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2

for a in range(0,7):
    robotArm.moveRight()


for a in range(0,8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if a < 7:
        robotArm.moveLeft()
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()