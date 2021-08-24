
import cube

x = ""
WrongInput = False


while x != "q":

    if WrongInput == False:
        cube.printCube()

    print("1 - rotateTopRight")
    print("2 - rotateTopLeft")
    print("3 - rotateMidRight")
    print("4 - rotateMidLeft")
    print("5 - rotateBotRight")
    print("6 - rotateBotLeft")
    print("7 - rotateMidUp")
    print("8 - rotateMidDown")

    print(" Your Input:  ")
    x = input()

    if x == "1":
        cube.rotateTopRight()
    elif x == "2":
        cube.rotateTopLeft()
    elif x == "3":
        cube.rotateMidRight()
    elif x == "4":
        cube.rotateMidLeft()
    elif x == "5":
        cube.rotateBotRight()
    elif x == "6":
        cube.rotateBotLeft()
    elif x == "7":
        cube.rotateMidUp()
    elif x == "8":
        cube.rotateMidDown()
    elif x!="q":
        WrongInput = True
