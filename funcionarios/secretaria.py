from funcionarios.funcionario import Funcionario

class Secretaria(Funcionario):
    def __init__(self, nomeF: str, cargo: str, ramal: int):
        super().__init__(nomeF, cargo, ramal)
        self.__funcs = []
        self.__socios = []

    def registrarFuncionario(self, novoFuncionario: object):
        self.__funcs.append(novoFuncionario)


    def removerFuncionario(self, nomeFuncionario: str):
        for f in self.__funcs:
            if f.nomeF == nomeFuncionario:
                self.__funcs.remove(f)

    def registrarSocios(self, novoSocio: object):
        self.__socios.append(novoSocio)


    def removerSocio(self, nomeSocio: str):
        for s in self.__socios:
            if s.nome == nomeSocio:
                self.__socios.remove(s)

    def registros(self):
        if self.__funcs and self.__socios:
            print("Registro de funcinarios: ")
            for f in self.__funcs:
                print(f.nomeF)
            print("Registro de socios:")
            for s in self.__socios:
                print(s.nome)
        else:
            print("Nenhum funcinário ou sócio registrado")



