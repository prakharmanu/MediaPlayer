from tkinter import *

root = Tk()


root.geometry("400x400")
root.title('Melody')
root.iconbitmap(r'favicon.ico')
text = Label(root,text ='Its good')
text.pack()

photo = PhotoImage(file = 'project.png')

def play_btn():
    print("Button was pressed")

btn = Button(root,image = photo, command = play_btn())
btn.pack()

root.mainloop()