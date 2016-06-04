def xSafe(x,sudoku,n):
	for i in range(0,9):
		if sudoku[x][i] == n:
			#print('*%i is already in x'%n)
			return False
	return True

def ySafe(y,sudoku,n):
	for i in range(0,9):
		if sudoku[i][y] == n:
			#print('*%i is already in y'%n)
			return False
	return True

def zoneSafe(x,y,sudoku,n):
	zoneX, zoneY = 3*int(x/3), 3*int(y/3)
	for xc in range(zoneX, zoneX+3):
		for yc in range(zoneY, zoneY+3):
			if sudoku[xc][yc] == n:
				#print('*%i is in zone from x%i y%i'%(n,xc,yc))
				return False
	return True

def safe(x,y,sudoku,n):
	if xSafe(x,sudoku,n) and ySafe(y,sudoku,n) and zoneSafe(x,y,sudoku,n):
		return True
	return False