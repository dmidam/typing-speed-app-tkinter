from words import words
from tkinter import *
import random


def get_content():
    # Get the content of Entry Widget
    print(typed_word.get())
    

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
get_content()
window.bind('<space>', get_content)

window.mainloop()
