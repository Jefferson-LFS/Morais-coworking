class Socio:
    def __init__(self, nome: str, cpf: str, numero: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__numero = numero

    def get_nome(self):
        return self.__nome

    def set_nome(self, novoNome):
        self.__nome = novoNome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novoCpf):
        self.__cpf = novoCpf

    def get_numero(self):
        return self.__numero

    def set_numero(self, novoNumero):
        self.__numero = novoNumero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero: str):
        self.__numero = novo_numero

    def __str__(self):
        return "Nome do Socío: " + self.get_nome() + ", cpf: " + self.get_cpf() + ", número: " + self.get_numero()



