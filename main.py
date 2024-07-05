from tkinter import *

sample_text = ("apple banana cherry orange grape pineapple strawberry blueberry raspberry mango kiwi peach plum "
               "apricot lemon lime watermelon cantaloupe honeydew grapefruit tangerine pomegranate avocado tomato "
               "cucumber lettuce spinach broccoli cauliflower carrot potato onion garlic mushroom zucchini pepper "
               "radish celery asparagus eggplant pumpkin squash beans peas lentils chickpeas oats rice quinoa barley "
               "wheat corn millet rye buckwheat pasta couscous bread bagel muffin croissant pancake waffle donut "
               "cookie cake pie pudding icecream yogurt cheese butter milk cream juice soda coffee tea water")
sample_word = sample_text.split()
input_time = None
timer = ""
time_remit = 5


def update_progress(event):
    typed_text = text_entry.get("1.0", END).rstrip()

    sample_text_widget.config(state="normal")
    sample_text_widget.delete('1.0', END)

    for i in range(len(sample_text)):
        if i < len(typed_text):
            if typed_text[i] == sample_text[i]:
                sample_text_widget.insert(END, sample_text[i], "correct")
            else:
                sample_text_widget.insert(END, sample_text[i], "incorrect")
        else:
            sample_text_widget.insert(END, sample_text[i], "default")

    sample_text_widget.config(state="disabled")


def start_timer(event):
    global input_time

    if input_time is None:
        input_time = time_remit
        count_down(time_remit)


def count_down(count):
    global timer
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
        Timer_count.config(text=count)

    else:
        stop_timer()


def reset_timer():
    global input_time, timer
    if timer:
        window.after_cancel(timer)
    input_time = None

    Timer_count.config(text=time_remit)

    sample_text_widget.config(state="normal")
    sample_text_widget.delete('1.0', END)
    sample_text_widget.insert(END, sample_text)
    sample_text_widget.config(state="disabled")

    text_entry.config(state="normal")
    text_entry.delete('1.0', END)


def stop_timer():
    calculate_wpm()
    text_entry.config(state="disabled")


def calculate_wpm():
    typed_text = text_entry.get("1.0", END).strip()
    typed_word = typed_text.split()
    word_count = 0
    for i in range(len(typed_word)):
        try:
            if typed_word[i] == sample_word[i]:
                word_count += 1
            else:
                break
        except IndexError:
            break

    result_label.config(text=f"Your typing speed is {word_count} words per minute.")


window = Tk()
window.title("Typing Speed Game")

Timer_title = Label(window, text="Time", wraplength=400, font=("Arial", 14))
Timer_title.pack(pady=5)
Timer_count = Label(window, text=time_remit, wraplength=400, font=("Arial", 28))
Timer_count.pack(pady=5)

sample_text_widget = Text(window, height=8, width=50, wrap='word', font=("Arial", 14))
sample_text_widget.insert(END, sample_text)
sample_text_widget.config(state="disabled")
sample_text_widget.pack(pady=10)

text_entry = Text(window, height=8, width=50, wrap='word', font=("Arial", 14))
text_entry.pack(pady=10)
text_entry.bind("<KeyPress>", start_timer)
text_entry.bind("<KeyRelease>", update_progress)

reset_button = Button(window, text="Reset", command=reset_timer, font=("Arial", 14))
reset_button.pack(pady=10)

result_label = Label(window, text="", wraplength=400, font=("Arial", 14))
result_label.pack(pady=10)

sample_text_widget.tag_configure("correct", foreground="green")
sample_text_widget.tag_configure("incorrect", foreground="red")
sample_text_widget.tag_configure("default", foreground="black")

window.mainloop()
