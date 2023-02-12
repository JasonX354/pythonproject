import random

def layout(grid, character):
  x = random.randint(0, 9)
  y = random.randint(0, 9)
  for row_n, row in enumerate(grid):
    for element_n, element in enumerate(row):
      if element == character:
        if row_n != y and element_n != x:
          grid[y][x] = str(random.randint(1, 9))
  for x, y in enumerate(grid):
    print(grid[x])

def up(x):
  placeholder = 0
  for row_n, row in enumerate(field):
    for element_n, element in enumerate(row):
      if element == x:
        if row_n == 0:
          print("choose another direction")
          break
        if field[row_n - 1][element_n] != " ":
          placeholder = int(field[row_n -1][element_n])
        field[row_n - 1][element_n] = field[row_n][element_n]
        field[row_n][element_n] = " "
  return placeholder

def down(x):
  placeholder = 0
  for row_n, row in enumerate(field):
    for element_n, element in enumerate(row):
      if element == x:
        if row_n == 9:
          print("choose another direction")
          break
        if field[row_n + 1][element_n] != " ":
          placeholder = int(field[row_n + 1][element_n])
        field[row_n + 1][element_n] = "X1"
        field[row_n][element_n] = " "
      if element == "X1":
        field[row_n][element_n] = x
  return placeholder

def left(x):
  placeholder = 0
  for row_n, row in enumerate(field):
    for element_n, element in enumerate(row):
      if element == x:
        if element_n == 0:
          print("choose another direction")
          break
        if field[row_n][element_n - 1] != " ":
          placeholder = int(field[row_n][element_n - 1])
        field[row_n][element_n - 1] = field[row_n][element_n]
        field[row_n][element_n] = " "
  return placeholder

def right(x):
  placeholder = 0
  for row_n, row in enumerate(field):
    for element_n, element in enumerate(row):
      if element == x:
        if element_n == 9:
          print("choose another direction")
          break
        if field[row_n][element_n + 1] != " ":
          placeholder = int(field[row_n][element_n + 1])
        field[row_n][element_n + 1] = field[row_n][element_n]
        field[row_n][element_n] = " "
        return placeholder
  return 0


def difficulty(x):
  settings = ["EASY", "MEDIUM", "HARD"]
  while x in settings:
    if x == "EASY":
      return(random.randint(100,300))
    if x == "MEDIUM":
      return(random.randint(300, 700))
    if x == "HARD":
      return(random.randint(700, 1000))
  return difficulty(input("What difficulty? EASY/MEDIUM/HARD: "))




def operator(operation, value1, value2):
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for x, n in enumerate(numbers):
    if value2 == numbers[x]:
      if operation == "add":
        return(value1 + value2)
      elif operation == "subtract":
        return(value1 - value2)
      elif operation == "multiply":
        return(value2 * value1)
      elif operation == "divide":
        return((value1 // value2))
      else:
        print("Invalid operation. Score did not change.")
        return(value1)

#could turn name into string and do stuff to it
def character_selection(name):
  while check(name):
    if len(name) == 1:
      print("Cannot be a number")
      name = input("What is your favorite letter or symbol?: ")
    else:
      print("One letter please!")
      name = input("What is your favorite letter or symbol?: ")
  return name

def check(name):
  if len(name) == 1:
    if (ord(name) < ord('0') | ord(name) > ord('9')):
      return False
    else:
      return True
  return True


#                                   MAIN

field = [[" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10,
         [" "] * 10]



character = character_selection(input("What is your favorite letter?: "))
field[random.randint(0, 9)][random.randint(0, 9)] = character
goal = difficulty(input("What difficulty? EASY/MEDIUM/HARD: "))
score = 0
turns = 0
print("Try to reach: " + str(goal))

while True:
  value = 0
  layout(field, character)
  print("Current score is " + str(score))
  print("Goal is " + str(goal))
  player_movement = input(character + " up/down/left/right: ")
  turns += 1

  if player_movement == "up":
    value += up(character)
  elif player_movement == "down":
    value += down(character)
  elif player_movement == "left":
    value += left(character)
  elif player_movement == "right":
    value += right(character)
  else:
    continue

  if value != 0:
      score = operator(input("add/subtract/multiply/divide: "), score, value)

  if score == goal:
    print("You win! It took you " + str(turns) + " turns!")
    break
