from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

for i in range(8):
        robotArm.moveRight()
for i in range(1,10):
    print(i)
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for _ in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(i):
            robotArm.moveLeft()
    else :
        robotArm.drop()
    if i < 9:
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()