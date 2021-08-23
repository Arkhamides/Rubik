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
        ['o','o','o'],
        ['o','o','o'],
        ['o','o','o']
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
        print(cube[3][i])

    for i in cube[4]:
        print('              ', i, end=' \n')

    for i in cube[5]:
        print('                              ', i, end=' \n')

printCube()