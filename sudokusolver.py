import check, glob

EMPTY = 0

def numPossible(_x,_y,_sudoku,_n):
	return check.safe(_x,_y,_sudoku,_n)

def findEmpty(_sudoku,_x,_y):
	for x in range(_x,9):
		for y in range(_y,9):
			if _sudoku[x][y] == EMPTY:
				#print('x%i y%i is empty'%(x,y))
				return x,y

	for x in range(0,9):
		for y in range(0,9):
			if _sudoku[x][y] == EMPTY:
				#print('x%i y%i is empty'%(x,y))
				return x,y

	#print('No empty fields found')
	return -1,-1

def solve(_sudoku, _x=0, _y=0):
	_x,_y = findEmpty(_sudoku,_x,_y)
	if _x == -1:
		return True

	for i in range(1,10):
		if numPossible(_x,_y,sudoku,i):
			_sudoku[_x][_y] = i
			#print('SET X%i Y%i TO %i'%(_x,_y,i))
			if solve(_sudoku,_x,_y):
				return True
			_sudoku[_x][_y] = 0
			#print('RESET X%i Y%i TO 0'%(_x,_y))
	return False

sudokufiles = glob.glob('sudokus\sudoku_*.txt')
solvedsudokus = glob.glob('sudokus\solvedsudoku_*.txt')
for sudoku in sudokufiles:
	if sudoku.replace('sudoku_','solvedsudoku_') in solvedsudokus:
		sudokufiles.remove(sudoku)
print(sudokufiles)

for sudokuname in sudokufiles:
	with open(sudokuname) as s:
		sudoku = [list(map(int,x.strip('\n').split())) for x in s.readlines()]
	solve(sudoku)

	print('Solved %s'%sudokuname)
	for x in range(0,9):
		solvefile = open(sudokuname.replace('sudoku_','solvedsudoku_'), 'a')
		solvefile.write(str(sudoku[x]).replace(',',' ').replace('[','').replace(']','')+'\n')
