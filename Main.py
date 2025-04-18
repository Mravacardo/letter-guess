import tkinter
import math
import tkinter.messagebox
import random
import string

root = tkinter.Tk()
root.minsize(350, 260)
root.title('Guess the letter game')

letters = ['a', 'b', 'c', 'd', 'e'] 
letter=random.choice(letters)

def say_hello():
    print('hello,world!')

def send_early():
    tkinter.messagebox.showinfo("messagebox", "Your guess is too early.")

def check_let():
    global letter
    guess = text_guess.get()
    guess = (guess)
    if guess == letter:
        tkinter.messagebox.showinfo("good", "Good job")
        letter=random.choice(letters)
    else:
        tkinter.messagebox.showinfo("not quite", "try again")

def btn_confirm():
    myName = text_name.get()
    tkinter.messagebox.showinfo("name", 'Well,' + myName + ',I am thinking of a letter between a and e.')

label = tkinter.Label(root, text="Welcome to our game!")
label.pack()
label_name = tkinter.Label(root, text="What's your name?")
label_name.place(x=10, y=60)
text_name = tkinter.Entry(root, width=20)
text_name.place(x=10, y=90)

btnOK = tkinter.Button(root, text="OK", command=btn_confirm)
btnOK.place(x=200, y=90, height=28)

label_guess = tkinter.Label(root, text='Take a guess:')
label_guess.place(x=10, y=150)
text_guess = tkinter.Entry(root, width=10)
text_guess.place(x=90, y=150)
btnCheck = tkinter.Button(root, text='Guess', command=check_let)
btnCheck.place(x=200, y=150, width=45, height=28)

root.mainloop()
