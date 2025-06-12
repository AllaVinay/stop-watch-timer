from tkinter import *
import time
def Main():
    global root
    root = Tk()
    root.title("Stopwatch")
    width = 500
    height = 400  # increased height for lap list
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=400)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=400)
    Bottom.pack(side=BOTTOM)
    # Buttons
    Start = Button(Bottom, text='START', command=stopWatch.Start, width=10, height=3)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='STOP', command=stopWatch.Stop, width=10, height=3)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='RESET', command=stopWatch.Reset, width=10, height=3)
    Reset.pack(side=LEFT)
    Lap = Button(Bottom, text='LAP', command=stopWatch.Lap, width=10, height=3)
    Lap.pack(side=LEFT)
    Exit = Button(Bottom, text='CLOSE', command=stopWatch.Exit, width=10, height=3)
    Exit.pack(side=LEFT)
    Title = Label(Top, text="StopWatch", font=("arial", 24), fg="white", bg="black")
    Title.pack(fill=X)
    root.config(bg="black")
    root.mainloop()
class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.lap_count = 0
        self.timestr = StringVar()
        self.MakeWidget()
    def MakeWidget(self):
        # Main stopwatch display
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 45), fg="white", bg="black")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=5, padx=10)
        # Lap Listbox
        self.lapList = Listbox(self, font=("Courier", 12), width=30, height=8)
        self.lapList.pack(pady=5)
    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)
        self.lapList.delete(0, END)  # Clear lap list
        self.lap_count = 0
    def Exit(self):
        root.destroy()
        exit()
    def Lap(self):
        if self.onRunning:
            self.lap_count += 1
            lap_time = self.timestr.get()
            self.lapList.insert(END, f"Lap {self.lap_count}: {lap_time}")
if __name__ == '__main__':
    Main()

