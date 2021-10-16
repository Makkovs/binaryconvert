#Импорты
import math
from tkinter import *
#Некоторые настройки
tk = Tk()
tk.resizable(0, 0)
tk.title('Калькулятор двоичных чисел')
tk.wm_attributes("-topmost", 0)

#Функции
def splitText(text):
    splited = []
    for b in enumerate(text):
        splited.append(b[1])
    return splited

#Основной код
class Main:
    #Интерфейс
    def __init__(self):
        self.binaryno = ['2', '3', '4', '5', '6', '7', '8', '9'] 

        self.he1 = Label(text = 'Двоичное число: ')
        self.he2 = Label(text = 'Десятичное число: ')

        self.e1 = Entry(width = "20")
        self.e2 = Entry(width = "20")

        btnok = Button(text = 'Преобразовать', command = self.convertb)
        btnok.grid(row = 4, column = 2)

        self.he1.grid(row = 2, column = 0)
        self.he2.grid(row = 3, column = 0)
        
        self.e1.grid(row = 2, column = 1)
        self.e2.grid(row = 3, column = 1)
    #Преобразование из бинарного
    def convertb(self):
        binary = self.e1.get()
        decimal = self.e2.get()
        for b in enumerate(self.binaryno):
            if b[1] in binary:
                self.e1.delete(0, 'end')
                self.e1.insert(0, 'Ошибка')
                self.e2.delete(0, 'end')
                return
        splitedBin = splitText(binary)
        
main = Main()

tk.mainloop()
