def empty(x,y,sudoku):
	for number in sudoku:
		if sudoku[x][y] == EMPTY:
			return True

def xSafe(y,sudoku,n):
	for i in range(0,9):
		if sudoku[y][i] == n:
			return False
	return True

def ySafe(x,sudoku,n):
	for i in range(0,9):
		if sudoku[i][x] == n:
			return False
	return True

def zoneSafe(x,y,sudoku,n):
	zoneX, zoneY = 3*int(x/3), 3*int(y/3)
	for yc in range(zoneY, zoneY+3):
		for xc in range(zoneX, zoneX+3):
			if sudoku[yc][xc] == n:
				print('X%i Y%i = %i within the zone'%xc,yc,n)
				return False
	return True

def safe(x,y,sudoku,n):
	if xSafe(y,sudoku,n) and ySafe(x,sudoku,n) and zoneSafe(x,y,sudoku,n):
		return True
	return False