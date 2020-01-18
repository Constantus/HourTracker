# HourTracker.py
# Written By: Matthew Talamantes
# Date: January 11, 2020

import tkinter as tk
import sys
import time
from timer import Timer


def startPauseTimer():
    global timerStatus
    if timerStatus == 'paused' or timerStatus == '':
        timer.timerStart()
        startButton.configure(text='Pause')
        timerStatus = 'running'
    elif timerStatus == 'running':
        timer.timerPause()
        startButton.configure(text='Start')
        timerStatus = 'paused'


def stopTimer():
    global timerStatus
    if timerStatus != '':
        timer.timerStop()
        if timerStatus == 'running':
            startButton.configure(text='Start')
        timerStatus = 'stopped'

def updateLabel():
    timeTuple = timer.getTimeTuple()
    timeString = '%02d:%02d:%02d:%02d' % (timeTuple[0], timeTuple[1], timeTuple[2], timeTuple[3])
    label.configure(text=timeString)
    root.after(10, updateLabel)

def resetTimer():
    global timerStatus
    timer.timerReset()
    if timerStatus == 'running' or timerStatus == 'stopped':
        startButton.configure(text='Start')
    timerStatus = ''

# To-Do: Get and do something with the hours returned by timer.timerStop()
# Add a timerReset button and then also a timer save button and the logic that goes with it.

# main code
timer = Timer()
timerStatus = ''
root = tk.Tk()
label = tk.Label(root, text='')
startButton = tk.Button(root, text='Start', command=startPauseTimer)
stopButton = tk.Button(root, text='Stop', command=stopTimer)
resetButton = tk.Button(root, text='Reset', command=resetTimer)
label.pack()
startButton.pack()
stopButton.pack()
resetButton.pack()
updateLabel()
root.mainloop()