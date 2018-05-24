from Tkinter import *
import time

class Timer:

	rate = 17.	# hourly rate

	# start or pause timer if space is pressed
	def space(self, event):
		if(self.start_time != None):
			self.pauseTimer()
		else:
			self.startTimer()

	def updateTime(self):
		# set time label to storedSeconds + (now - start_time) (if start_time is not None)
		totalSec = self.storedSeconds
		#print self.storedSeconds
		if(self.start_time != None):
			totalSec += int(time.time() - self.start_time)
		hr = int(totalSec)/3600
		mn = (int(totalSec)/60)%60
		sc = int(totalSec)%60
		self.timestr.set('{0:02d}:{1:02d}:{2:02d}'.format(hr,mn,sc))
		self.moneystr.set('${0:.2f}'.format(self.rate*totalSec/3600.))	# divide by 3600 to get hours worked
		self.frame.after(1000, self.updateTime)

	def startTimer(self):
		if(self.start_time == None):
			self.start_time = time.time()
		self.startButton.config(state=DISABLED)
		self.pauseButton.config(state=NORMAL)
		self.endButton.config(state=NORMAL)
		self.frame.title('Tiny Timer (running)')

	def pauseTimer(self):
		# add seconds elapsed since start was hit to storedSeconds
		if(self.start_time != None):
			self.storedSeconds += int(time.time() - self.start_time)
		self.start_time = None
		self.startButton.config(state=NORMAL)
		self.pauseButton.config(state=DISABLED)
		self.endButton.config(state=NORMAL)
		self.frame.title('Tiny Timer (paused)')

	def endTimer(self):
		self.pauseTimer()
		# disable start and pause buttons
		self.startButton.config(state=DISABLED)
		self.pauseButton.config(state=DISABLED)
		self.endButton.config(state=DISABLED)

	def __init__(self):
		# generate the window
		self.running = False
		self.frame = Tk()
		#self.frame = Frame(self.root, width=400, height=240)
		self.timestr = StringVar()
		self.moneystr = StringVar()
		self.frame.title('Tiny Timer')
		self.start_time = None
		self.storedSeconds = 0
		self.timeLabel = Label(self.frame, textvariable=self.timestr)
		self.moneyLabel = Label(self.frame, textvariable=self.moneystr)
		self.startButton = Button(self.frame, text="Start", command=self.startTimer)
		self.pauseButton = Button(self.frame, text="Pause", command=self.pauseTimer, state=DISABLED)
		self.endButton = Button(self.frame, text="End", command=self.endTimer, state=DISABLED)

	def buildWindow(self):
		self.timeLabel.grid(row=0, column=0, columnspan=3)
		#self.moneyLabel.grid(row=0, column=2)
		self.startButton.grid(row=1, column=0)
		self.pauseButton.grid(row=1, column=1)
		self.endButton.grid(row=1, column=2)

	def newTimer(self):
		self.buildWindow()
		self.timestr.set('00:00:00')
		self.moneystr.set('$0.00')
		self.frame.bind("<space>", self.space)	# space bar pausing
		# define repeating function to update timer
		self.frame.after(1000, self.updateTime)
		self.frame.mainloop()

if __name__ == '__main__':
	timer = Timer()
	timer.newTimer()