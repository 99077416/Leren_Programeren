from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

x=1
y=0

for i in range(4):
     c = 0
     for z in range(x):
          robotArm.grab()
          for i in range(5):
               robotArm.moveRight()
          robotArm.drop()
          c+=1
          if c == 4:
               break
          if z == y:
               for i in range(4):
                    robotArm.moveLeft()
          else:
               for i in range(5):
                    robotArm.moveLeft()
     y+=1
     x+=1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()