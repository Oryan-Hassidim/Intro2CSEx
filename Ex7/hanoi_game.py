__author__ = 'ayalg'
## Animated Tower-Of-Hanoi game with Tkinter GUI
## using Python's turtle module
## author: Gregor Lingl, Vienna, Austria
## email: glingl@aon.at
## date: 22. 7. 2009
## modified for Into2Cs2015 by Ayal Green

## derived from a pure tkinter-version from 16. 2. 2004

from tkinter import *
from turtle import TurtleScreen, RawTurtle
import ex7

class Disc(RawTurtle):
    """Hanoi disc, a RawTurtle object on a TurtleScreen."""
    def __init__(self, cv):
        RawTurtle.__init__(self, cv, shape="square", visible=False)
        self.pu()
        self.goto(-140,200)
    def config(self, k, n):
        self.hideturtle()
        f = float(k+1)/n
        self.shapesize(0.5, 1.5+5*f) # square-->rectangle
        self.fillcolor(f, 0, 1-f)
        self.showturtle()


class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-70+10*len(self))
        self.append(d)
    def pop(self, y=90):
        d = list.pop(self)
        d.sety(y)
        return d


class HanoiEngine:
    """Play the Hanoi-game on a given TurtleScreen."""
    def __init__(self, canvas, nrOfDiscs, speed, moveCntDisplay=None):
        """Sets Canvas to play on as well as default values for
        number of discs and animation-speed.
        moveCntDisplay is a function with 1 parameter, which communicates
        the count of the actual move to the GUI containing the
        Hanoi-engine-canvas."""
        self.ts = canvas
        self.ts.tracer(False)
        # setup scene
        self.designer = RawTurtle(canvas, shape="square")
        self.designer.penup()
        self.designer.shapesize(0.5, 21)
        self.designer.goto(0,-80); self.designer.stamp()
        self.designer.shapesize(7, 0.5)
        self.designer.fillcolor('darkgreen')
        for x in -140, 0, 140:
            self.designer.goto(x,-5); self.designer.stamp()

        self.nrOfDiscs = nrOfDiscs
        self.speed = speed
        self.moveDisplay = moveCntDisplay
        self.running = False
        self.moveCnt = 0
        self.discs = [Disc(canvas) for i in range(10)]
        self.towerA = Tower(-140)
        self.towerB = Tower(0)
        self.towerC = Tower(140)
        self.ts.tracer(True)

    def setspeed(self):
        for disc in self.discs: disc.speed(self.speed)

    def move(self, src_tower, dest_tower):
        """move uppermost disc of source tower to top of destination
        tower."""
        dest_tower.push(src_tower.pop())
        self.moveCnt += 1
        self.moveDisplay(self.moveCnt)

    def reset(self):
        """Setup of (a new) game."""
        self.ts.tracer(False)
        self.moveCnt = 0
        self.moveDisplay(0)
        for t in self.towerA, self.towerB, self.towerC:
            while t != []: t.pop(200)
        for k in range(self.nrOfDiscs-1,-1,-1):
            self.discs[k].config(k, self.nrOfDiscs)
            self.towerA.push(self.discs[k])
        self.ts.tracer(True)

    def run(self):
        """run game ;-)
        return True if game is over, else False"""
        self.running = True
        ex7.play_hanoi(self, self.nrOfDiscs,
                             self.towerA, self.towerC, self.towerB)
        return True

