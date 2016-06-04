from bs4 import BeautifulSoup
import requests, re

url = 'http://show.websudoku.com/?level=4'
page = requests.get(url)
page.raise_for_status()
rawPage=page.text

sudokuid = int(re.search(r'\d+', rawPage.split('\n')[20]).group())

soup = BeautifulSoup(rawPage,'html.parser')
sudokuTable = soup.findAll(True, {'class':['s0', 'd0']})
sudoku = [ [(int(item['value']) if item.get('class')[0] == 's0' else 0) for item in sudokuTable][i:i+9] for i in range(0, 81, 9) ]

filename = 'sudokus/sudoku_%i.txt'%sudokuid
sudokufile = open(filename, 'w')
for line in sudoku:
	sudokufile.write( str(line).replace(',',' ').replace('[','').replace(']',' ') + '\n' )
