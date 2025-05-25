from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time
import random

import sys
sys.setrecursionlimit(99999999) # Increasing recursion limit so its less likely for errors

#initializing the screen

root = Tk()
root.geometry("1000x1000")
root.title("MathBot")
root.configure(bg='black')

operation = ""
mode_game = ""
answer = 0
time_after_id = 0
time_p1 = 0
time_p2 = 0
p1_correct = ""
p2_correct = ""
pointsp1 = 0
pointsp2 = 0

# Creating the styles

style = ttk.Style()
style.theme_use('clam')


style.configure("Compete.TLabel",
    background="black",
    foreground="lightblue",
    font=("Helvetica", 29, "italic"),
    padding=10)

style.configure("Mathbot.TLabel",
    background="black",
    foreground="white",
    font=("Oswald", 29, "italic"),
    padding=10)


style.configure("Stop.TButton",
    background="black",
    foreground="white",
    font=("Helvetica", 12),
    borderwidth=1,
    padding=(0.5,0.5,0.5,0.5))

style.configure("Operation.TButton",
    background="black",
    foreground="red",
    font=("Oswald", 27),
    borderwidth=0.5,
    padding=10)

style.configure("AfterChoosing.TLabel",
    background="black",
    foreground="white",
    font=("Oswald", 50, "bold"),
    )

style.configure("signs.TLabel",
    background="black",
    foreground="white",
    font=("Oswald", 70, "bold"),
    )


style.configure("timer.TLabel",
    background="black",
    foreground="white",
    font=("Oswald", 50, "bold"),
    )


style.configure("nums.TLabel",
    background="black",
    foreground="silver",
    font=("Georgia", 50, "bold"),
    )

style.configure("partners.TLabel",
    background="black",
    foreground="orange",
    font=("Helvetica", 30),
    )


style.configure("START.TButton",
    background="black",
    foreground="white",
    font=("Helvetica", 24),
    borderwidth=1.5,
    padding=(5,5,5,5))


style.configure("entry.TEntry",
    foreground="black",
    font=("Helvetica", 100),
    padding=(10,5,10,5),
)


style.configure("correct1.TLabel",
    background="black",
    foreground="red",
    font=("Oswald", 30, "bold")
    )

style.configure("final_result.TLabel",
    background="black",
    foreground="lightblue",
    font=("Oswald", 40, "bold")
    )

style.configure("nextround.TLabel",
    background="black",
    foreground="white",
    font=("Oswald", 30))


style.configure("whowon.TLabel",
    background="black",
    foreground="green",
    font=("Oswald", 60, "bold"))



# Creating maps


style.map("Stop.TButton", background=[('active', 'gray20')], foreground=[('active', 'white')])



# Creating the labels

label = ttk.Label(root, text="-    Compete against a partner!", style="Compete.TLabel")
label.place(relx=0.6, rely=0.1, anchor="center")


mathbot_label = ttk.Label(root, text="Mathbot", style="Mathbot.TLabel")
mathbot_label.place(relx=0.32, rely=0.1, anchor="center")


#Creating the text

text_widget = tk.Text(root, height=10, width=50, wrap = "word", borderwidth=0, highlightthickness=0,  bg="black", fg="lightcyan", font=("Helvetica", 24))

num1 = ttk.Label(root, text="Number 1:", style="nums.TLabel")

num2 = ttk.Label(root, text="Number 2:", style="nums.TLabel")

num1p2 = ttk.Label(root, text="Number 1:", style="nums.TLabel")

num2p2 = ttk.Label(root, text="Number 2:", style="nums.TLabel")

next_round = ttk.Label(root, text="", style="nextround.TLabel")

after_choosing_label = ttk.Label(root, text="", style="AfterChoosing.TLabel")



# Timer Label
timer_label1 = ttk.Label(root, text="0.0", style="timer.TLabel")

timer_label2 = ttk.Label(root, text="0.0", style="timer.TLabel")

correct1 = ttk.Label(root, text="", style="correct1.TLabel")
correct2 = ttk.Label(root, text="", style="correct1.TLabel")

final_result = ttk.Label(root, text="", style="final_result.TLabel")

entry = ttk.Entry(root, width=15, style="entry.TEntry", font= ("Helvetica", 25))



# Frame to hold the operation buttons
button_frame = tk.Frame(root, bg="black")
button_frame.place(relx=0.5, rely=0.2, anchor="center")


button2_frame = tk.Frame(root, bg="black")
button2_frame.place(relx=0.5, rely=0.6, anchor="center")


label_frame = tk.Frame(root, bg="black")
label_frame.place(relx=0.5, rely=0.35, anchor="center")

label2_frame = tk.Frame(root, bg="black")
label2_frame.place(relx=0.5, rely=0.75, anchor="center")


button3_frame = tk.Frame(root, bg="black")

