from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

x = 0
y=90
delta=0
while(1):
 delta=90
 while (x < 800):
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x, y)
  x = x + 2 
 while (y < 600):
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x,y )
  y = y + 2
 while (x > 0 ):
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x, y)
  x = x - 2
 while (y > 90):
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x, y)
  y = y - 2
 while (x < 400):
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x, y)
  x = x + 2
 while(delta<450):
  sinx=math.sin(delta/360*2*math.pi)
  cosx=math.cos(delta/360*2*math.pi)
  grass.draw_now(400, 30)
  character.draw_now(x-(200*cosx), y+(200*sinx)+200)
  delta=delta+10
  delay(0.01)
  clear_canvas_now()

close_canvas()
