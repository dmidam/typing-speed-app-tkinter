from words import words
from tkinter import *
import random


def add_highlight():
    index_two = len(words[0])
    word_list.tag_add("start", "1.0", f"1.{index_two}")
    word_list.tag_config("start", background="green", foreground="white")


def countdown(count):
    # change text in label
    label['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count - 1)


def get_content():
    index_two = len(words[0])
    word_to_check = typed_word.get().strip()
    print(words[0])
    if words[0] == word_to_check:
        words.remove(words[0])
        correct_list.append(word_to_check)
        print("ok")
    else:
        words.remove(words[0])
    word_list.delete('1.0', f'1.{index_two + 1}')
    typed_word.delete(0, END)
    add_highlight()


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
add_highlight()
window.bind('<space>', lambda event: get_content())

window.mainloop()

print(correct_list)
