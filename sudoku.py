import math

sudoku = [[0 for x in xrange(9)] for x in xrange(9)]

original_coords = []

global_x_back = 0
global_y_back = 0
debug = False


def print_all(sudoku):
    for i in range(9):
        for j in range(9):
            print str(sudoku[j][i]) + ' ',
        print '\n'
    print "================================"


def check_square(x, y, n):
    kvadrant = [0, 0]
    kvadrant[0] = x/3*3
    kvadrant[1] = y/3*3
    kvadrant_cifra = (x/3+1) * (y/3+1)
    #print 'kvadrant: ' + str(kvadrant_cifra)
    #print kvadrant

    occurance = 0
    for i in range(3):
        for j in range(3):
            if n == sudoku[kvadrant[0]+i][kvadrant[1]+j]:
                occurance += 1
    if occurance > 1:
        return False
    else:
        return True


# return False if number already exists, else OK True
def check(x, y):
    n = sudoku[x][y]
    y_count = 0
    x_count = 0
    for i in range(9):
        if n == sudoku[i][y]:
            y_count += 1
        if n == sudoku[x][i]:
            x_count += 1

    if x_count > 1 or y_count > 1:
        return False

    return check_square(x, y, n)


def go_back(x, y):
    global global_x_back, global_y_back
    if x < 0 or x > 9 or y < 0 or y > 9:
        print "out of bounds", x, y
        exit(1)

    if (x, y) in original_coords:
        if debug:
            print "Original coordinate detected", x, y
        global_x_back += 1
        if x-1 < 0:
            if debug:
                print "Edge coordinate detected", x, y
            y = y - 1
            x = 9
        go_back(x-1, y)
    else:
        val = sudoku[x][y] + 1
        if debug:
            print "Value", sudoku[x][y], "increased to", val, "on coord", x, y
        if val > 9:
            sudoku[x][y] = 0
            global_x_back += 1
            if x == 0:
                if debug:
                    print "Edge coordinate detected", x, y
                y = y - 1
                x = 9
                global_y_back += 1
            go_back(x - 1, y)
        else:
            sudoku[x][y] = val
            #print "Value Increased to", val
            if debug:
                print_all(sudoku)
            if check(x, y) is False:
                if debug:
                    print "Inserted value not ok, increasing it again"
                go_back(x, y)


def try_fill():
    global original_coords, global_x_back, global_y_back
    pointer = 0
    x = 0
    y = 0
    while y < 9:
        while x < 9:
            if sudoku[x][y] == 0:
                if debug:
                    print "Processing coordinate", x, y
                for n in range(1, 10):
                    sudoku[x][y] = n
                    if check(x, y) is True:
                        if debug:
                            print "Add value", n, " to ", x, " ", y
                        pointer += 1
                        if debug:
                            print_all(sudoku)
                        break
                    elif n == 9:
                        #sudoku[x][y] = 0
                        if debug:
                            print "Can't add value to", x, y
                        global_x_back = 0
                        global_y_back = 0
                        go_back(x, y)
                        if debug:
                            print "All fixed, continuing on coords 0, 0"
                        x =-1
                        y = 0
                        #exit(0)
            x += 1

        y += 1
        x = 0
        #print_all(sudoku)
    print "Done."


def save_org_coords():
    global original_coords
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                original_coords.append((i, j))

#izpisi(sudoku)
sudoku[8][0] = 1
sudoku[0][1] = 9
sudoku[3][1] = 3
sudoku[4][1] = 2
sudoku[5][1] = 8
sudoku[7][1] = 7
sudoku[8][1] = 5
sudoku[1][2] = 7
sudoku[2][2] = 3
sudoku[5][2] = 9

sudoku[0][3] = 1
sudoku[2][3] = 5
sudoku[5][3] = 6
sudoku[7][3] = 2
sudoku[1][4] = 4
sudoku[7][4] = 1
sudoku[1][5] = 2
sudoku[3][5] = 1
sudoku[6][5] = 5
sudoku[8][5] = 6

sudoku[3][6] = 8
sudoku[6][6] = 3
sudoku[7][6] = 4
sudoku[0][7] = 8
sudoku[1][7] = 3
sudoku[3][7] = 5
sudoku[4][7] = 4
sudoku[5][7] = 2
sudoku[8][7] = 7
sudoku[0][8] = 7
print_all(sudoku)
save_org_coords()

#print original_coords

try_fill()
print_all(sudoku)
