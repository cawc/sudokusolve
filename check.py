def checkEmpty(row,col,sudoku):
	for number in sudoku:
		if sudoku[row][col] == EMPTY:
			return True

def checkRowSafe(col,sudoku,n):
	for i in range(0,9):
		if sudoku[i][col] == n:
			return False
	return True

def checkColSafe(row,sudoku,n):
	for i in range(0,9):
		if sudoku[row][i] == n:
			return False
	return True

def checkFieldSafe(row,col,sudoku,n):
	return True