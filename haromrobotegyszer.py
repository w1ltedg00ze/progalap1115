import random
def haromrobotegyszer():
    szam = random.randint(1,10)
    robot1 = random.randint(1,10)
    robot2 = random.randint(1, 10)
    robot3 = random.randint(1, 10)

    eltalalta = ""

    if robot1 == szam:
        eltalalta += "1.robot"

    if robot2 == szam:
        eltalalta+= "2.robot"

    if robot3 == szam:
        eltalalta+= "3.robot"
    print("eltalálták: ", eltalalta)