label3_frame = tk.Frame(root, bg="black")

ok_button = ttk.Button(root, text="OK!", style="START.TButton", command=lambda: op_screen2())

start_button = ttk.Button(root, text="START!", style="START.TButton", command=lambda: game())


player1_label = ttk.Label(label3_frame, text=f"Player 1", style="partners.TLabel")
player2_label = ttk.Label(label3_frame, text=f"Player 2", style="partners.TLabel")

who_won = ttk.Label(root, text="", style="whowon.TLabel")



def generate_num(p):
    global operation
    global answer
    if p == 0:
        num1.place(relx=0.275, rely=0.55, anchor="center")
        num2.place(relx=0.275, rely=0.65, anchor="center")
    if p == 1:
        num1p2.place(relx=0.725, rely=0.55, anchor="center")
        num2p2.place(relx=0.725, rely=0.65, anchor="center")

    if operation == "Adding":

        test_num1 = random.randint(100,200)
        test_num2 = random.randint(100,200)
        while test_num2 == test_num1:
            test_num2=random.randint(100,200)

        if p == 0:

            num1.config(text=f"Number 1: {str(test_num1)}")
            num2.config(text=f"Number 2: {str(test_num2)}")

        if p == 1:

            num1p2.config(text=f"Number 1: {str(test_num1)}")
            num2p2.config(text=f"Number 2: {str(test_num2)}")


        answer = test_num1+test_num2
    
    if operation == "Subtracting":

        test_num1 = random.randint(150,250)
        test_num2 = random.randint(100,200)
        while test_num2 >= test_num1:
            test_num2=random.randint(100,200)


        if p == 0:

            num1.config(text=f"Number 1: {str(test_num1)}")
            num2.config(text=f"Number 2: {str(test_num2)}")

        if p == 1:

            num1p2.config(text=f"Number 1: {str(test_num1)}")
            num2p2.config(text=f"Number 2: {str(test_num2)}")       

        answer = test_num1-test_num2


    if operation == "Multiplying":

        test_num1 = random.randint(2,20)
        test_num2 = random.randint(2,20)
        while test_num2 == test_num1:
            test_num2=random.randint(2,20)


        if p == 0:

            num1.config(text=f"Number 1: {str(test_num1)}")
            num2.config(text=f"Number 2: {str(test_num2)}")

        if p == 1:

            num1p2.config(text=f"Number 1: {str(test_num1)}")
            num2p2.config(text=f"Number 2: {str(test_num2)}")
        answer = test_num1*test_num2


    if operation == "Dividing":

        test_num1 = random.randint(100,200)
        test_num2 = random.randint(10,30)
        
        while test_num2 == test_num1:
            test_num2=random.randint(10,100)

        answer = test_num1/test_num2

        while answer.is_integer() == False:
            test_num1 = random.randint(100,200)
            test_num2 = random.randint(10,100)
            answer = test_num1/test_num2


        answer = test_num1/test_num2


        if p == 0:

            num1.config(text=f"Number 1: {str(test_num1)}")
            num2.config(text=f"Number 2: {str(test_num2)}")

        if p == 1:

            num1p2.config(text=f"Number 1: {str(test_num1)}")
            num2p2.config(text=f"Number 2: {str(test_num2)}")



times = 0

rounds = 1

