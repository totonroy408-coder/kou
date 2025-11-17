import tkinter 
from PIL import Image , ImageTk
import random
root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
canvas = tkinter.Canvas(root,width= width,height=height,bg='black',highlightthickness=0)
canvas.pack()
img = Image.open('fff.jpeg')
tt_img = ImageTk.PhotoImage(img)
canvas.create_image(400,400, image = tt_img)
def add_tt():
    x=random.randint(0,height)
    y=random.randint(0,width)
    canvas.create_image(x,y, image = tt_img)
    root.after(200,add_tt)
add_tt()
root.mainloop()