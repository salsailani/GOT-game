
from __future__ import print_function
from random import randint

# The user plays the role of a king in a quest through a vast kingdom to defeat the other kings. 
# The kingdom is represented by an n x n board, where each tile is a town. There are a number of kings (roughly 1 kings for every 6 towns)
# which have randomly chosen a town as their current residence. The user king has at his disposal an army of knights
# (same number of knights as the number of kings), which he/she will use to find and defeat the other kings.
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#The user enters two integers representing the coordinates (row and column) of the next town to be explored.
#Uncovering a tile on the board should return to the user the total number of kings residing in the 8 neighboring towns (tiles). 
#If the location explored has 0 kings around it, uncover all the neighboring tiles as well. If any of the neighboring tiles also has 0 kings around it, uncover its neighbors as well, and so on. 
#The board presented to the user should show the uncovered tiles, unless kings occupy those towns.
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#If the user guesses the location of a king then that king is automatically defeated and the user gains 2 knights
# Somewhere, hidden in one random town in the kingdom, three powerful dragons are hidden. If the user’s move is to this town, the user is presented with the following two choices:
#1.	Swear allegiance to the Mother of Dragons. In this case the user receives a bonus army of 5 knights and continues the game.
#2. if they refuse, they lose and end the game
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#The game ends when:
#1. The user has run out of knights.
#2.	The user has encountered the city of the dragons and refused to swear allegiance to their mother.
#3. The user has defeated all the other kings.



def incrementByOne(Board,size,i,j): #will be used in the incrementing neighbors function
	if(i<0 or i>=size or j<0 or j>=size): #if out of bounds
		return Board #exit 
	if(Board[i][j] < 0): #if there is a king or dragon
		return Board
	Board[i][j] += 1 #the counter
	return Board
	
def incrementNeighbours(Board,size,i,j): #this function is responsible for calculating the number of kings and dragons surounding a vilage.

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
				if Board[i][j] == -1: # if you hit a king
					print ("K ", end = "") #print K
				elif  Board[i][j] == -2:    # if you hit a dragon print D
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
		i = randint(0,size-1) # random row placement for the king
		j = randint(0,size-1) # random column placement for the king
		if(Board[i][j] == 0): # check to see if there is nothing placed already 
			Board[i][j] = -1 # place the king
			Board = incrementNeighbours(Board,size,i,j) 
			kings -= 1 # reduce number of kings remaining to be placed
	dragonPlaced = False
	while not dragonPlaced:
		i = randint(0,size-1) # random row placement for the Dragon
		j = randint(0,size-1) # random column placement for the Dragon
		if(Board[i][j] == 0): # check to see if there is nothing placed already 
			Board[i][j] = -2 #place the dragon
			dragonPlaced = True
	return Board
	
def initGame(size): # this function initializes the boards
	Board = [[0 for x in range(size)] for y in range(size)] # the hidden board
	Visible = [[0 for x in range(size)] for y in range(size)] # the user board (visible)
	kings = size*size/6 # number of kings
	knights = size*size/6 # number of knights
	Board = placePieces(Board,size,kings) #calling function to place the kings and knights
	moves = 0 # user moves
	return (Board,Visible,kings,knights,moves) 
	
def recordWin(user,moves,size): # record each win
	f = open("results.txt", "a") #open a new text file
	f.write("%s\t%d\t%d\n" % (user,moves,size)) #record the user name, number of moves, and size of board
	f.close #close
	
def getMoves(item): # number of moves
	return item[1] #return number of moves
	
def readResults(): # Reading the wins results file
	f = open("results.txt", "r") #open the file
	results = [] #empty array
	for line in f: #loop through lines (each win)
		parts = line.split() #splite into parts
		if len(parts) == 3: #if recorded correctly
			results.append((parts[0],parts[1],parts[2])) #add them to the array
	f.close()
	return sorted(results,key=getMoves) #return 
	
def printResults(results):
	print ("Name\tScore\tBoardSize")
	for (user,moves,size) in results:
		print ("%s\t%s\t%s" % (user,moves,size))
		
print ("Welcome to the G A M E of T H R O N E S !")
user = str(input("State your name, Your Grace: "))
size = int(input("How vast is your kingdom %s, Your Grace? (Enter an integer for the size of the board)" % (user)))
(Board,Visible,kings,knights,moves) = initGame(size)
#printBoard(Board,size) This is to see the board with the actual values

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
	
