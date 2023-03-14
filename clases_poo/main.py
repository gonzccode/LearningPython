
class CuentaBancaria:

    def __init__(self, saldo, name ="gonzalo"):
        #se hace privado cuando se utiliza __ y @property (decorator) y externamente no se puede modificar
        #es modificable con setter, deleter
        self.__saldo = self.validar_saldo(saldo)

        #aqui ya la variable cuenta con el getter, setter y deleter por default, sin validar y no es privada
        self.name = name

    #cuando se utiliza property se crea al valor de lectura de la variable como un get
    @property
    def saldo(self):
        return self.__saldo

    #si quiero modificar utilizo setter
    @saldo.setter
    def saldo(self, credito):
        if credito > 0:
            self.__saldo = credito
        else:
            self.__saldo = 0

    #para eliminar el atributo
    @saldo.deleter
    def saldo(self):
        self.__saldo = 0
    #metodo de instancia <= es mejor esto
    def validar_saldo(self, value):
        if type(value) == float:
            return value
        else:
            return 0

    #metodo de clase <= es mejor utilizarlo en un modulo
    @classmethod
    def validar_saldo_1(cls, value):
        if type(value) == float:
            return value
        else:
            return 0


#metodo de instancia
my_account = CuentaBancaria(1000.0)
print(my_account.saldo)

#metodo de clase
print(CuentaBancaria.validar_saldo_1("perro"))

print("------------------")
#no se puede modificar al ser una variable privada
my_account.saldo = 2000.0
print(my_account.saldo)
del my_account.saldo
print(my_account.saldo)
print("------------------")
###ejemplo decorator, primero paso 1, luego hola y luego paso 2
# decorator hace un codigo intermedio, ejemplo se utiliza en inicia de sesion, autenticar, etc
def f(g):
    print("paso 1")
    g()
    print("paso 2")

@f
def hola():
    print("hola")

##
"""def f1(g1, algo): 
    print("paso f1")
    g1(algo)
    print("paso f2")

@f1("x")
def hola1(y):
    print("hola1")"""