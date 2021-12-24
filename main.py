import random
import time

def goToTheTree():
  print("Going to the tree...")
  time.sleep(1)
  print("We're now there! What's next?")
  shakeTheTree()

def shakeTheTree():
  print("Shaking tree...")
  numberOfApples = random.randrange(0, 30)
  print("We got ", numberOfApples, " apples")
  collectApples(numberOfApples)

def collectApples(numberOfApples):
  for i in range(1, numberOfApples+1):
    print("Collecting...", i)
    time.sleep(1)
  else:
    print("All apples collected!")
  beProud()

def beProud():
  print("Good Job!")

goToTheTree()