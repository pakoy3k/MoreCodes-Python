"""
Problem 20: Write a program to print the number pattern using loop.
  1
 222
33333
 444
  5
"""
import sys
y = 0
x = 0
rows = 2
stars = 1
blank = rows
 
for y in range(0,((rows * 2) + 1)):
 for x in range(0,(blank)):
  sys.stdout.write(" ")
  sys.stdout.flush()
  
 for x in range(0,((stars * 2) - 1)):
  sys.stdout.write(str(y + 1))
  sys.stdout.flush()
  
 print()
 
 if(y < rows) :
  blank -= 1
  stars += 1
 else:
  blank += 1
  stars -= 1
 
