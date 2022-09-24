import random


class Conta:

    # Constructor
    def __init__(self):
        self._numConta = None
        self._dono = None
        self._tipo = None
        self._saldo = 0
        self._status = False

    # GETTERS
    @property
    def numConta(self):
        return self._numConta

    @property
    def tipo(self):
        return self._tipo

    @property
    def dono(self):
        return self._dono

    @property
    def saldo(self):
        return self._saldo

    @property
    def status(self):
        return self._status

    # SETTERS

    @numConta.setter
    def numConta(self, numero):
        self._numConta = numero

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo

    @dono.setter
    def dono(self, novo_dono):
        self._dono = novo_dono

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    def abriConta(self, dono, tipo):

        self.dono = dono
        self.tipo = tipo
        self.numConta = random.randint(0, 1000)
        self.status = True
        self.saldo = 50 if self.tipo == 'CC' else (150 if self.tipo == 'CP' else 0)

    def fecharConta(self):
        if self.saldo > 0:
            print('Retire todo dinheiro antes de fechar a conta')
        elif self.saldo < 0:
            print('Conta em debito')
        else:
            print('Conta fechada')
            self.status = False

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            print('Saldo depositado')
        else:
            print('Abra a conta primeiro')

    def sacar(self, valor):
        if self.status:
            if self.saldo < valor:
                print('Saldo indisponivel')
            else:
                print('Saldo sacado')
                self.saldo -= valor
        else:
            print('Abra a conta primeiro')

    def pagamentoMensal(self):
        valor = 0
        if self.tipo == 'CC':
            valor = 12
        elif self.tipo == 'CP':
            valor = 20
        if self.saldo < 12:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor

    def informacao(self):
        print(f'numero:{self.numConta}\n'
              f'dono: {self.dono}\n'
              f'tipo: {self.tipo}\n'
              f'saldo: {self.saldo}\n'
              f'status: {self.status}')

