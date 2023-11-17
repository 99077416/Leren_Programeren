from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:


for a in range(0,7):
    robotArm.moveRight()


for a in range(0,7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()