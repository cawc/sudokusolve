import check

EMPTY = 0
sudoku = [[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0]]
	
def checkSafe(row,col,sudoku,n):
	if check.checkRowSafe(col,sudoku,n) and check.checkColSafe(row,sudoku,n) and check.checkFieldSafe:
		return True
	else:
		return False


if checkSafe(1,0,sudoku,1):
	print('Safe!')
else:
	print('Not safe')