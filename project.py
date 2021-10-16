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
        self.binToDec = True
        self.binaryno = ['2', '3', '4', '5', '6', '7', '8', '9'] 
 
        self.he1 = Label(text = 'Двоичное число: ')
        self.he2 = Label(text = 'Десятичное число: ')

        self.e1 = Entry(width = "25")
        self.e2 = Entry(width = "25")

        btnok = Button(text = 'Преобразовать', command = self.convert)
        btnok.grid(row = 4, column = 2)
        btnRemake = Button(text = 'Поменять', command = self.remake)
        btnRemake.grid(row=4, column = 1)

        self.he1.grid(row = 2, column = 0)
        self.he2.grid(row = 3, column = 0)
        
        self.e1.grid(row = 2, column = 1)
        self.e2.grid(row = 3, column = 1)

        self.e2.config(state = DISABLED)
    #Кнопка поменять
    def remake(self):
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        if self.binToDec == True:
            self.e2.config(state = NORMAL)
            self.e1.config(state = DISABLED)
        if self.binToDec == False:
            self.e2.config(state = DISABLED)
            self.e1.config(state = NORMAL)
        self.binToDec = not self.binToDec
    #Преобразование
    def convertBinary(self, bin): 
        splitedBin = splitText(bin)
        mathDegree = lambda a, b : a*(2**b)
        decimal = 0

        for d in enumerate(splitedBin):
            degree = len(splitedBin) - d[0] - 1
            if degree < 0:
                break
            decimal += mathDegree(int(d[1]), degree)

        self.e2.config(state = NORMAL)
        self.e2.delete(0, 'end')
        self.e2.insert(0, str(decimal))
        self.e2.config(state = DISABLED)
    #Кнопка преобразовать
    def convert(self):
        if self.binToDec:
            binary = self.e1.get()
            if len(binary) >= 61: 
                self.e1.delete(0, 'end')
                self.e1.insert(0, 'Слишком большое число')
                return
            for b in enumerate(self.binaryno):
                if b[1] in binary:
                    self.e1.delete(0, 'end')
                    self.e2.delete(0, 'end')
                    self.e1.insert(0, 'Ошибка')
                    return
            self.convertBinary(binary)
        else:
            pass
  
main = Main()

tk.mainloop()
