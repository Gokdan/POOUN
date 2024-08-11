class Cuenta:
    def __init__(self,saldo,tasaAnual):
        self._saldo = saldo
        self._numeroConsignaciones = 0
        self._numeroRetiros = 0
        self._tasaAnual = tasaAnual
        self._comisionMensual = 0

    def consignar(self,cantidad):
        self._saldo = self._saldo  + cantidad
        self._numeroConsignaciones += 1

    def retirar(self,cantidad):
        nuevoSaldo =self._saldo - cantidad
        if  nuevoSaldo >= 0:
            self._saldo -= cantidad
            self._numeroRetiros +=1
        else:
            print('La cantidad a retirar excede el saldo actual.')

    def calcularInteres(self):
        tasaMensual = self._tasaAnual / 12
        interesMensual = self._saldo * tasaMensual
        self._saldo += interesMensual

    def extractoMensual(self):
        self._saldo -= self._comisionMensual
        self.calcularInteres()
    
    def imprimir(self):
        print(f'Saldo: ${self._saldo}')
        print(f'Comision mensual: ${self._comisionMensual}')
        print(f'Número de transascciones: {self._numeroConsignaciones + self._numeroRetiros}')

class CuentaAhorros(Cuenta):
    def __init__(self,saldo,tasaAnual):
        super().__init__(saldo,tasaAnual)
        self.__activa = self._saldo >=1000

    def retirar(self, cantidad):
        if self.__activa:
            super().retirar(cantidad)
    
    def consignar(self, cantidad):
        if self.__activa:
            super().consignar(cantidad)
        
    def extractoMensual(self):
        if self._numeroRetiros > 4:
            self._comisionMensual += (self._numeroRetiros - 4) * 1000
        super().extractoMensual()
        if self._saldo < 10000:
            self.__activa = False
    
    def imprimir(self):
        super().imprimir()

class CuentaCorriente(Cuenta):
        def __init__(self,saldo,tasaAnual):
            super().__init__(saldo,tasaAnual)
            self.sobreGiro = 0
        
        def retirar(self, cantidad):
            resultado = self._saldo - cantidad
            if resultado < 0:
                self.sobreGiro = self.sobreGiro - resultado
                self._saldo = 0
            else:
                super().retirar(cantidad)

        def consignar(self, cantidad):
            if self.sobreGiro > 0:
                residuo = self.sobreGiro - cantidad
                if residuo > 0:
                    self.sobreGiro = residuo
                else:
                    self._saldo += abs(residuo) 
                    self.sobreGiro = 0
            else:
                super().consignar(cantidad)

        def extractoMensual(self):
            super().extractoMensual()

        def imprimir(self):
            super().imprimir()
            print(f'Valor de sobregiro: {self.sobreGiro}')
        

class Main:
    @staticmethod
    def Main():
        Ahorros_1 = CuentaAhorros(100000,0.10)
        Ahorros_1.consignar(50000)
        Ahorros_1.retirar(70000)
        Ahorros_1.extractoMensual()
        Ahorros_1.imprimir()

Main.Main()