# timer.py
# Written By: Matthew Talamantes
# Date: January 11, 2020
# Definition of the class Timer

from datetime import datetime as dt

class Timer():
    def __init__(self):
        self.instanceTime = 0.0
        self.status = 'stopped'

    def getTimeString(self, timeStamp):
        '''For internal use, takes a timestamp as an argument and returns the formatted string.
        In format HH:MM:SSAM/PM'''
        datetimeObject = dt.fromtimestamp(timeStamp)
        timeString = datetimeObject.strftime("%I:%M:%S%p")
        return timeString

    def timerStart(self):
        '''Starts the timer. Creates a startTime class variable that is the timestamp of when the method was called.
        Returns the time it was started.'''
        if self.status != 'running':
            self.startTime = dt.now().timestamp()
            self.status = 'running'
            startString = self.getTimeString(self.startTime)
            return startString
        else:
            # Do nothing
            pass
    

    def timerPause(self):
        '''Pauses the timer. But is able to restart when ready, adding to the instanceTime.
        Returns the time it was paused.'''
        if self.status == 'running':
            currentTime = dt.now().timestamp()
            timeDifference = currentTime - self.startTime
            self.instanceTime += timeDifference
            self.status = 'paused'
            pausedString = self.getTimeString(currentTime)
            return pausedString
        else:
            # Do nothing
            pass
    

    def timerStop(self):
        '''Stops the timer, returning an array of the final instance time in hours and 
        if the timer was still running the time it stopped. and resetting the instance time to 0.0.'''
        stopString = ''
        if self.status == 'running':
            currentTime = dt.now().timestamp()
            timeDifference = currentTime - self.startTime
            self.instanceTime += timeDifference
            stopString = self.getTimeString(currentTime)
        self.status = 'stopped'
        finalTimeSeconds = self.instanceTime
        finalTime = (finalTimeSeconds / 60) / 60
        if stopString != '':
            returnArray = [finalTime, stopString]
        else:
            returnArray = [finalTime]
        return returnArray

    def timerReset(self):
        '''Resets the timer.'''

        self.__init__()

    def getTimeTuple(self):
        '''Returns a tuple of the hours, minutes, seconds, milliseconds on the timer.'''
        if self.status == 'running':
            currentTime = dt.now().timestamp()
            timeDifference = currentTime - self.startTime
            tempInstanceTime = self.instanceTime + timeDifference
        else:
            tempInstanceTime = self.instanceTime

        timerMillisec = int((tempInstanceTime % 1) * 100)
        timerSec = int(tempInstanceTime % 60)
        timerMinute = int(tempInstanceTime // 60)
        timerHour = timerMinute // 60
        timeTuple = (timerHour, timerMinute, timerSec, timerMillisec)
        return timeTuple

    def getStatus(self):
        return self.status
