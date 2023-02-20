import random
import time
import os
import sys 
import subprocess

print('Welcome to the random number generator! Please type a number!: ')


while True:
  minimum = int(input("Type a min. number: "))
  maximum = int(input("Type a max. number: "))

  zufallszahl = random.randint(minimum, maximum)
  
  print(zufallszahl)
  print( )
  print( )
  print('Starts again...')
  print('.')
  time.sleep(1)
  print('..')
  time.sleep(1)
  print('...')
  time.sleep(1)

