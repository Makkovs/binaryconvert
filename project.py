from tkinter import *

tk = Tk()
tk.resizable(0, 0)
tk.title('Калькулятор двоичных чисел')
tk.wm_attributes("-topmost", 0)

class Main:
    def __init__(self):
        self.he1 = Label(text = 'Двоичное число: ')
        self.he2 = Label(text = 'Десятичное число: ')

        self.e1 = Entry(width = "20")
        self.e2 = Entry(width = "20")
    def binaryto(self):
        self.he1.grid(row = 2, column = 0)
        self.he2.grid(row = 3, column = 0)
        
        self.e1.grid(row = 2, column = 1)
        self.e2.grid(row = 3, column = 1)
                
btnok = Button(text = 'Преобразовать')
btnok.grid(row = 4, column = 2)

main = Main()
main.binaryto() 

tk.mainloop()
