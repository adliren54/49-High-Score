import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  