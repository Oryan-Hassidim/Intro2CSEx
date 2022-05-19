import tkinter as tki
import random
from random import randint, randrange

CANVAS_SIZE = 600
BALL_SIZE = 20
STEP_SIZE = 2


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def randcolor():
    return rgb_hack((randint(0, 255), randint(0, 255), randint(0, 255)))


class Ball():
    def __init__(self, id):
        self.id = id
        self.dx = randint(2,20)
        self.dy = randint(2,20)


class MyApp:
    def __init__(self, parent):
        self._parent = parent

        self._canvas = tki.Canvas(parent, width=CANVAS_SIZE,
                                  height=CANVAS_SIZE,
                                  highlightbackground='black')
        self._canvas.pack()

        button = tki.Button(parent,
                            text="Add",
                            command=self._add_ball)
        button.pack()

        self._balls = set()  # the list of balls that are on screen.
        self._move()     # start moving the balls!

    def _add_ball(self):
        for _ in range(50):
            x = random.randrange(CANVAS_SIZE - BALL_SIZE)
            y = random.randrange(CANVAS_SIZE - BALL_SIZE)
            ball = self._canvas.create_oval(x, y, x + BALL_SIZE, y + BALL_SIZE, fill=randcolor())
            print(ball)
            self._balls.add(Ball(ball))

    def _move(self):
        for ball in self._balls:
            x1, y1, x2, y2 = self._canvas.coords(ball.id)

            if x1 + ball.dx < 0 or x2 + ball.dx > CANVAS_SIZE:
                ball.dx *= -1

            if y1 + ball.dy < 0 or y2 + ball.dy > CANVAS_SIZE:
                ball.dy *= -1
            self._canvas.move(ball.id, ball.dx, ball.dy)
        # notice HERE! we ask for an event in 10 msec to move again!
        self._parent.after(5, self._move)


root = tki.Tk()
MyApp(root)
root.mainloop()
