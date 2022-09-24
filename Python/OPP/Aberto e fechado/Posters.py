class Postegre:

    def __init__(self) -> None:
        self.__conexao = 'Postgres'


    def conectar(self) -> str:
        print('conectando ao banco')
        return self.__conexao

    def desconectar(self) -> str:
        print('desconectando')