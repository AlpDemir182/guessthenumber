from tkinter import *
# from tkinter.ttk import *
import tkinter.font as f
import tkinter.messagebox
import random

root = Tk()
root.geometry("300x300")
root.title("Guess the Number Game")
root.config(background="white")

number = random.randint(1,20)

def hello():
    print("Hello")

def check_number():
    guess = entrytext.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("High, Your guess is too high")
    if guess < number:
        tkinter.messagebox.showinfo("Low, Your guess is too low")
    if guess == number:
        tkinter.messagebox.showinfo("Well done, You guessed the numer!")

def welcome():
    myname = entryname.get()
    tkinter.messagebox.showinfo("Name: ", "Hi, " +myname +" I'm thinking of a number between 1 and 20")

label1 = Label(root, text= "Guess the Number", background = "white", font = ("Arial", 20), foreground = "black")
label1.pack(side= "top")

entryname = Entry(root, width= 10 )
entryname.place(x=100, y= 60)
label2 = Label(root, text= "What is your name?", background = "white", font = ("Arial", 15), foreground = "black")
label2.place(x=70 , y=30)
entrytext = Entry(root, width = 10)
entrytext.place(x= 100, y = 150)
label3 = Label(root, text = "Guess a number between 1 and 20:", background = "white", font = ("Arial", 15), foreground= "black")
label3.place(x = 20, y = 120)


root.mainloop()