from typing import Type
class Interruptor:

    def __init__(self,comodo: str) -> None:
        self.__comodo = comodo

    def acender(self):
        print(f'acendendo {self.__comodo}')

    def apagar(self):
        print(f'apagando {self.__comodo}')



class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self,interruptor : Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('dormindo')


interruptor_quarto= Interruptor('quarto')
vitor = Pessoa()


interruptor_quarto.acender()
vitor.acender_luz(interruptor_quarto)