# trackerGui.py
# Written By: Matthew Talamantes
# Date: January 18, 2020

import tkinter as tk
from timer import Timer

class TrackerGui():
    def __init__(self):
        
        # Initialize timer and timerStatus
        self.timer = Timer()
        self.timerStatus = ''

        # Initialize root window and top level frames and top level widgets
        self.root = tk.Tk()
        self.timerControls = tk.Frame(self.root)
        self.timerContainer = tk.Frame(self.root)

        # Initialize Project label and timer.
        self.projectLabel = tk.Label(self.timerContainer, text='ProjectName')
        self.timerPrintOut = tk.Label(self.timerContainer, text='', font=('Courier', 30))
        self.projectLabel.grid(row=0, column=0, pady=2, sticky='W')
        self.timerPrintOut.grid(row=1, columnspan=5, sticky='W')

        # Initialize the timer control buttons.
        self.startButton = tk.Button(self.timerControls, text = 'Start', command=self.startPauseTimer)
        self.stopButton = tk.Button(self.timerControls, text='Stop', command=self.stopTimer)
        self.resetButton = tk.Button(self.timerControls, text='Reset', command=self.resetTimer)
        self.startButton.grid(row=0, column=0, padx=5)
        self.stopButton.grid(row=0, column=1, padx=5)
        self.resetButton.grid(row=0, column=2, padx=5)

        # Pack top level frames and widgets and start mainloop
        self.timerContainer.pack()
        self.timerControls.pack()
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
        self.timerPrintOut.configure(text=timeString)
        self.root.after(10, self.updateTimer)