def actual_game():
    global time_after_id
    global time_p1
    global time_p2
    global rounds

    start_button.place_forget()

    if times  <= 1:

        countdown = ttk.Label(root, text="3", style="signs.TLabel")

        if times == 0:
            countdown.place(relx=0.275, rely=0.45, anchor="center")
        if times == 1:
            countdown.place(relx=0.725, rely=0.45, anchor="center")

        start_time = 0

        def update_countdown(i):
            if i > 0:
                countdown.config(text=str(i))
                root.after(1000, lambda: update_countdown(i - 1))
            else:
                countdown.place_forget()
                generate_num(times)
                
                entry.delete(0, tk.END)
                if times == 0:
                    entry.place(relx=0.275, rely = 0.75, anchor = "center")

                if times == 1:
                    entry.place(relx=0.725, rely = 0.75, anchor = "center")
                
                entry.unbind("<Return>")

                entry.bind("<Return>", stop_timer)

                entry.focus()


                start_timer()
            
        def start_timer():
            if times == 0:
                timer_label1.place(relx=0.275, rely=0.45, anchor="center")

            if times == 1:
                timer_label2.place(relx=0.725, rely=0.45, anchor="center")

            nonlocal start_time
            start_time = time.time()


            def update_timer():
                global time_after_id

                elapsed = time.time() - start_time
                if times == 0:
                    timer_label1.config(text=f"{elapsed:.2f}")
                    time_after_id = timer_label1.after(10, update_timer)

                if times == 1:
                    timer_label2.config(text=f"{elapsed:.2f}")
                    time_after_id = timer_label2.after(10, update_timer)

            update_timer()


        def stop_timer(event=None):

            global times

            if (entry.get() != "") and ((entry.get()).isdigit() == True):
                nonlocal start_time
                global times
                global answer
                global time_p1
                global time_p2
                global p1_correct
                global p2_correct
                
                if time_after_id is not None:
                    if times == 0:
                        timer_label1.after_cancel(time_after_id)
                        time_p1 = round((time.time() - start_time), 2)
                        timer_label1.config(text=f"{time_p1:.2f}")
                    if times == 1:
                        timer_label2.after_cancel(time_after_id)
                        time_p2 = round((time.time() - start_time), 2)
                        timer_label2.config(text=f"{time_p2:.2f}")


                user_input = int(entry.get())
                entry.place_forget()

                if user_input == answer:
                    if times == 0:
                        correct1.place(relx = 0.275, rely = 0.75, anchor = "center")
                        correct1.config(text=f"{user_input} is correct!", foreground="green", background="black")
                        p1_correct = "YES"
                    if times == 1:
                        correct2.place(relx = 0.725, rely = 0.75, anchor = "center")
                        correct2.config(text=f"{user_input} is correct!", foreground="green", background="black")
                        p2_correct = "YES"

                else:
                    if times == 0:
                        correct1.place(relx=0.275, rely = 0.75, anchor = "center")
                        correct1.config(text=f"{user_input} is incorrect", foreground="red", background= "black")
                        p1_correct = "NO"

                    if times == 1:
                        correct2.place(relx=0.725, rely = 0.75, anchor = "center")
                        correct2.config(text=f"{user_input} is incorrect", foreground="red", background= "black")
                        p2_correct = "NO"

                
                if times == 0:
                    start_button.place(relx=0.725, rely=0.45, anchor="center")

                if times == 1:
                    global rounds
                    global pointsp1
                    global pointsp2

                    final_result.place(relx=0.5, rely=0.825, anchor="center")
                    if p1_correct == "YES" and p2_correct == "NO":
                        final_result.config(text="Player 1 wins!")
                        pointsp1+=1
                    if p1_correct == "NO" and p2_correct == "YES":
                        final_result.config(text="Player 2 wins!")
                        pointsp2+=1

                    if (p1_correct == "YES" and p2_correct == "YES") or (p1_correct=="NO" and p2_correct=="NO"):
                        if time_p1 < time_p2:
                            final_result.config(text="Player 1 won because they were faster!")
                            pointsp1+=1
                        elif time_p2 < time_p1:
                            final_result.config(text="Player 2 won because they were faster!")
                            pointsp2+=1
                        elif time_p1 == time_p2:
                            final_result.config(text="It's a draw!")
                            pointsp1+=1
                            pointsp2+=1

                    if mode_game == "Best of 3":
                        player1_label.config(text=f"Player 1 ({pointsp1})")
                        player2_label.config(text=f"Player 2 ({pointsp2})")

                    rounds += 1

                entry.unbind("<Return>")

                times += 1

            
            elif (entry.get() != "") and (entry.get().isdigit() != True):
                if times == 0:
                    correct1.place(relx=0.275, rely = 0.85, anchor = "center")
                    correct1.config(text=f"Please enter a valid input", foreground="red", background= "black")

                if times == 1:
                    correct2.place(relx=0.725, rely = 0.85, anchor = "center")
                    correct2.config(text=f"Please enter a valid input", foreground="red", background= "black")


            elif entry.get() == "":
                if times == 0:
                    correct1.place(relx=0.275, rely = 0.85, anchor = "center")
                    correct1.config(text=f"Please enter something", foreground="red", background= "black")

                if times == 1:
                    correct2.place(relx=0.725, rely = 0.85, anchor = "center")
                    correct2.config(text=f"Please enter something", foreground="red", background= "black")
            

        
        update_countdown(3)

