import tkinter as tk
from math import sqrt
class Main:
    @staticmethod
    def perimetroTriangulo(lado): #Metodo que retorna el perimetro dado el argumento lado
        return lado*3
    
    @staticmethod
    def alturaTriangulo(lado): #Metodo que retorna la altura dado el argumento lado
        return (sqrt(3)*lado)/2
    

    @staticmethod
    def areaTriangulo(lado): #Metodo que retorna el area dado el argumento lado
        return sqrt(3)*pow(lado,2)/4   
    
    @staticmethod
    def info(): #Método que captura el valor de "lado" y lo emplea para el calculo 
        lado = float(entry_lado.get())
        perimetro = Main.perimetroTriangulo(lado)
        altura = Main.alturaTriangulo(lado)
        area = Main.areaTriangulo(lado)
        resultado.configure(text= f'Perimetro: {perimetro:.2f}unidades \n Area: {area:.2f} unidades cuadradas\n Altura {altura:.2f} unidades')
#Creacion de la ventana
ventana = tk.Tk()
ventana.title('Triangulo')
#Widgets
label_lado = tk.Label(ventana,text='Ingrese la longitud del lado del triangulo equilatero: ')
label_lado.pack()
entry_lado = tk.Entry(ventana)
entry_lado.pack()

boton_calcular = tk.Button(ventana, text='Calcular', command=Main.info)
boton_calcular.pack()
resultado = tk.Label(ventana, text='')
resultado.pack()


ventana.mainloop()