from tkinter import *

'''
Label(text='Spam').pack()
mainloop()
'''

from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')
'''
if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
'''

mainwin = Tk()
Label(mainwin, text=__name__).pack()

popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()