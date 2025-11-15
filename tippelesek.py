import random
# def haromrobotegyszer():
#     szam = random.randint(1,10)
#     robot1 = random.randint(1,10)
#     robot2 = random.randint(1, 10)
#     robot3 = random.randint(1, 10)
#
#     eltalalta = ""
#     eltszam = 0
#
#     if robot1 == szam:
#         eltalalta += "1.robot"
#         eltszam +=1
#
#     if robot2 == szam:
#         eltalalta+= "2.robot"
#         eltszam +=1
#
#     if robot3 == szam:
#         eltalalta+= "3.robot"
#         eltszam +=1
#
#
#     if eltszam == 0:
#         print("Nem")
#     elif eltszam <3:
#         print("eltalálták: ", eltalalta)
#     else:
#         print("mind")


def egyrobotharomtipp():
    szam = random.randint(1,10)
    robot = random.randint(1,10)
    if robot == szam:
        print("Elsőre")
    elif robot == random.randint(1,10):
        if robot == szam:
            print("Másodjára")
        elif robot == random.randint(1,10):
            if robot == szam:
                print("Harmadjára")
            else:
                print("Nem sikerült :p")
    else:
        print("Nem sikerült :p")