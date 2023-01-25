from tkinter import *

root = Tk()
root.title("Round Button")
root.geometry("300x200")
root.configure(bg="lightgray")


arrows = PhotoImage(file="/home/alex/python/pets/small-tkinter/arrows1.png")
change_label = Label(root, image=arrows)

my_button = Button(root, image=arrows, compound="center", font=("Helvetica", 20), fg="lightgray", borderwidth=0, activebackground="lightgray", relief="flat", bg="lightgray")
my_button.pack(pady=20)

root.mainloop()