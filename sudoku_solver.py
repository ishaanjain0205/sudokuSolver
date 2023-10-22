import numpy as np

#Open and turn file into array
file = open("test_cases.txt", "r")
lines = file.readlines()

gameboard = np.full((9,9), 0)

#Sets game board with test case 
for row in range(9):
    for col in range(9):
        gameboard[row][col] = int(lines[row][col])

#function to print formatted gameboard
def printGameboard(gameboard):
    for row in range(9):
        if row == 3 or row == 6:
            print("_____________________")
            print()
        for col in range(9):
            if col == 3 or col == 6:
                print("|", end = " ")
            if gameboard[row][col] == 0:
                print(" ", end = " ")
            else:
                print(gameboard[row][col], end = " ")
        print()


#Is given num able to fit in selected spot
def possible(row, col, num):
    global gameboard

    #check row
    for r in range(9):
        if gameboard[r][col] == num:
            return False
            
    #check col
    for c in range(9):
        if gameboard[row][c] == num:
            return False

    #check box
    boxRow = row // 3
    boxCol = col // 3

    for r in range(boxRow * 3, boxRow * 3 + 3):
        for c in range(boxCol * 3, boxCol * 3 + 3):
            if gameboard[r][c] == num:
                return False

    return True


#Solve puzzle
def solve():
    global gameboard
    for row in range(9):
        for col in range(9):
            if gameboard[row][col] == 0:
                for num in range(1,10):
                    if possible(row, col, num):
                        gameboard[row][col] = num
                        solve()
                        gameboard[row][col] = 0
                return           
    print()
    print("SOLVED PUZZLE: ")
    printGameboard(gameboard)         



#EXECUTE 
print("PUZZLE TO SOLVE: ")       
printGameboard(gameboard)

solve()