def game():
    global times
    global pointsp1
    global pointsp2


    if mode_game == "Single Match":
        actual_game()

    elif mode_game == "Best of 3":

        def play_round():
            actual_game()
            check_round_end()


        def check_round_end():

            global pointsp1
            global pointsp2
            if times < 2:
                # Wait until both players finish (times == 2)
                root.after(500, check_round_end)
            else:
                if rounds != 4:
                    show_next_round_countdown()
                elif rounds == 4:
                    who_won.place(relx=0.5, rely=0.9, anchor="center")
                    if pointsp1 > pointsp2:
                        who_won.config(text=f"Player 1 won {pointsp1}-{pointsp2}!")
                    if pointsp2 > pointsp1:
                        who_won.config(text=f"Player 2 won {pointsp2}-{pointsp1}!")
                    if pointsp2 == pointsp1:
                        who_won.config(text=f"It's a tie! {pointsp1}-{pointsp2}!") #extraordinarily rare situation


        def show_next_round_countdown():
            global times

            countdown_time = 10

            def update_countdown2(i):
                if i > 0:
                    next_round.place(relx=0.5, rely=0.9, anchor="center")
                    next_round.config(text=f"Next round starting in {i}")
                    root.after(1000, lambda: update_countdown2(i - 1))
                else:
                    next_round.place_forget()
                    reset_round()

            def reset_round():
                global times, p1_correct, p2_correct, time_p1, time_p2
                times = 0
                p1_correct = ""
                p2_correct = ""
                time_p1 = 0
                time_p2 = 0

                final_result.place_forget()
                correct1.place_forget()
                correct2.place_forget()
                timer_label1.place_forget()
                timer_label2.place_forget()
                num1.place_forget()
                num2.place_forget()
                num1p2.place_forget()
                num2p2.place_forget()

                start_button.place(relx=0.275, rely=0.45, anchor="center")



            update_countdown2(countdown_time)


        play_round()


def op_screen2():
    global pointsp1
    global pointsp2

    ok_button.place_forget()
    text_widget.place_forget()

    label3_frame.place(relx=0.5, rely=0.35, anchor="center")


    start_button.place(relx=0.275, rely=0.45, anchor="center")


    text_widget.config(state="disabled")


    player1_label.pack(side=LEFT, padx=150)
    player2_label.pack(side=LEFT, padx=150)
    

def op_screen(mode):

    global operation
    global mode_game
    mode_game = mode

    button3_frame.place_forget()

    text_widget.place(relx=0.5, rely=0.5, anchor="center")


    if operation == "Adding":
        text_widget.insert(tk.END, "You will be given 2 numbers, number 1 and number 2. You will need to add both the numbers, input the answer into the textbox as fast as you can, click enter, and whoever gets it correct the fastest wins! If both are incorrect, the faster one wins.")

    if operation == "Subtracting":
        text_widget.insert(tk.END, "You will be given 2 numbers, number 1 and number 2. You will need to subtract number1 - number2, input the answer into the textbox as fast as you can, click enter, and whoever gets it correct the fastest wins! If both are incorrect, the faster one wins.")

    if operation == "Multiplying":
        text_widget.insert(tk.END, "You will be given 2 numbers, number 1 and number 2. You will need to multiply both the numbers, input the answer into the textbox as fast as you can, click enter, and whoever gets it correct the fastest wins! If both are incorrect, the faster one wins.")

    if operation == "Dividing":
        text_widget.insert(tk.END, "You will be given 2 numbers, number 1 and number 2. You will need to divide number1/number2, input the answer into the textbox as fast as you can, click enter, and whoever gets it correct the fastest wins! If both are incorrect, the faster one wins.")

    text_widget.config(state="disabled")


    ok_button.place(relx=0.5, rely=0.6, anchor="center")




def execute(op):

    global operation 
    operation = op

    button_frame.place_forget()
    button2_frame.place_forget()
    label_frame.place_forget()
    label2_frame.place_forget()
    button3_frame.place(relx=0.5, rely=0.35, anchor="center")

    options = ["Single Match", "Best of 3"]

    for loop in options:
        b = ttk.Button(button3_frame, text=loop, style="Operation.TButton", command=lambda mode=loop: op_screen(mode))
        b.pack(side=LEFT, padx=5)
    after_choosing_label.config(text = op)
    after_choosing_label.place(relx=0.5, rely=0.2, anchor="center")





# Four operation buttons
operations = ["Adding", "Subtracting"]

operations2 = ["Multiplying", "Dividing"]

operations3 = ["+        ", "       -"]

operations4 = ["x        ", "       /"]


for loop_op in operations:
    # we are game captured_op=loop_op so that the specific operation matches each button so during execution it calls the proper function
    b = ttk.Button(button_frame, text=loop_op, style="Operation.TButton", command=lambda captured_op=loop_op: execute(captured_op))
    b.pack(side=LEFT, padx=5)

for loop_op in operations2:
    b = ttk.Button(button2_frame, text=loop_op, style="Operation.TButton", command=lambda captured_op=loop_op: execute(captured_op))
    b.pack(side=LEFT, padx=5)

for loop_op in operations3:
    b = ttk.Label(label_frame, text=loop_op, style="signs.TLabel")
    b.pack(side=LEFT, padx=5)


for loop_op in operations4:
    b = ttk.Label(label2_frame, text=loop_op, style="signs.TLabel")
    b.pack(side=LEFT, padx=5)


# Stop button
stop_button = ttk.Button(root, text="Exit Program", style="Stop.TButton", command=root.destroy)
stop_button.place(relx=0.94, rely=0.025, anchor="center")

root.mainloop()
