# trackerGui.py
# Written By: Matthew Talamantes
# Date: January 18, 2020

import tkinter as tk
from tkinter import messagebox, ttk
from timer import Timer

# To-Do:
#   -Add rest of file menu and logic
#   -Add save and quit logic to their functions. 
#   -Add confirmation message if user quits or resets the timer, perhaps also before a user stops the timer.

class TrackerGui():
    def __init__(self):
        
        # Initialize timer and timerStatus
        self.timer = Timer()
        self.timerStatus = ''
        self.recordList = []
        self.timeList = []
        self.totalHours = 0.0

        # Initialize root window and top level frames and top level widgets
        self.root = tk.Tk()
        self.root.title('Hour Tracker')
        self.menubar = tk.Menu(self.root)
        self.timerControls = tk.Frame(self.root)
        self.timerContainer = tk.Frame(self.root)
        self.taskInfoContainer = tk.Frame(self.root)

        # Initialize menu bar
        fileMenu = tk.Menu(self.menubar, tearoff=0)
        fileMenu.add_command(label='New Task', command=self.createNewTask)
        self.menubar.add_cascade(label='File', menu=fileMenu)

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

        # Initialize the task info text fields.
        self.taskLabel = tk.Label(self.taskInfoContainer, text='Task Name:')
        self.taskName = tk.Entry(self.taskInfoContainer)
        self.descriptionLabel = tk.Label(self.taskInfoContainer, text='Task Description:')
        self.taskDescription = tk.Text(self.taskInfoContainer, height=5)
        self.scrollbar = ttk.Scrollbar(self.taskInfoContainer, orient = 'vertical', command = self.taskDescription.yview)
        self.scrollbar.grid(column=5, row=3, sticky='NS')
        self.taskDescription.config(yscrollcommand = self.scrollbar.set)
        self.saveContainer = tk.Frame(self.taskInfoContainer)
        self.quitButton = tk.Button(self.saveContainer, text='Quit', command=self.quitTracker)
        self.saveButton = tk.Button(self.saveContainer, text='Save', command=self.saveTracker)
        self.taskLabel.grid(row=0, column=0, pady=2, sticky='W')
        self.taskName.grid(row=1, columnspan=5, pady=2, padx=3, sticky='W')
        self.descriptionLabel.grid(row=2, column=0, pady=2, sticky='W')
        self.taskDescription.grid(row=3, columnspan=5, pady=2, padx=3, sticky='W')
        self.quitButton.grid(row=0, column=0, pady=2, padx=3, sticky='E')
        self.saveButton.grid(row=0, column=1, pady=2, padx=3, sticky='E')
        self.saveContainer.grid(row=4, column=4, sticky='E')

        # Pack top level frames and widgets and start mainloop
        self.root.config(menu=self.menubar)
        self.timerContainer.pack()
        self.timerControls.pack()
        self.taskInfoContainer.pack()
        self.updateTimer()
        self.root.mainloop()


    def convertList(self):
        """Takes the self.timeList, converts it to a tuple and adds it to the 
        self.recordList. It then resets the self.timeList."""
        timeList = self.timeList
        timeTuple = tuple(timeList)
        self.recordList.append(timeTuple)
        self.timeList = []

    
    def startPauseTimer(self):
        """Starts the timer if it isn't currently running, pauses it if it is."""
        if self.timerStatus == '' or self.timerStatus == 'paused':
            startTime = self.timer.timerStart()
            self.startButton.configure(text='Pause')
            self.timerStatus = 'running'
            self.timeList.append(startTime)
        elif self.timerStatus == 'running':
            pauseTime = self.timer.timerPause()
            self.startButton.configure(text='Start')
            self.timerStatus = 'paused'
            self.timeList.append(pauseTime)
            self.convertList()

        
    def stopTimer(self):
        """Stops the timer if it has been started."""
        if self.timerStatus != '' and self.timerStatus != 'stopped':

            msgBox = tk.messagebox.askquestion('Stop Timer', 'Are you sure you want to start the timer? You will have to start a new task to restart it!', icon = 'warning')
            if msgBox == 'yes':
                stopArray = self.timer.timerStop()
                
                if self.timerStatus == 'running':
                    self.startButton.configure(text='Start')
                
                self.timerStatus = 'stopped'

                if len(stopArray) > 1:
                    self.totalHours = stopArray[0]
                    self.timeList.append(stopArray[1])
                    self.convertList()
                else:
                    self.totalHours = stopArray[0]


    def resetTimer(self):
        """Resets the timer."""

        msgBox = tk.messagebox.askquestion('Reset Timer', 'Are you sure you want to reset the timer and clear the fields?', icon = 'warning')
        if msgBox == 'yes':
            self.timer.timerReset()
            self.taskName.delete(0, 'end')
            self.taskDescription.delete('1.0', 'end -1 chars')
            
            if self.timerStatus == 'running' or self.timerStatus == 'stopped':
                self.startButton.configure(text='Start')

            self.timerStatus = ''


    def createNewTask(self):
        pass


    def updateTimer(self):
        """Gets the tuple of the time on the timer and updates the timer label to it."""
        timeTuple = self.timer.getTimeTuple()
        timeString = '%02d:%02d:%02d:%02d' % (timeTuple[0], timeTuple[1], timeTuple[2], timeTuple[3])
        self.timerPrintOut.configure(text=timeString)
        self.root.after(10, self.updateTimer)

    
    def quitTracker(self):
        msgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit? (Unsaved data will be lost!)', icon = 'warning')
        if msgBox == 'yes':
            self.root.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen.')

    
    def saveTracker(self):
        taskNameStr = self.taskName.get()
        taskDescriptionStr =self.taskDescription.get("1.0", 'end-1c')
        print(taskNameStr)
        print(taskDescriptionStr)