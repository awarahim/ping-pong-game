from pygame import *
#~~~~~~~~~~~ 1st Commit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Game scene
back = (255,255,255) # background color
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


#images
arm_L = 'arm_L.png'
arm_R = 'arm.png'
ball = 'droplet.png'


# losing conditions and fonts
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2nd Commit ~~~~~~~~~~~~~~~~~~~~~~~~~~

#parent class for other sprites
class GameSprite(sprite.Sprite):
#class constructor
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #call for the class (Sprite) constructor:
      sprite.Sprite.__init__(self)
      #every sprite must store the image property
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #every sprite must have the rect property that represents the rectangle it is fitted in
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#method drawing the character on the window
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#main player class
class Player(GameSprite):
  #method to control the sprite with arrow keys
   def update_L(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 10:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_width - 200:
           self.rect.y += self.speed

   def update_R(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 10:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 200:
           self.rect.y += self.speed


player_L = Player(arm_L,30, 200, 60, 90, 10)
player_R = Player(arm_R,520, 200, 60, 90, 10)
ball = GameSprite('droplet.png', 200, 200, 50, 50, 50)

clock = time.Clock()
FPS = 60
game = True
game_over = False


speed_x = 3
speed_y = 3

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if game_over != True:
       window.fill(back)
       player_L.update_L()
       player_R.update_R()
       ball.rect.x += speed_x
       ball.rect.y += speed_y

       if sprite.collide_rect(player_L, ball) or sprite.collide_rect(player_R, ball):
            speed_x *= -1
            speed_y *= 1

       #if the ball reaches screen edges, change its movement direction
       if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
       #if ball flies behind this paddle, display loss condition for player 1
       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True


#        #if ball flies behind this paddle, display loss condition for player 2
       if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True
       

    player_L.reset()
    player_R.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
