from tkinter import *
import math
pi = math.pi

class circulo:
    def __init__(self,radio):
        self.radio = radio
    def area_circulo(self):                 #Metodo para el area del circulo
        return  (pi * pow(self.radio,2))
    
    def circunferencia(self):               #Metodo para la circunferencia
        return 2 * pi * self.radio
    
class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):              #Metodo para el area del rectangulo
        return self.base * self.altura
    
    def perimetro_rectangulo(self):         #Metodo para el perimetro del rectangulo
        return (2 * self.base) + (2 * self.altura)
    
class cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def area_cuadrado(self):                #Metodo para el area del cuadrado
        return  self.lado * self.lado
    
    def perimetro_cuadrado(self):           #Metodo para el perimetro del cuadrado
        return self.lado * 4

class triangulo_rectangulo:                 
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area_triangulo(self):               #Metodo para el area del triangulo
        return (self.base * self.altura) / 2
    
    def hipotenusa(self):                   #Metodo para calcular la hipotenusa
        argumento = pow(self.base,2) + pow(self.altura,2)
        return math.sqrt(argumento)

    def perimetro_triangulo(self):          #Metodo para hallar el perimetro del triangulo
        return self.base + self.altura + self.hipotenusa()
    
    def tipo_triangulo(self):               #Metodo para determinar el tipo de triangulo
        if self.base == self.altura and self.base == self.hipotenusa():
            return  'equilátero!'
        
        elif self.base != self.altura and self.base != self.hipotenusa():
            return 'Escaleno!'
        
        else:
            return 'isósceles!'

class Main:         #Clase Main y metodo main para crear instancias de las figuras geometricas y probar los metodos definidos sobre ellas
    @staticmethod
    def main():
        # Instancias de las figuras geométricas
        circulo_1 = circulo(int(entrada_radioCirculo.get()))  
        rectangulo_1 = rectangulo(float(entrada_baseRectangulo.get()),float(entrada_alturaRectangulo.get()))   
        cuadrado_1 = cuadrado(float(entrada_ladoCuadrado.get()))  
        triangulo_rectangulo_1 = triangulo_rectangulo(float((entrada_baseTriangulo.get())),float((entrada_alturaRectangulo.get())))  
        
        salida = (
        f'Área del círculo: {circulo_1.area_circulo():.2f} cm cuadradros\n'
        f'Perímetro del círculo: {circulo_1.circunferencia():.2f}cm\n\n'
        f'Área del rectángulo: {rectangulo_1.area_rectangulo():.2f}cm cuadrados\n'
        f'Perímetro del rectángulo: {rectangulo_1.perimetro_rectangulo():.2f}cm\n\n'
        f'Área del cuadrado: {cuadrado_1.area_cuadrado():.2f}cm cuadrados\n'
        f'Perímetro del cuadrado: {cuadrado_1.perimetro_cuadrado():.2f} cm\n\n'
        f'Área del triángulo rectángulo: {triangulo_rectangulo_1.area_triangulo():.2f} cm cuadrados\n'
        f'Perímetro del triángulo rectángulo: {triangulo_rectangulo_1.perimetro_triangulo():.2f} cm\n\n'
        f'Hipotenusa del triángulo rectángulo: {triangulo_rectangulo_1.hipotenusa():.2f} cm\n'
        f'Tipo de triángulo: {triangulo_rectangulo_1.tipo_triangulo()}'
                        )
        resultado.config(text=salida)


#CREACION DE LA VENTANA PRINCIPAL

root = Tk()
root.title('Figuras geométricas')
root.geometry('350x450')

label_radioCirculo = Label(root, text= 'Ingrese el radio del circulo: ')
label_radioCirculo.grid(row= 0, column= 0)
entrada_radioCirculo = Entry(root)
entrada_radioCirculo.grid(row= 0, column=1)

label_baseRectangulo = Label(root, text= 'Ingrese la base del rectángulo: ')
label_baseRectangulo.grid(row= 1, column= 0)
entrada_baseRectangulo = Entry(root)
entrada_baseRectangulo.grid(row= 1, column= 1)

label_alturaRectangulo = Label(root, text= 'Ingrese la altura del rectángulo: ')
label_alturaRectangulo.grid(row= 2, column= 0)
entrada_alturaRectangulo = Entry(root)
entrada_alturaRectangulo.grid(row= 2, column= 1)

label_ladoCuadrado = Label(root, text= 'Ingrese el lado del cuadrado: ')
label_ladoCuadrado.grid(row= 3, column= 0)
entrada_ladoCuadrado = Entry(root)
entrada_ladoCuadrado.grid(row= 3, column= 1)

label_baseTriangulo = Label(root, text= 'Ingrese la base del triangulo: ')
label_baseTriangulo.grid(row=4 , column=0)
entrada_baseTriangulo = Entry(root)
entrada_baseTriangulo.grid(row=4, column=1)

label_alturaTriangulo = Label(root, text= 'Ingrese altura el triangulo: ')
label_alturaTriangulo.grid(row= 5, column=0)
entrada_alturaTriangulo = Entry(root)
entrada_alturaTriangulo.grid(row= 5, column=1)

boton_calcular = Button(root, text= 'Calcular', command= Main.main)
boton_calcular.grid(row=6 , columnspan= 2)

resultado = Label(root, text='')
resultado.grid(row= 7, columnspan= 2)



root.mainloop()