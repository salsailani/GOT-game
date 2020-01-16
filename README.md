# Game of Thrones board game

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

#The game ends when:
#1. The user has run out of knights.
#2.	The user has encountered the city of the dragons and refused to swear allegiance to their mother.
#3. The user has defeated all the other kings.
