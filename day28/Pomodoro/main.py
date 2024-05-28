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
LONG_BREAK_MIN = 20
reps = 0
timer = None
# one_check_mark = "✔️"
# two_check_mark = "✔️✔️"
# three_check_mark = "✔️✔️✔️"
# four_check_mark = "✔️✔️✔️✔️"
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer",  fg=GREEN )
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    success_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    # 1 * 60
    global reps 
    reps +=1
    work_sec = WORK_MIN * 60
    
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # countdown(5 * 60)
   
    # if reps % 2 != 0:
    #     if countdown(short_break_sec == 0):
    #         start_timer()
    #     if countdown(test_sec == 0):     
    #         start_timer()
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=PINK,  font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break", fg=GREEN,  font=(FONT_NAME, 50, "bold"))
        
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=RED, font=(FONT_NAME, 50, "bold"))
    # if reps == 1:
    #     success_label["text"] = one_check_mark
    # elif reps == 3:
    #     success_label["text"] = two_check_mark
    # elif reps == 5:
    #     success_label["text"] = three_check_mark
    # elif reps == 7:
    #     success_label["text"] = four_check_mark
  
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60 # 100 / 60 = 1 (100 - 60 = 40) 40 is remainder that is basically number of seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔️"
        success_label.config(text=marks)
    # if count_min == 0 and count_sec == 0:
    #     global reps 
    #     reps += 1
    #     start_timer()
    # 300 / 60 = 5
    # 245 / 60 = 4 mnt
    # 245 % 60 =
    # if count_sec == 0:
    #     count_sec = "00"
    # if count_sec ==1:
    #     count_sec = "01"
    # if count_sec ==2:
    #     count_sec = "02"
    # if count_sec ==3:
    #     count_sec = "03"
    # if count_sec ==4:
    #     count_sec = "04"
    # if count_sec ==5:
    #     count_sec = "05"
    # if count_sec ==6:
    #     count_sec = "06"
    # if count_sec ==7:
    #     count_sec = "07"
    # if count_sec ==8:
    #     count_sec = "08"
    # if count_sec ==9:
    #     count_sec = "09"
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)


# def say(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# window.after(1000, say, "Hello", 4, 4)

timer_label = Label(text="Timer", padx=20, pady=20, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"day28\Pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_btn=Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn=Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_btn.grid(column=2, row=2)


success_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
success_label.grid(column=1, row=3)

window.mainloop()