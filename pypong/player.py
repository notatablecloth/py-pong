import pygame, random

class BasicAIPlayer(object):
    def __init__(self):
        self.bias = random.random() - 0.5
        self.hit_count = 0
        
    def update(self, paddle, game):
        # Dead simple AI, waits until the ball is on its side of the screen then moves the paddle to intercept.
        # A bias is used to decide which edge of the paddle is going to be favored.
        if (paddle.rect.x < game.bounds.centerx and game.ball.rect.x < game.bounds.centerx) or (paddle.rect.x > game.bounds.centerx and game.ball.rect.x > game.bounds.centerx):
            delta = (paddle.rect.centery + self.bias * paddle.rect.height) - game.ball.rect.centery 
            if abs(delta) > paddle.velocity:
                if delta > 0:
                    paddle.direction = -1
                else:
                    paddle.direction = 1
            else:
                paddle.direction = 0
        else:
            paddle.direction = 0

    def hit(self):
        self.hit_count += 1
        if self.hit_count > 6:
            self.bias = random.random() - 0.5 # Recalculate our bias, this game is going on forever
            self.hit_count = 0
            
    def lost(self):
        # If we lose, randomise the bias again
        self.bias = random.random() - 0.5
        
    def won(self):
        pass
        
class KeyboardPlayer(object):
    def __init__(self, input_state, up_key=None, down_key=None):
        self.input_state = input_state
        self.up_key = up_key
        self.down_key = down_key
        
    def update(self, paddle, game):
        if self.input_state['key'][self.up_key]:
            paddle.direction = -1
        elif self.input_state['key'][self.down_key]:
            paddle.direction = 1
        else:
            paddle.direction = 0

    def hit(self):
        pass

    def lost(self):
        pass
        
    def won(self):
        pass
        
class MousePlayer(object):
    def __init__(self, input_state):
        self.input_state = input_state
        pygame.mouse.set_visible(False)
        
    def update(self, paddle, game):
        centery = paddle.rect.centery/int(paddle.velocity)
        mousey = self.input_state['mouse'][1]/int(paddle.velocity)
        if centery > mousey:
            paddle.direction = -1
        elif centery < mousey:
            paddle.direction = 1
        else:
            paddle.direction = 0

    def hit(self):
        pass

    def lost(self):
        pass

    def won(self):
        pass
