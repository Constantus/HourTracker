# trackerGui.py
# Written By: Matthew Talamantes
# Date: January 18, 2020

import tkinter as tk
from timer import Timer

class TrackerGui():
    def __init__(self):
        self.timer = Timer()
        self.timerStatus = ''
        self.root = tk.Tk()
        self.timerLabel = tk.Label(self.root, text='')
        self.startButton = tk.Button(self.root, text = 'Start', command=self.startPauseTimer)
        self.stopButton = tk.Button(self.root, text='Stop', command=self.stopTimer)
        self.resetButton = tk.Button(self.root, text='Reset', command=self.resetTimer)
        self.timerLabel.pack()
        self.startButton.pack()
        self.stopButton.pack()
        self.resetButton.pack()
        self.updateTimer()
        self.root.mainloop()

    
    def startPauseTimer(self):
        """Starts the timer if it isn't currently running, pauses it if it is."""
        if self.timerStatus == '' or self.timerStatus == 'paused':
            self.timer.timerStart()
            self.startButton.configure(text='Pause')
            self.timerStatus = 'running'
        elif self.timerStatus == 'running':
            self.timer.timerPause()
            self.startButton.configure(text='Start')
            self.timerStatus = 'paused'

        
    def stopTimer(self):
        """Stops the timer if it has been started."""
        if self.timerStatus != '':
            self.timer.timerStop()
            
            if self.timerStatus == 'running':
                self.startButton.configure(text='Start')
            
            self.timerStatus = 'stopped'


    def resetTimer(self):
        """Resets the timer."""
        self.timer.timerReset()
        
        if self.timerStatus == 'running' or self.timerStatus == 'stopped':
            self.startButton.configure(text='Start')

        self.timerStatus = ''


    def updateTimer(self):
        """Gets the tuple of the time on the timer and updates the timer label to it."""
        timeTuple = self.timer.getTimeTuple()
        timeString = '%02d:%02d:%02d:%02d' % (timeTuple[0], timeTuple[1], timeTuple[2], timeTuple[3])
        self.timerLabel.configure(text=timeString)
        self.root.after(10, self.updateTimer)