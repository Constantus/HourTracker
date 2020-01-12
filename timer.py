# timer.py
# Written By: Matthew Talamantes
# Date: January 11, 2020
# Definition of the class Timer

from datetime import datetime as dt

class Timer():
    def __init__(self):
        self.instanceTime = 0.0
        self.timeObject = None
        self.status = 'stopped'

    
    def timerStart(self):
        '''Starts the timer. Creates a startTime class variable that is the timestamp of when the method was called.'''
        if self.status != 'running':
            self.startTime = dt.now().timestamp()
            self.status = 'running'
        else:
            # Do nothing
            pass
    

    def timerPause(self):
        '''Pauses the timer. But is able to restart when ready, adding to the instanceTime.'''
        if self.status == 'running':
            currentTime = dt.now().timestamp()
            timeDifference = currentTime - self.startTime
            self.instanceTime += timeDifference
            self.status = 'paused'
        else:
            # Do nothing
            pass
    

    def timerStop(self):
        '''Stops the timer, returning the final instance time and resetting the instance time to 0.0.'''
        if self.status == 'running':
            currentTime = dt.now().timestamp()
            timeDifference = currentTime - self.startTime
            self.instanceTime += timeDifference
        elif self.status == 'paused':
            # Do Nothing Remove if unnecessary
            pass
        else:
            # Do Nothing
            pass
        self.status = 'stopped'
        finalTime = self.instanceTime
        self.instanceTime = 0.0
        return finalTime

    def getTimeTuple(self):
        '''Returns a tuple of the hours, minutes, seconds, milliseconds on the timer.'''
        if self.status == 'running':
            currentTime = dt.now().timestamp()
            timeDifference = currentTime - self.startTime
            tempInstanceTime = self.instanceTime + timeDifference
        elif self.status == 'paused':
            tempInstanceTime = self.instanceTime
        else: 
            # Throw error
            pass

        timerMillisec = int((tempInstanceTime % 1) * 100)
        timerSec = int(tempInstanceTime % 60)
        timerMinute = int(tempInstanceTime // 60)
        timerHour = timerMinute // 60
        timeTuple = (timerHour, timerMinute, timerSec, timerMillisec)
        return timeTuple

    def getStatus(self):
        return self.status
