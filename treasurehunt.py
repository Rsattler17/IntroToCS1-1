#Treasure Hunt Lab
#Ryan Sattler, Graham Pankratz, Jacob Bussmann
#10-14-18
import random


#Greeting 
print('Welcome to the Treasure Hunt!') 

#User Input/Difficulty Level 
difficulty =input('What difficulty level would you like? (enter: "E" for easy (3x3), "M" for Medium (4x4), "H" for Hard (5x5)')

#User error
while difficulty not in ('E', 'M', 'H'):
    print('Game difficulty not possible.')
    difficulty = input('What difficulty level would you like? (enter: "E" for easy (3x3), "M" for Medium (4x4), "H" for Hard (5x5)')
    
#Determining Grid Size
#Easy mode
if difficulty == 'E':
    width = 3
if difficulty == 'E':
    height = 3
#Medium Mode
if difficulty == 'M':
    width = 4
if difficulty == 'M':
    height = 4
#Hard Mode
if difficulty == 'H':
    width = 5
if difficulty == 'H':
    height = 5

#Displaying Grid
grid = []
row = []
back = ' ' 
for i in range(width):
    row.append(back)
for i in range(height):
    grid.append(row)

for i in range (len(grid)):
        print(grid[i])
