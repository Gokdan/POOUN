import tkinter as tk

class Main:
    @staticmethod
    def desigualdad():
        A = int(entrada_A.get())
        B = int(entrada_B.get())
        
        if (A<B):
            resultado.config(text=f'A ({A}) es menor que B ({B})')
        elif (A==B):
            resultado.config(text=f'A ({A}) es igual a B ({B})')
        else:
            resultado.config(text=f'A ({A}) es mayor que B ({B})')

ventana = tk.Tk()
ventana.title('Desigualdad')

label_A = tk.Label(ventana,text= 'Ingrese el numero A: ')
label_A.pack()
entrada_A = tk.Entry(ventana)
entrada_A.pack()

label_B = tk.Label(ventana,text= 'Ingrese el numero B: ')
label_B.pack()
entrada_B = tk.Entry(ventana)
entrada_B.pack()

boton_calcular = tk.Button(ventana, text='Calcular', command=Main.desigualdad)
boton_calcular.pack()

resultado = tk.Label(ventana, text='')
resultado.pack()

ventana.mainloop()