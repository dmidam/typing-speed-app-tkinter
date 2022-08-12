from words import words
from tkinter import *
import random




def get_content():
    # Get the content of Entry Widget
    if words[0] == typed_word.get().strip():
        words.remove(words[0])
        print("ok")
    typed_word.delete(0, END)


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

button = Button(window, command=get_content)
window.bind('<space>', lambda event: get_content())
while True:
    if words[0] == typed_word.get():
        print("ok")

    window.mainloop()


