import random

cube = [

    [
        ['r','r','r'],
        ['r','r','r'],
        ['r','r','r']
    ],
    [
        ['b','b','b'],
        ['b','b','b'],
        ['b','b','b']
    ],

    [
        ['g','g','g'],
        ['g','g','g'],
        ['g','g','g']
    ],

    [
        ['w','w','w'],
        ['w','w','w'],
        ['w','w','w']
    ],
    [
        ['b','b','b'],
        ['b','b','b'],
        ['b','b','b']
    ],
    [
        ['y','y','y'],
        ['y','y','y'],
        ['y','y','y']
    ],
]

def printCube():
    for i in cube[0]:
        print('              ', i, end=' \n')

    for i in range(3):
        print(cube[1][i], end='')
        print(cube[2][i], end='')
        print(cube[3][i], end='')
        print(cube[5][i])

    for i in cube[4]:
        print('              ', i, end=' \n')

def getCube(i):
    return cube[i]



def rotateTopRight():
    temp = cube[5][0];

    #Rotates cube[i][0]
    cube[5][0] = cube[3][0]
    cube[3][0] = cube[2][0]
    cube[2][0] = cube[1][0]
    cube[1][0] = temp

    #Rotating cube[0] to fit
    tempCube1 = cube[0][0][0]
    tempCube2 = cube[0][0][1]

    cube[0][0][0] = cube[0][0][2]
    cube[0][0][1] = cube[0][1][2]
    cube[0][0][2] = cube[0][2][2]

    cube[0][1][2] = cube[0][2][1]
    cube[0][2][2] = cube[0][2][0]

    cube[0][2][1] = cube[0][1][0]
    cube[0][2][0] = tempCube1
    cube[0][1][0] = tempCube2

def rotateTopLeft():
    temp = cube[1][0]

    #Rotates cube[i][0]
    cube[1][0] = cube[2][0]
    cube[2][0] = cube[3][0]
    cube[3][0] = cube[5][0]
    cube[5][0] = temp

    #Rotating cube[0] to fit
    tempCube = cube[0][0][0]

    cube[0][0][0] = cube[0][2][0]
    cube[0][2][0] = cube[0][2][2]
    cube[0][2][2] = cube[0][0][2]
    cube[0][0][2] = tempCube

    tempCube2 = cube[0][0][1]

    cube[0][0][1] = cube[0][1][0]
    cube[0][1][0] = cube[0][2][1]
    cube[0][2][1] = tempCube2
    cube[0][2][2] = cube[0][2][2]

    tempCube = cube[0][1][2]

    cube[0][1][2] = cube[0][2][1]
    cube[0][2][1] = tempCube


def rotateMidRight():
    temp = cube[5][1]

    cube[5][1] = cube[3][1]
    cube[3][1] = cube[2][1]
    cube[2][1] = cube[1][1]
    cube[1][1] = temp

def rotateMidLeft():
    temp = cube[1][1]

    cube[1][1] = cube[2][1]
    cube[2][1] = cube[3][1]
    cube[3][1] = cube[5][1]
    cube[5][1] = temp


def rotateBotRight():
    temp = cube[5][2]

    #Rotating Cube
    cube[5][2] = cube[3][2]
    cube[3][2] = cube[2][2]
    cube[2][2] = cube[1][2]
    cube[1][2] = temp


    #Rotating cube[4] to fit
    tempCube = cube[4][0][0]

    cube[4][0][0] = cube[4][2][0]
    cube[4][2][0] = cube[4][2][2]
    cube[4][2][2] = cube[4][0][2]
    cube[4][0][2] = tempCube

    tempCube2 = cube[0][0][1]

    cube[4][0][1] = cube[4][1][0]
    cube[4][1][0] = cube[4][2][1]
    cube[4][2][1] = tempCube2
    cube[4][2][2] = cube[4][2][2]

    tempCube = cube[4][1][2]

    cube[4][1][2] = cube[4][2][1]
    cube[4][2][1] = tempCube

def rotateBotLeft():
    temp = cube[1][2]

    cube[1][2] = cube[2][2]
    cube[2][2] = cube[3][2]
    cube[3][2] = cube[5][2]
    cube[5][2] = temp

    #Rotating cube[4] to fit
    tempCube1 = cube[4][0][0]
    tempCube2 = cube[4][0][1]

    cube[4][0][0] = cube[4][0][2]
    cube[4][0][1] = cube[4][1][2]
    cube[4][0][2] = cube[4][2][2]

    cube[4][1][2] = cube[4][2][1]
    cube[4][2][2] = cube[4][2][0]

    cube[4][2][1] = cube[4][1][0]
    cube[4][2][0] = tempCube1
    cube[4][1][0] = tempCube2


def rotateMidUp():
    temp1 = cube[0][0][1]
    temp2 = cube[0][1][1]
    temp3 = cube[0][2][1]

    cube[0][0][1] = cube[2][0][1]
    cube[0][1][1] = cube[2][1][1]
    cube[0][2][1] = cube[2][2][1]

    cube[2][0][1] = cube[4][0][1]
    cube[2][1][1] = cube[4][1][1]
    cube[2][2][1] = cube[4][2][1]

    cube[4][0][1] = cube[5][2][1]
    cube[4][1][1] = cube[5][1][1]
    cube[4][2][1] = cube[5][0][1]

    cube[5][2][1] = temp1
    cube[5][1][1] = temp2
    cube[5][0][1] = temp3

def rotateMidDown():
    temp1 = cube[0][0][1]
    temp2 = cube[0][1][1]
    temp3 = cube[0][2][1]

    cube[0][0][1] = cube[5][2][1]
    cube[0][1][1] = cube[5][1][1]
    cube[0][2][1] = cube[5][0][1]

    cube[5][2][1] = cube[4][0][1]
    cube[5][1][1] = cube[4][1][1]
    cube[5][0][1] = cube[4][2][1]

    cube[4][0][1] = cube[2][0][1]
    cube[4][1][1] = cube[2][1][1]
    cube[4][2][1] = cube[2][2][1]

    cube[2][0][1] = temp1
    cube[2][1][1] = temp2
    cube[2][2][1] = temp3



def shuffle(i):
    
    for x in range(i):
        rd = random.randint(0, 7)
        print(rd)
        if rd == 0:
            rotateTopRight()
        elif rd == 1:
            rotateTopLeft()
        elif rd == 2:
            rotateMidRight()
        elif rd == 3:
            rotateMidLeft()
        elif rd == 4:
            rotateBotRight()
        elif rd == 5:
            rotateBotLeft()
        elif rd == 6:
            rotateMidUp()
        elif rd == 7:
            rotateMidDown()

