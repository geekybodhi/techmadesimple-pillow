import tkinter as tk
import tkinter.filedialog
import PIL
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
import numpy as np


class ImageEditor(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent) 
        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("Simple Photo Editor")
        self.pack(fill = tk.BOTH, expand = 1)
        
        self.label1 = tk.Label(self, border = 25)
        self.label1.grid(row = 1, column = 1)
        menubar = tk.Menu(self.parent)
        filemenu = tk.Menu(menubar, tearoff=0)
        
        filemenu.add_command(label="Open", command= self.onOpen)
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Close")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Rotate", command=self.onRot)
        editmenu.add_command(label="Negative", command=self.onNeg)
        menubar.add_cascade(label="Simple Mods", menu=editmenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index")
        helpmenu.add_command(label="About...")
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.parent.config(menu = menubar)


    def onNeg(self):
        I2 = 255-self.I;
        im = Image.fromarray(np.uint8(I2))
        photo2=ImageTk.PhotoImage(im)
        self.label1.configure(image=photo2)
        self.label1.image = photo2  ## keep a reference!
        self.label1.grid(row=1, column=2)


    def onRot (self):
        im = self.img.rotate(45)  ##rotate an image 45 degrees
        #im = self.img.filter(ImageFilter.CONTOUR)  ## trace the contours of an image
        photo3 = ImageTk.PhotoImage(im)
        self.label1.configure(image=photo3)
        self.label1.image = photo3
        self.label1.grid(row=1, column=3)
        self.img = photo3
            

    def setImage(self):
        self.img = Image.open(self.fn)
        ##resize the window as per the size of the image
        self.I = np.asarray(self.img)
        l, h = self.img.size
        geo= str(l)+"x"+str(h)+"+0+0"
        self.parent.geometry(geo)
        photo = ImageTk.PhotoImage(self.img)  ## convert PIL image object to Tkinter's PhotoImage object
        self.label1.configure(image = photo) ## put the image into the canvas
        self.label1.image = photo # keep a reference!

    def onOpen(self):
        ftypes = [('Image Files', '*.jpg *.png')]
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        self.fn = filename
        self.setImage()

    def onError(self):
        box.showerror("Error", "Could not open file")    


def main():

    root = tk.Tk()
    ImageEditor(root)
    root.geometry("300x200")
    root.mainloop()  


if __name__ == '__main__':
    main()
