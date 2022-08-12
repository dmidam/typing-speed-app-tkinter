from words import words
from tkinter import *
import random

def countdown(count):
    # change text in label
    label['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count-1)

def get_content():
    word_to_check = typed_word.get().strip()
    if words[0] == word_to_check:
        words.remove(words[0])
        correct_list.append(word_to_check)
        print("ok")
    typed_word.delete(0, END)

correct_list = []

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

word_list = Text(window, font=42, wrap=WORD, width=50, height=4, padx=20, pady=20)
random.shuffle(words)
word_list.pack()

typed_word = Entry(window, font=42)
typed_word.pack()

for word in words:
    word_list.insert(END, word + ' ')

label = Label(window)
label.pack()

# call countdown first time
countdown(60)

window.bind('<space>', lambda event: get_content())

window.mainloop()

print(correct_list)