class Hanoi:
    """GUI for animated towers-of-Hanoi-game with upto 10 discs:"""

    def displayMove(self, move):
        """method to be passed to the Hanoi-engine as a callback
        to report move-count"""
        self.moveCntLbl.configure(text = "move:\n%d" % move)

    def adjust_nr_of_discs(self, e):
        """callback function for nr-of-discs-scale-widget"""
        self.hEngine.nrOfDiscs = self.discs.get()
        self.reset()

    def adjust_speed(self, e):
        """callback function for speeds-scale-widget"""
        self.hEngine.speed = self.tempo.get() % 10
        self.hEngine.setspeed()

    def setState(self, STATE):
        """most simple implementation of a finite state machine"""
        self.state = STATE
        try:
            if STATE == "START":
                self.discs.configure(state=NORMAL)
                self.discs.configure(fg="black")
                self.discsLbl.configure(fg="black")
                self.resetBtn.configure(state=DISABLED)
                self.startBtn.configure(text="start", state=NORMAL)
            elif STATE == "RUNNING":
                self.discs.configure(state=DISABLED)
                self.discs.configure(fg="gray70")
                self.discsLbl.configure(fg="gray70")
                self.startBtn.configure(state=DISABLED)
            elif STATE == "DONE":
                self.discs.configure(state=NORMAL)
                self.discs.configure(fg="black")
                self.discsLbl.configure(fg="black")
                self.resetBtn.configure(state=NORMAL)
                self.startBtn.configure(text="start", state=DISABLED)
            elif STATE == "TIMEOUT":
                self.discs.configure(state=DISABLED)
                self.discs.configure(fg="gray70")
                self.discsLbl.configure(fg="gray70")
                self.resetBtn.configure(state=DISABLED)
                self.startBtn.configure(state=DISABLED)
        except TclError:
            pass

    def reset(self):
        """restore state "START" for a new game"""
        self.hEngine.reset()
        self.setState("START")

    def start(self):
        """callback function for start button. Makes hEngine running until done"""
        if self.state == "START":
            self.setState("RUNNING")
            if self.hEngine.run():
                self.setState("DONE")


    def __init__(self, nrOfDiscs, speed):
        """construct Hanoi-engine, build GUI and set STATE to "START"
        then launch mainloop()"""
        root = Tk()
        root.title("TOWERS OF HANOI")
        cv = Canvas(root,width=440,height=210, bg="gray90")
        cv.pack()
        cv = TurtleScreen(cv)
        self.hEngine = HanoiEngine(cv, nrOfDiscs, speed, self.displayMove)
        fnt = ("Arial", 12, "bold")
        # set attributes: nr of discs, speed; display move count
        attrFrame = Frame(root) #contains scales to adjust game's attributes
        self.discsLbl = Label(attrFrame, width=7, height=2, font=fnt,
                              text="discs:\n")
        self.discs = Scale(attrFrame, from_=1, to_=10, orient=HORIZONTAL,
                           font=fnt, length=75, showvalue=1, repeatinterval=10,
                           command=self.adjust_nr_of_discs)
        self.discs.set(nrOfDiscs)
        self.tempoLbl = Label(attrFrame, width=8,  height=2, font=fnt,
                              text = "   speed:\n")
        self.tempo = Scale(attrFrame, from_=1, to_=10, orient=HORIZONTAL,
                           font=fnt, length=100, showvalue=1,repeatinterval=10,
                           command = self.adjust_speed)
        self.tempo.set(speed)
        self.moveCntLbl= Label(attrFrame, width=5, height=2, font=fnt,
                               padx=20, text=" move:\n0", anchor=CENTER)
        for widget in ( self.discsLbl, self.discs, self.tempoLbl, self.tempo,
                                                             self.moveCntLbl ):
            widget.pack(side=LEFT)
        attrFrame.pack(side=TOP)
        # control buttons: reset, start
        ctrlFrame = Frame(root) # contains Buttons to control the game
        self.resetBtn = Button(ctrlFrame, width=11, text="reset", font=fnt,
                               state = DISABLED, padx=15, command = self.reset)
        self.startBtn = Button(ctrlFrame, width=11, text="start", font=fnt,
                               state = NORMAL,  padx=15, command = self.start)
        for widget in self.resetBtn, self.startBtn:
            widget.pack(side=LEFT)
        ctrlFrame.pack(side=TOP)

        self.state = "START"
        root.mainloop()

if __name__  == "__main__":
    Hanoi(6,3)