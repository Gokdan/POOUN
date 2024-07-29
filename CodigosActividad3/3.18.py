import tkinter as tk
# Clase empleado
class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion
    
    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora
    
    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion_fosf = salario_bruto * (self.retencion / 100)
        return salario_bruto - retencion_fosf

# Metodo que es llamado en el Button para capturar los valores y crear la instancia
def calcular_salarios():
    codigo = entry_codigo.get()
    nombres = entry_nombres.get()
    horas_trabajadas = float(entry_horas.get())
    valor_hora = float(entry_valor.get())
    retencion = float(entry_retencion.get())
    
    empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion)
    
    salario_bruto = empleado.calcular_salario_bruto()
    salario_neto = empleado.calcular_salario_neto()
    
    resultado.config(text=f"Código: {codigo}\nNombre: {nombres}\nSalario Bruto: {salario_bruto}\n Salario Neto: {salario_neto}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Salarios")

# Crear los widgets
label_codigo = tk.Label(root, text="Código del empleado:")
label_codigo.grid(row=0, column=0)
entry_codigo = tk.Entry(root)
entry_codigo.grid(row=0, column=1)

label_nombres = tk.Label(root, text="Nombres del empleado:")
label_nombres.grid(row=1, column=0)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)

label_horas = tk.Label(root, text="Horas trabajadas:")
label_horas.grid(row=2, column=0)
entry_horas = tk.Entry(root)
entry_horas.grid(row=2, column=1)

label_valor = tk.Label(root, text="Valor hora trabajada:")
label_valor.grid(row=3, column=0)
entry_valor = tk.Entry(root)
entry_valor.grid(row=3, column=1)

label_retencion = tk.Label(root, text="Porcentaje de retención:")
label_retencion.grid(row=4, column=0)
entry_retencion = tk.Entry(root)
entry_retencion.grid(row=4, column=1)

boton_calcular = tk.Button(root, text="Calcular Salario", command=calcular_salarios)
boton_calcular.grid(row=5, columnspan=2)

resultado = tk.Label(root, text="")
resultado.grid(row=6, columnspan=2)

# Ejecutar la aplicación
root.mainloop()