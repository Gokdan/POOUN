from tkinter import *
import math

class ecuacion_cuadratica:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def calculo(self):    
        discriminante = pow(self.b,2) - 4 * self.a * self.c
        if discriminante < 0:
            return None
        else:
            x_1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x_2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return x_1, x_2

    def soluciones(self):
        soluciones = self.calculo()
        if soluciones is None:
            resultado.config(text= 'No existen soluciones reales.')
        else:
            x_1, x_2 = soluciones
            resultado.config(text= f'Las soluciones a la ecuacion cuadratica son:\n X1: {x_1:.2f}\nX2: {x_2:.2f}')


class Main:
    @staticmethod
    def salida():
    
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        ecuacion_prueba = ecuacion_cuadratica(a,b,c)
        ecuacion_prueba.soluciones()



#CREACION DE LA VENTANA PRINCIPAL

root = Tk()
root.title('Ecuacion cuadratica')
root.geometry('250x250')

#ETIQUETA Y ENTRADA PARA VALOR A

label_a = Label(root, text='a: ')
label_a.grid(row= 0, column= 0)
entry_a = Entry(root)
entry_a.grid(row= 0, column=1)

#ETIQUETA Y ENTRADA PARA VALOR B

label_b = Label(root, text='b: ')
label_b.grid(row= 1, column= 0)
entry_b = Entry(root)
entry_b.grid(row= 1, column=1)

#EQUIQUETA Y ENTRADA PARA VALOR C

label_c = Label(root, text='c: ')
label_c.grid(row= 2, column= 0)
entry_c = Entry(root)
entry_c.grid(row= 2, column=1)

#BOTON CALCULAR

boton_calcular = Button(root, text='Calcular', command= Main.salida)
boton_calcular.grid(row=3 , columnspan=2, pady= 4)

#ETIQUETA RESULTADO

resultado = Label(root, text='')
resultado.grid(row=4, columnspan=2)

root.mainloop()