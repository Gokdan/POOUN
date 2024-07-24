import tkinter as tk
from math import sqrt

class Main:
    @staticmethod
    def perimetroTriangulo(lado):
        return lado * 3
    
    @staticmethod
    def alturaTriangulo(lado):
        return (sqrt(3) * lado) / 2
    
    @staticmethod
    def areaTriangulo(lado):
        return sqrt(3) * pow(lado, 2) / 4
    
    @staticmethod
    def calcular():
        lado = float(entry_lado.get())
        perimetro = Main.perimetroTriangulo(lado)
        altura = Main.alturaTriangulo(lado)
        area = Main.areaTriangulo(lado)
        resultado.config(text=f'Perímetro: {perimetro:.2f} unidades\nAltura: {altura:.2f} unidades\nÁrea: {area:.2f} unidades cuadradas')

ventana = tk.Tk()
ventana.title('Triángulo')

label_lado = tk.Label(ventana, text='Ingrese la longitud del lado del triángulo equilátero: ')
label_lado.pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

boton_calcular = tk.Button(ventana, text='Calcular', command=Main.calcular)
boton_calcular.pack()

resultado = tk.Label(ventana, text='')
resultado.pack()

ventana.mainloop()
