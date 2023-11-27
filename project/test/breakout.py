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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        if lives > 0 and graphics.brick_counts > 0:  # continuous condition
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.ball.move(vx, vy)
            graphics.check()  # check if there is object and what object is, then go following action
            pause(FRAME_RATE)
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:  # two sides
                graphics.set_vx(-vx)
            if graphics.ball.y <= 0:  # top side
                graphics.set_vy(-vy)
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:  # out of bottom side
                lives -= 1
                # graphics.set_ball_position
                graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                    y=(graphics.window.height - graphics.ball.height) / 2)
                graphics.set_vx(0)
                graphics.set_vy(0)
                # graphics.set_ball_position
                # graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
                # graphics.ball.x = (graphics.window.height - graphics.ball.height) / 2
        else:
            break


if __name__ == '__main__':
    main()
