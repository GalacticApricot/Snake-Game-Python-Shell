import txtblit as t
from getch import getch
import random
from time import sleep as wait
screen = t.screen(40, 20)
score = 0
lastinp = None
start = False

class apple:
  def __init__(self, screen):
    self.screen = screen
    self.object = t.object()
    self.object.rect(2, 1, 5, 0, self.screen)
  def newpos(self):
    x = random.randint(1, ((self.screen.width-2)/2)) * 2
    y = random.randint(2, self.screen.height-2)
    self.object.x = x
    self.object.y = y


capple = apple(screen)
capple.newpos()

class snake:
  def __init__(self, screen):
    self.screen = screen
    self.head = t.object()
    self.head.rect(2, 1, 40, 0, self.screen)
    self.head.center((1, 0))
    self.snake = [self.head]
  def move(self, p):
    for i in range(len(self.snake)-1, 0, -1):
      self.snake[i].x = self.snake[i-1].x
      self.snake[i].y = self.snake[i-1].y
    match p:
      case "s":
        if len(self.snake) == 1 or self.head.y >= self.snake[1].y:
          self.head.y += 1
      case "d":
        if len(self.snake) == 1 or self.head.x >= self.snake[1].x:
          self.head.x += 2
      case "w":
        if len(self.snake) == 1 or self.head.y <= self.snake[1].y:
          self.head.y -= 1
      case "a":
        if len(self.snake) == 1 or self.head.x <= self.snake[1].x:
          self.head.x -= 2
  def getbigger(self):
    new = t.object()
    new.rect(2, 1, self.snake[-1].x, self.snake[-1].y, self.screen)
    self.snake.append(new)
  def is_hit(self):
    if self.head.x < 0 or self.head.x == self.screen.width or self.head.y < 0 or self.head.y > self.screen.height:
      return True
    for i in range(2, len(self.snake)-2):
      if self.snake[i].x == self.head.x and self.snake[i].y == self.head.y:
        return True
    return False

  def update(self):
    global capple, lastinp, score, start
    inp = getch()
    if inp:
      lastinp = inp
      self.move(inp)
      if not start:
        start = True
      if t.istouching(self.head, capple.object):
        self.getbigger()
        capple.newpos()
        score += 1
    else:
      self.move(lastinp)
    return self.is_hit()

csnake = snake(screen)
con = True



while con:
  if csnake.update():
    con = False
  screen.update()
  if start:
    print(f"               Score: {score}")
  wait(0)
print("game over")
