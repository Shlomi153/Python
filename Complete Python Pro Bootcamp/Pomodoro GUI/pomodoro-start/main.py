#Created By: Shlomi Kiko
#Topic: This program helps manage work and break times, 4 iterations of 20 minute work, 5 minute break, finishing with a longer 25 minute break
#Linkedin: https://www.linkedin.com/in/shlomikiko/

import tkinter as tk;
import math;
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BABYBLUE = "#89CFF0"
FONT_NAME = "Comic Sans MS"

WORK_MIN = 20;
SHORT_BREAK_MIN = 5;
LONG_BREAK_MIN = 25;

repetition = 0;
timer = None;

# ---------------------------- Exit ------------------------------- # 
def exit():
    window.quit();
    window.destroy();

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_label;
    #Stops the timer
    if(timer is not None):
        timer_label.after_cancel(timer);
    #Resets the time
    canvas.itemconfigure(canvas_text, text="00:00");
    #Resets the label and the checkmarks
    timer_label["text"] = "Timer";
    timer_label["fg"] = GREEN; 
    checkmark["text"] = "";
    #Resets the counter, this avoids timer conflicts
    global repetition;
    repetition = 0;

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetition;
    repetition += 1;

    work_min = WORK_MIN * 60;
    short_break = SHORT_BREAK_MIN * 60;
    long_break = LONG_BREAK_MIN * 60;

    if(repetition % 8 == 0):
        timer_label.config(text="Take it easy!", fg=RED);
        countdown(long_break);
    elif(repetition % 2 == 0):
        timer_label.config(text="Short break!", fg=PINK);
        countdown(short_break);
    else:
        timer_label.config(text="Work it!", fg=GREEN);
        countdown(work_min);

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global repetition;

    # If the window has been closed, stop this function immediately
    if not window.winfo_exists():
        return

    count_minutes = math.floor(count / 60);

    if(count_minutes < 10):#Makes sure you get the format 00:00, Math floor already ensures it's an Integer
        count_minutes = f"0{count_minutes}";

    count_seconds = int(count % 60);
    if(count_seconds < 10):#Makes sure you get the format 00:00
        count_seconds = f"0{count_seconds}";
    
    canvas.itemconfigure(canvas_text, text=f"{count_minutes}:{count_seconds}");

    if(count > 0):
        global timer;
        timer = canvas.after(1000, countdown, count - 1);
    else:
        start_timer();

        if(repetition != 1 and repetition % 2 != 0):
            checkmark["text"] += "✔"

# ---------------------------- UI SETUP ------------------------------- #
#Create the Tkinter window
window = tk.Tk();
window.title("Pomodoro");
window.config(padx=100, pady=50, bg=YELLOW);

#Create the Canvas for the image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0);
#Use this class to identify the image location
photo_image = tk.PhotoImage(file="tomato.png");

canvas.create_image(100, 112, image=photo_image);
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"));
canvas.grid(row=1, column=1, padx=20, pady=20);

#Create label for Timer
timer_label = tk.Label(text="Timer", width=13, font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN);
timer_label.grid(row=0, column=1);

#Create buttons for Start and Reset
start_button = tk.Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=BABYBLUE, command=start_timer);
start_button.grid(row=2, column=0);

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=BABYBLUE, command=reset_timer);
reset_button.grid(row=2, column=2);

#Create a Label that keeps track of the repeats
checkmark = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"));
checkmark.grid(row=3, column=1);

#Ensures everything is forced closed on exit to avoid running threads
window.protocol("WM_DELETE_WINDOW", exit);

#Makes sure the GUI stays on the screen and doesn't close right away
window.mainloop();
