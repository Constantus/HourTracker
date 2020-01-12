# HourTracker.py
# Written By: Matthew Talamantes
# Date: January 11, 2020

import tkinter as tk
import sys
import time
from timer import Timer


def startTimer():
    timer.timerStart()
    timerRun = True

def pauseTimer():
    timer.timerPause()

def stopTimer():
    timer.timerStop()

def updateLabel():
    timeTuple = timer.getTimeTuple()
    timeString = '%02d:%02d:%02d:%02d' % (timeTuple[0], timeTuple[1], timeTuple[2], timeTuple[3])
    label.configure(text=timeString)
    root.after(10, updateLabel)
# main code

timer = Timer()
root = tk.Tk()
timerRun = False
label = tk.Label(root, text='')
startButton = tk.Button(root, text='Start', command=startTimer)
pauseButton = tk.Button(root, text='Pause', command=pauseTimer)
stopButton = tk.Button(root, text='Stop', command=stopTimer)
label.pack()
startButton.pack()
pauseButton.pack()
stopButton.pack()
updateLabel()
root.mainloop()