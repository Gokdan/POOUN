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
            print('La cantidad a retirar excede el _saldo actual.')

    def calcularInteres(self):
        tasaMensual = self._tasaAnual / 12
        interesMensual = self._saldo * tasaMensual
        self._saldo += interesMensual

    def extractoMensual(self):
        self._saldo -= self._comisionMensual
        self.calcularInteres()
    
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
        