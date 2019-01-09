
from __future__ import print_function
from random import randint

def incrementByOne(Board,size,i,j):
	if(i<0 or i>=size or j<0 or j>=size):
		return Board
	if(Board[i][j] < 0):
		return Board
	Board[i][j] += 1
	return Board
	
def incrementNeighbours(Board,size,i,j):
	Board = incrementByOne(Board,size,i-1,j-1)
	Board = incrementByOne(Board,size,i-1,j)
	Board = incrementByOne(Board,size,i-1,j+1)
	Board = incrementByOne(Board,size,i,j-1)
	Board = incrementByOne(Board,size,i,j+1)
	Board = incrementByOne(Board,size,i+1,j-1)
	Board = incrementByOne(Board,size,i+1,j)
	Board = incrementByOne(Board,size,i+1,j+1)
	return Board
	
def display(Board,Visible,size):
	print('- ', end = "")
	for i in range (1,size+1):
		print (str(i) + " ", end = "")
	print ("\n")
	for i in range(0,size):
		print (str(i+1)+" ", end = "")
		for j in range(0,size):
			if Visible[i][j] == 0:
				print (". ", end = "")
			else:
				if Board[i][j] == -1:
					print ("* ", end = "")
				elif  Board[i][j] == -2:
					print ("D ", end = "")
				else:
					print (str(Board[i][j])+" ", end = "")
		print ("\n")
					
def visitNeighbours(Board,Visible,size,i,j):
	if(i<0 or i>=size or j<0 or j>=size or Visible[i][j] == 1):
		return Visible
	Visible[i][j] = 1
	if Board[i][j] == 0:
		Visible = visitNeighbours(Board,Visible,size,i-1,j-1)
		Visible = visitNeighbours(Board,Visible,size,i-1,j)
		Visible = visitNeighbours(Board,Visible,size,i-1,j+1)
		Visible = visitNeighbours(Board,Visible,size,i,j-1)
		Visible = visitNeighbours(Board,Visible,size,i,j+1)
		Visible = visitNeighbours(Board,Visible,size,i+1,j-1)
		Visible = visitNeighbours(Board,Visible,size,i+1,j)
		Visible = visitNeighbours(Board,Visible,size,i+1,j+1)
	return Visible

def printBoard(Board,size):
	for i in range(0,size):
		print (Board[i])
		
def placePieces(Board,size,kings):
	while kings>0:
		i = randint(0,size-1)
		j = randint(0,size-1)
		if(Board[i][j] == 0):
			Board[i][j] = -1
			Board = incrementNeighbours(Board,size,i,j)
			kings -= 1
	dragonPlaced = False
	while not dragonPlaced:
		i = randint(0,size-1)
		j = randint(0,size-1)
		if(Board[i][j] == 0):
			Board[i][j] = -2
			dragonPlaced = True
	return Board
	
def initGame(size):
	Board = [[0 for x in range(size)] for y in range(size)]
	Visible = [[0 for x in range(size)] for y in range(size)]
	kings = size*size/6
	knights = size*size/6
	Board = placePieces(Board,size,kings)
	moves = 0
	return (Board,Visible,kings,knights,moves)
	
def recordWin(user,moves,size):
	f = open("results.txt", "a")
	f.write("%s\t%d\t%d\n" % (user,moves,size))
	f.close()
	
def getMoves(item):
	return item[1]
	
def readResults():
	f = open("results.txt", "r")
	results = []
	for line in f:
		parts = line.split()
		if len(parts) == 3:
			results.append((parts[0],parts[1],parts[2]))
	f.close()
	return sorted(results,key=getMoves)
	
def printResults(results):
	print ("Name\tScore\tBoardSize")
	for (user,moves,size) in results:
		print ("%s\t%s\t%s" % (user,moves,size))
		
print ("Welcome to the G A M E of T H R O N E S !")
user = str(input("State your name, Your Grace: "))
size = int(input("How vast is your kingdom %s, Your Grace? (Enter an integer for the size of the board)" % (user)))
(Board,Visible,kings,knights,moves) = initGame(size)
printBoard(Board,size)
while(True):
	if kings < 1:
		Visible = [[1 for x in range(size)] for y in range(size)]
		print ("Congratulations %s, Your Grace! You have %d knights left and you defeated all %d kings in %d moves." % (user,knights,size*size/6,moves))
		display(Board,Visible,size)
		recordWin(user,moves,size)
		printResults(readResults())
		response = str(input("Play again: Y/N ")).lower()
		if response != 'y':
			break
		(Board,Visible,kings,knights,moves) = initGame(size)
		continue
	if knights < 1:
		response = str(input("You have ran out of knights and hence lost the game. Continue with new set of knights: Y/N ")).lower()
		if response != 'y':
			break
		knights = size*size/6
		continue
	print ("%s, Your Grace, you have %d knights left to defeat %d kings." % (user,knights, kings)) 
	display(Board,Visible,size)
	i = int(input("Please enter x: "))-1
	j = int(input("Please enter y: "))-1
	if(i<0 or i>=size or j<0 or j>=size or Visible[i][j] == 1):
		print ("invalid input")
		continue
	moves += 1
	if(Board[i][j] > 0):
		Visible[i][j] = 1
		knights -= 1
		continue
	elif(Board[i][j] == -1):
		Visible[i][j] = 1
		knights += 2
		kings -= 1
		continue
	elif(Board[i][j] == -2):
		Visible[i][j] = 1
		response = str(input("You have found the mother of dragons. Swear allegiance to the	Mother of Dragons: Y/N ")).lower()
		if response != 'y':
			response = str(input("You have been defeated by the dragons Continue the game: Y/N ")).lower()
			if response == 'y':
				continue
			else:
				break
		print ("Good. For your allegiance you have been awarded 5 knights")
		knights += 5
		continue
	elif(Board[i][j] == 0):
		Visible = visitNeighbours(Board,Visible,size,i,j)
		knights -= 1
		continue
	
got.py
