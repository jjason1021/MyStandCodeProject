"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
Name: Jason
This program makes bricks breakout by ball bounce between paddle and wall. Game will finish when fails 3 times or
all bricks are removed.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=(self.window.height - paddle_offset))
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        # self.set_ball_position()  # method
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        # self.set_ball_position():
        # self.ball.x = (self.window.width - self.ball.width) / 2
        # self.ball.y = (self.window.height - self.ball.height) / 2

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.change_position)
        onmouseclicked(self.fall)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=(brick_width+brick_spacing)*i,
                                y=brick_offset+(brick_height+brick_spacing)*j)
                # if self.brick.y < brick_offset+brick_spacing+brick_height*2:
                # fill color
                if j < 2:
                    self.brick.fill_color = 'red'
                elif 2 <= j < 4:
                    self.brick.fill_color = 'orange'
                elif 4 <= j < 6:
                    self.brick.fill_color = 'yellow'
                elif 6 <= j < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
        self.brick_counts = brick_cols * brick_rows

    def change_position(self, mouse):  # paddle will move with mouse x location
        self.paddle.x = mouse.x - PADDLE_WIDTH/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x+self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def fall(self, mouse):  # decide initial ball speed
        if self.__dx == 0 and self.__dy == 0:  # ball should be static to start
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_vx(self):
        # getter
        return self.__dx

    def get_vy(self):
        # getter
        return self.__dy

    def set_vx(self, new_dx):
        # setter
        self.__dx = new_dx

    def set_vy(self, new_dy):
        # setter
        self.__dy = new_dy

    def check(self):
        switch = True
        for i in range(2):
            for j in range(2):
                maybe_obj = self.window.get_object_at(self.ball.x+BALL_RADIUS*2*i, self.ball.y+BALL_RADIUS*2*j)
                if maybe_obj is not None:
                    if maybe_obj is not self.paddle:
                        self.window.remove(maybe_obj)
                        self.brick_counts -= 1
                        # self.__dx = -self.__dx
                        self.__dy = -self.__dy
                        switch = False
                        break  # for j loop break
                    if maybe_obj is self.paddle and self.__dy > 0:
                        # self.__dx = -self.__dx
                        self.__dy = -self.__dy
                        switch = False
                        break  # for j loop break
            if not switch:  # for i loop break if j loop break
                break
