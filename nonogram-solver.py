import random

clue_rows = []
clue_cols = []
grid = []

# TODO: loop and try-catch block in case of invalid (non-integer) input
grid_width = int(input("Grid width: "))
grid_height = int(input("Grid height: "))

# prompt for clues ("top bar")


# prompt for clues ("left bar")


# generate and print random, non-valid grid to get
# an idea of what actual outputs will look like
line = ""
rand = 0

for row in range(-1, grid_height + 1):
  for col in range(-1, grid_width + 1):
    if row < 0 or row == grid_height:
      line += "-"
    
    elif col < 0 or col == grid_width:
      line += "|"
    
    else:
      rand = random.randint(0,1)
      line += "█" if rand else "X"

  print(line)
  line = ""
