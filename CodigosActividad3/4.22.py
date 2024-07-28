from tkinter import *

class Main:
    @staticmethod
    def salario():
        nombre = entrada_nombre.get()
        valor_hora = float(entrada_valorHora.get())
        horas_mes = int(entrada_horasMes.get())
        salario_total = valor_hora * horas_mes
        if salario_total > 450000:
            label_resultado.config(text= f'Nombre: {nombre}\n Salario total: $ {salario_total:.2f}')
        else: 
            label_resultado.config(text= f'Nombre: {nombre}')


root = Tk()
root.title('Informacion trabajador')
root.geometry('200x250')

label_nombre = Label(root, text='Nombre: ')
label_nombre.pack()
entrada_nombre = Entry(root)
entrada_nombre.pack()

label_valorHora = Label(root, text='Valor hora: ')
label_valorHora.pack()
entrada_valorHora = Entry(root)
entrada_valorHora.pack()

label_horasMes = Label(root, text= 'Horas al mes: ')
label_horasMes.pack()
entrada_horasMes = Entry(root)
entrada_horasMes.pack()

boton_calcular = Button(root, text='Calcular', command=Main.salario)
boton_calcular.pack()

label_resultado = Label(root, text='')
label_resultado.pack()

root.mainloop()
