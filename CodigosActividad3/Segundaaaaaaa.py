import tkinter as tk

class Empleado:
    def __init__(self,codigo,nombre,horasTrabajadas,valorHora,porcentajeRetencion):
        self.codigo = codigo
        self.nombre = nombre
        self.horasTrabajadas = horasTrabajadas
        self.valorHora = valorHora
        self.porcentajeRetencion = porcentajeRetencion

    def salarioBruto(self):
        return (self.horasTrabajadas) * (self.valorHora)
    
    def salarioNeto(self):
        return (self.salarioBruto()) - (self.salarioBruto()*self.porcentajeRetencion)

class Main:
    @staticmethod
    def info():
        codigo = int(entrada_codigo.get())
        nombre = entrada_nombre.get()
        horas_trabajadas = int(entrada_horasTrabajadas.get())
        valor_hora = float(entrada_valorHora.get())
        porcentaje_retencion = float(entrada_porcentajeRetencion.get())


        empleado = Empleado(codigo,nombre,horas_trabajadas,valor_hora,porcentaje_retencion)
        resultado.config(text= f'Codigo: {codigo}\n Nombre: {nombre}\n Salario bruto: ${empleado.salarioBruto()}\n Salario neto: ${empleado.salarioNeto()}')
        


ventana = tk.Tk()
ventana.title('Pago empleados')

label_codigo = tk.Label(ventana, text='Codigo: ')
label_codigo.pack()
entrada_codigo = tk.Entry(ventana)
entrada_codigo.pack()

label_nombre = tk.Label(ventana, text='Nombre: ')
label_nombre.pack()
entrada_nombre = tk.Entry(ventana,)
entrada_nombre.pack()

label_horasTrabajadas = tk.Label(ventana, text='Horas Trabajadas: ')
label_horasTrabajadas.pack()
entrada_horasTrabajadas = tk.Entry(ventana)
entrada_horasTrabajadas.pack()

label_valorHora = tk.Label(ventana, text= 'Valor Hora: ')
label_valorHora.pack()
entrada_valorHora = tk.Entry(ventana)
entrada_valorHora.pack()

label_porcentajeRetencion = tk.Label(ventana, text= 'Porcentaje de Retencion: ')
label_porcentajeRetencion.pack()
entrada_porcentajeRetencion = tk.Entry(ventana)
entrada_porcentajeRetencion.pack()

resultado = tk.Label(ventana, text = '')
resultado.pack()

boton_calcular = tk.Button(ventana, text='Calcular', command=Main.info)
boton_calcular.pack()

ventana.mainloop()