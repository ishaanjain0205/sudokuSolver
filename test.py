import numpy as np

file = open("test_cases.txt", "r")
lines = file.readlines()

gameboard = np.array([[0,2,3],[4,5,6],[7,8,9]])

print(len(gameboard))

for i in range (0,3):
    print(i)

print(print(5/3))

def check_box(gameboard, row, col, num):

    #DETERMINE WHICH 3x3 box piece is being placed in

    boxRow = row // 3
    boxCol = col // 3

    for r in range(boxRow * 3, boxRow * 3 + 3):
        for c in range(boxCol * 3, boxCol * 3 + 3):
            if gameboard[r][c] != num:
                possible = True
            else:
                possible  = False
                break
    

def check_col(gameboard, col, num):
    possible = False
    for row in range(len(gameboard)):
        if gameboard[row][col] != num:
            possible = True
        else:
            possible = False
            break
    return possible

#print(check_col(gameboard, 2, 6))



def check_row(gameboard, row, num):
    possible = False
    for col in range(len(gameboard[row])):
        if gameboard[row][col] != num:
            possible = True
        else:
            possible = False
            break
    return possible

#print(check_row(gameboard, 0, 5))
