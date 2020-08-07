from tkinter import *
from pygame import mixer

root = Tk()

mixer.init()  #initializing

root.geometry("400x400")
root.title('Melody')
root.iconbitmap(r'favicon.ico')

text = Label(root,text ='Its good')
text.pack()


def play_music():
    mixer.music.load("Pikachu.wav")
    mixer.music.play()
    print("Button working")

def stop_music():
    mixer.music.stop()

photo = PhotoImage(file = 'project.png')
btn = Button(root, image=photo, command=play_music())
btn.pack()

Stop_photo = PhotoImage(file = 'traffic-sign.png')
btn = Button(root, image=Stop_photo, command=stop_music())
btn.pack()

root.mainloop()