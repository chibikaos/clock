from tkinter import *
from datetime import *
import pyglet

pyglet.font.add_file("digital-7.ttf")

window = Tk()
window.title("")
window.geometry("360x140")
window.resizable(width=FALSE, height=FALSE)
window.configure(bg="#000000")

def clock():
    local = datetime.now()
    time = local.strftime("%H:%M:%S")
    date = local.strftime("%d %b %Y")

    l1.config(text=time)
    l1.after(200, clock) # depois de 200 milesimos de segundos ele irá executar a função novamente
    l2.config(text=date)

l1 = Label(window, text="", font=("digital-7", 80), bg="#000000", fg="#FFFFFF", width=7)
l1.grid(row=0, column=0)

l2 = Label(window, text="", font=("digital-7" ,17), bg="#000000", fg="#FFFFFF")
l2.grid(row=1, column=0)

clock()
window.mainloop()