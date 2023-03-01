from tkinter import *
import time
from playsound import playsound

CLEAR = "\033[2j"
CLEAR_AND_RETURN = "\033[H"

def alarm(minutes, seconds):
    time_elapsed = 0
    total_seconds = minutes * 60 + seconds

    print(CLEAR)
    while time_elapsed < total_seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = total_seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        timer_label.config(text=f"{minutes_left:02d}:{seconds_left:02d}")
        root.update()

    playsound("Alarm-Fast-A1-www.fesliyanstudios.com.mp3")
    timer_label.config(text="00:00")

root = Tk()
root.title("Alarm")
root.geometry("300x150")

minutes_entry = Entry(root, width=3)
minutes_entry.pack(side=LEFT, padx=10)

seconds_entry = Entry(root, width=3)
seconds_entry.pack(side=LEFT)

timer_label = Label(root, text="00:00", font=("Arial", 30))
timer_label.pack(pady=20)

start_button = Button(root, text="Start", command=lambda: alarm(int(minutes_entry.get()), int(seconds_entry.get())))
start_button.pack()

root.mainloop()
