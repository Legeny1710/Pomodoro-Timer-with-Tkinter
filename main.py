from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    title["text"] = "Timer"
    title["fg"] = GREEN
    check_mark["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        title["text"] = "Long Break"
        title["fg"] = "blue"
    elif reps % 2 == 0:
        count_down(short_sec)
        title["text"] = "Short Break"
        title["fg"] = RED
    else:
        count_down(work_sec)
        title["text"] = " Focus"
        title["fg"] = GREEN




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        # work_sessions = math.floor(reps/2)
        marks = ""
        if reps % 2 == 0:
            marks += "✔"
        check_mark["text"] += marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Focus")
window.config(pady=100, padx=70)

canvas = Canvas(width=210, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato_img)
timer_text = canvas.create_text(104, 130, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=2)


# title
title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN)
title.grid(column=2, row=1, pady=10, padx=10)

#buttons
start_btn = Button(text="START", font=(FONT_NAME, 15), command=start_time)
start_btn.grid(column=1, row=3)

reset_btn = Button(text="RESET", font=(FONT_NAME, 15), command=reset)
reset_btn.grid(column=3, row=3)

# check_mark
check_mark = Label(text="", font=(FONT_NAME, 30), fg=GREEN)
check_mark.grid(column=2, row=3, pady=20)

##################################################################
# Loop to keep screen open
window.mainloop()