import math

sudoku = [[0 for x in xrange(9)] for x in xrange(9)]

def izpisi(sudoku):
    for i in range(9):
        for j in range(9):
            print str(sudoku[j][i]) + ' ',
        print '\n'

def preveri_kvadratek(x,y,cifra):
    kvadrant = [0,0]
    kvadrant[0] = x/3*3
    kvadrant[1] = y/3*3
    kvadrant_cifra = (x/3+1) * (y/3+1)
    print 'kvadrant: ' + str(kvadrant_cifra)
    print kvadrant
    for i in range(3):
        for j in range(3):
            if cifra == sudoku[kvadrant[0]+i][kvadrant[1]+j]:
                return True
    return False

def preveri_vrstico_stolpec(x,y,cifra):
	for i in range(9):
		if cifra == sudoku[i][y]:
			return True
		if cifra == sudoku[x][i]:
			return True
	return False

def napolni():
	for cifra in range(9,1, -1):
		for y in range(9):
			for x in range(9):
				if sudoku[x][y] == 0:
					if preveri_vrstico_stolpec(x,y, cifra) == False and preveri_kvadratek(x,y, cifra) == False:
							sudoku[x][y] = cifra
			

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

napolni()
izpisi(sudoku)
