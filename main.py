from words import words
from tkinter import *
import random


# create function to highlight word to type
def add_highlight():
    index_two = len(words[0])
    word_list.tag_add("start", "1.0", f"1.{index_two}")
    word_list.tag_config("start", background="green", foreground="white")


# create counter
def countdown(count):
    # change text in label
    timer['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count - 1)
    else:
        length = 0
        for element in correct_list:
            length += len(element)
        word_list.delete("1.0", "end")
        word_list.insert(END, f"Words per min(WPM): {len(correct_list)}\n"
                              f"Characters per min(CPM): {length}\n"
                              f"You typed {len(wrong_list)} words incorrectly.")
        word_list.config(state=DISABLED)
        typed_word.pack_forget()


# function to check if user typed word correctly
def get_content():
    index_two = len(words[0])
    word_to_check = typed_word.get().strip()
    if words[0] == word_to_check:
        words.remove(words[0])
        correct_list.append(word_to_check)
    else:
        words.remove(words[0])
        wrong_list.append(word_to_check)

    word_list.delete('1.0', f'1.{index_two + 1}')
    typed_word.delete(0, END)
    add_highlight()


# function to call counter
def start_counting():
    countdown(60)
    start_info.destroy()


# lists to fill with correctly and incorrectly typed words
correct_list = []
wrong_list = []


root = Tk()
root.title("Typing Speed Test")
root.minsize(width=300, height=50)
root.config(padx=20, pady=20)

# import list of words, put it in textbox and shuffle
word_list = Text(root, font=42, wrap=WORD, width=50, height=4, padx=20, pady=20)
random.shuffle(words)
word_list.pack()
for word in words:
    word_list.insert(END, word + ' ')

# create entry box
typed_word = Entry(root, font=42)
typed_word.pack()
typed_word.focus()

# create label for timer
timer = Label(root)
timer.pack()

# create info label
start_info = Label(root, text="Press left CTRL to start", font=42)
start_info.pack()

# call function highlight
add_highlight()

# bind keys for start new word in entry and start countdown
root.bind('<space>', lambda event: get_content())
typed_word.bind("<Control_L>", lambda event: start_counting())

root.mainloop()
