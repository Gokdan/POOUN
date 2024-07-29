from tkinter import *

class Estudiante:
    def __init__(self,numero_inscripcion,nombre,apellido,patrimonio,estrato_social): #Metodo constructor
        self.numero = numero_inscripcion
        self.nombre = nombre
        self.apellido = apellido
        self.patrimonio = patrimonio
        self.estrato = estrato_social
    
    def valor_matricula(self): #Metodo para el calculo del valor a pagar en la matricula
        valor_inicial = 50000
        if (self.patrimonio >= 2000000) and (self.estrato > 3) :
            return valor_inicial + self.patrimonio * 0.03
        else: 
            return valor_inicial

class Main:
    @staticmethod
    def info(): #Metodo que captura y crea una instancia de estudiante   
        
        numero = int(entrada_numero.get())
        nombre = entrada_nombre.get()
        apellido = entrada_apellido.get()
        patrimonio = int(entrada_patrimonio.get())
        estrato_social = int(entrada_estrato.get())

        estudiante_1 = Estudiante(numero,nombre,apellido,patrimonio,estrato_social)
        resultado.config(text = f'El estudiante con número de inscripcion {estudiante_1.numero} y nombre {nombre} {apellido} debe pagar ${estudiante_1.valor_matricula()}')
#Ventana principal
ventana = Tk()
ventana.title('Pago matricula')
#Widgets
label_numero = Label(ventana, text='Numero de inscripcion: ')
label_numero.pack()
entrada_numero = Entry(ventana)
entrada_numero.pack()

label_nombre = Label(ventana, text='Nombre: ')
label_nombre.pack()
entrada_nombre = Entry(ventana)
entrada_nombre.pack()

label_apellido = Label(ventana, text='Apellido: ')
label_apellido.pack()
entrada_apellido = Entry(ventana)
entrada_apellido.pack()

label_patrimonio = Label(ventana, text='Patrimonio: ')
label_patrimonio.pack()
entrada_patrimonio = Entry(ventana)
entrada_patrimonio.pack()

label_estrato = Label(ventana, text='Estrato Social: ')
label_estrato.pack()
entrada_estrato = Entry(ventana)
entrada_estrato.pack()

boton_calcular = Button(ventana, text='Calcular', command=Main.info)
boton_calcular.pack()

resultado = Label(ventana, text = '')
resultado.pack()

ventana.mainloop()
