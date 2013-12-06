import random

def roll3d6():
  return random.choice(1, 6) + random.choice(1, 6) + random.choice(1, 6)

def rolld100():
  return random.choice(1, 100)
