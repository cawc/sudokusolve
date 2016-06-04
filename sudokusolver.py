import check

EMPTY = 0 #0 1 2 3 4 5 6 7 8
sudoku = [[0,0,0,0,0,9,1,0,6],# 0
					[0,0,7,0,1,3,0,0,4],# 1
					[0,0,1,2,0,0,5,3,0],# 2
					[0,7,0,3,2,0,4,6,0],# 3
					[4,0,0,9,0,6,0,0,3],# 4
					[0,9,3,0,7,4,0,5,0],# 5
					[0,8,6,0,0,1,2,0,0],# 6
					[7,0,0,6,5,0,3,0,0],# 7
					[2,0,4,8,0,0,0,0,0]]# 8

def numPossible(_x,_y,_sudoku,_n):
	return check.safe(_x,_y,_sudoku,_n)

def findEmpty(_sudoku,_x,_y):
	for x in range(_x,9):
		for y in range(_y,9):
			if _sudoku[x][y] == EMPTY:
				print('x%i y%i is empty'%(x,y))
				return x,y

	for x in range(0,9):
		for y in range(0,9):
			if _sudoku[x][y] == EMPTY:
				print('x%i y%i is empty'%(x,y))
				return x,y

	print('No empty fields found')
	return -1,-1

def solve(_sudoku, _x=0, _y=0):
	_x,_y = findEmpty(_sudoku,_x,_y)
	if _x == -1:
		return True

	for i in range(1,10):
		if numPossible(_x,_y,sudoku,i):
			_sudoku[_x][_y] = i
			print('SET X%i Y%i TO %i'%(_x,_y,i))
			if solve(_sudoku,_x,_y):
				return True
			_sudoku[_x][_y] = 0
			print('RESET X%i Y%i TO 0'%(_x,_y))
	return False

solve(sudoku)



for x in range(0,9):
	print(sudoku[x])
