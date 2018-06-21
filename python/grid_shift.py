"""
print grid so that the corresponding indexes of each inner list prints 
horizontally as a new line.
""" 


grid = [
['0', '.', '.', '.', '.'],
['0', '.', '.', '.', '.'],
['.', '0', '0', '.', '.'],
['.', '.', '.', '0', '0'],
['.', '0', '0', '.', '.'],
['0', '.', '.', '.', '.'],
['0', '.', '.', '.', '.']
]


#???map, zip
#print('\n'.join(map(''.join, zip(*grid))))


for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print(i)
    print('')


"""
def printer(grid):
    for m in range(len(grid[0])):
        print()
        for n in range(len(grid)):
            print (grid[n][m],end="")
            n+=1        
    m+=1

printer(grid)
"""