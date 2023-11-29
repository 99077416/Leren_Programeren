from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

for a in range(0,4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()


robotArm.moveRight()

for a in range(0,4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()