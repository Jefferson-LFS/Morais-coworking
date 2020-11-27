from modelo.socio import Socio
from funcionarios.funcionario import Funcionario
from funcionarios.secretaria import Secretaria
def main():
    socio_1 = Socio("Jefferson", '2222222222-42', "8393000-0000")
    socio_2 = Socio("Valesca", '3333333333-42', "8392000-0000")
    func_1 = Funcionario("Carlos", "auxiliar adimistrativo", 7834)
    func_2 = Funcionario("Maria", "Superitendete", 7012)
    secrt = Secretaria("Adrina", 'Secretaria', 7015)
    secrt.registrarSocios(socio_1)
    secrt.registrarSocios(socio_2)
    secrt.registrarFuncionario(func_1)
    secrt.registrarFuncionario(func_2)
    secrt.registros()
    secrt.removerFuncionario("Maria")
    secrt.removerSocio("Jefferson")
    secrt.registros()

    sala_1 = []
    sala_2 = []
    sala_3 = []
    sala_4 = []


if __name__ == '__main__':
    main()