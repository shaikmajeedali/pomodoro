from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#fae588"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = None

# Reset time
def reset():
    panel.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lable.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0




# timer mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brek_sec = SHORT_BREAK*60
    long_sec = LONG_BREAK *60

        # if reps 8
    if reps % 8 == 0:
        count_down(long_sec)
        lable.config(text="Long Break", fg=RED)
        # if reps 2,4,6
    elif reps % 2 == 0:
        count_down(short_brek_sec)
        lable.config(text="Short Break", fg=RED)
    else:
        # if reps 1,3,5,7
        count_down(work_sec)
        lable.config(text="Work", fg=GREEN)



# add a count mechanism\
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = panel.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        label_check.config(text=mark)


# UI Setup
panel = Tk()
panel.title("Pomodoro")
panel.config(padx=100, pady=50, bg=YELLOW)

lable = Label(text="Timer", bg=YELLOW)
lable.config(font=(FONT_NAME, 45, "bold"), fg=GREEN)
lable.grid(column=1, row=0)

canvas = Canvas(height=225, width=208, bg=YELLOW, highlightthickness=0)
tomo_img = PhotoImage(file="tomato.png")
img = canvas.create_image(105, 112, image=tomo_img)
timer_text = canvas.create_text(103, 112, text="00:00", font=(FONT_NAME, 36, "bold"), fill="white", )
canvas.grid(column=1, row=1)

button = Button(text="start", highlightthickness=0, command=start_timer)
button.grid(column=0, row=2)

button_end = Button(text="Reset", highlightthickness=0, command=reset)
button_end.grid(column=2, row=2)

label_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
label_check.grid(column=1, row=3)




panel.mainloop()
