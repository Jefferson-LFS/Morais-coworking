from modelo.socio import Socio
from modelo.salas.sala_1 import Sala_1
from modelo.salas.sala_2 import Sala_2
from modelo.salas.sala_3 import Sala_3
from modelo.salas.sala_4 import Sala_4
from funcionarios.funcionario import Funcionario
from funcionarios.secretaria import Secretaria

def main():
    # ------------------------------Reserva de salas------------------------------------------------------------------------#

    lista_horarios = ["07:00-07:45", "08:00-08:45", "09:00-09:45", "10:00-10:45", "11:00-11:45", "13:00-13:45",
                      "14:00-14:45",
                      "15:00-15:45", "16:00-16:45", "17:00-17:45", "18:00-18:45", "19:00-10:45", "19:00-19:45",
                      "20:00-20:45"]
    registro_geral = []
    sala_1 = Sala_1()
    sala_2 = Sala_2()
    sala_3 = Sala_3()
    sala_4 = Sala_4()

    def discover_sala(num_sala):
        if num_sala == 1:
            return sala_1
        elif num_sala == 2:
            return sala_2
        elif num_sala == 3:
            return sala_3
        elif num_sala == 4:
            return sala_4
        else:
            return False

    def pesquisar_reservas_dia(nome_s, data_r, lista_geral):
        for rg in lista_geral:
            if (nome_s and data_r) in rg:
                print(rg)

    def pesquisar_salas_livres(data, horario):
        print(sala_1.disp_reserva(data, horario))
        print(sala_2.disp_reserva(data, horario))
        print(sala_3.disp_reserva(data, horario))
        print(sala_4.disp_reserva(data, horario))

    def valida_nome(nome):
        try:
            if secrt.buscarSocio(nome) != False:
                return True
        except Exception as erro:
            return False

    def valida_horario(horario, lista_horarios):
        try:
            if horario not in lista_horarios:
                return False
        except Exception as erro:
            return False
        finally:
            return horario

    def valida_reservas_geral(sala_desejada, data_r, horario, nome_s, lista_geral):
        if registro_geral:
            for rg in registro_geral:
                if data_r == rg[0] and horario == rg[1] and nome_s == rg[2] and num_sala != rg[3]:
                    return False
                elif data_r == rg[0] and horario == rg[1] and nome_s == rg[2] and num_sala == rg[3]:
                    return False
                else:
                    valida_reserva(sala_desejada, data_r, horario, nome_s, registro_geral)
        else:
            valida_reserva(sala_desejada, data_r, horario, nome_s, registro_geral)

    def valida_reserva(sala_desejada, data_r, horario, nome_s, lista_geral):
        if sala_desejada.registros() == False:
            sala_desejada.reservar(data_r, horario, nome_s, lista_geral)
            return sala_desejada.registros()
        else:
            for r in sala_desejada.registros():
                for i in range(len(sala_desejada.registros())):
                    if horario == sala_desejada.registros()[i][1] and data_r == sala_desejada.registros()[i][0]:
                        return False
                sala_desejada.reservar(data_r, horario, nome_s, lista_geral)
                return sala_desejada.registros()

    # SECRETÁRIA
    secrt = Secretaria("Adrina", 'Secretaria', 7015)

    opc = " "
    while opc != 'q':
        opc = input('Digite: '
                    '\n[cas_s] Cadastrar sócio'
                    '\n[cas_f] Cadastrar Funcionário'
                    '\n[rem] Remover reserva'
                    '\n[res] Reservar sala'
                    '\n[alt_s] Alterar no do sócio na reserva'
                    '\n[alt_h] Alterar horário na reserva'
                    '\n[const_d] Consultar reservas do dia'
                    '\n[disp] Consultar Disponibilidade'
                    '\n[q] Sair'
                    '\n')

        # --------------------Cadastro dos Socios------------------#
        if opc == "cas_s":
            socio_1 = Socio("Jefferson", '11111111-42', "8393000-0000")
            socio_2 = Socio("Valesca", '33333333-42', "8392000-0000")
            socio_3 = Socio("Fulano", '44444444-42', "8394000-0000")
            secrt.registrarSocios(socio_1)
            secrt.registrarSocios(socio_2)
            secrt.registrarSocios(socio_3)
            secrt.removerFuncionario("Maria")
            secrt.removerSocio("Fulano")
            print("Cadastros realizados com sucesso")
        # --------------------Cadastro dos Funcionários ----------------#
        if opc == "cas_f":
            func_1 = Funcionario("Carlos", "auxiliar adimistrativo", 7834)
            func_2 = Funcionario("Maria", "Superitendete", 7012)
            secrt.registrarFuncionario(func_1)
            secrt.registrarFuncionario(func_2)
            print("Cadastros realizados com sucesso")

        # -------------------------------------Reserva Sala---------------------------------------#
        if opc == 'res':
            nome_s = input("Nome do sócio: ")
            while not valida_nome(nome_s):
                print("Sócio não registrado ou nome estar incorreto")
                nome_s = input("Informe o nome sócio novamente: ")
            nome_s = secrt.buscarSocio(nome_s)

            data_r = input("Informe a data: ")

            horario_incial, horario_final = input("Informe o horário no seguinte formato -> hh:mm-hh:mm ").split("-")
            horario = horario_incial + "-" + horario_final
            while valida_horario(horario, lista_horarios) == False:
                print("Horario não cadastrado.")
                horario_incial, horario_final = input(
                    "Informe novamente o horário no seguinte formato -> hh:mm-hh:mm : ")
                horario = horario_incial + "-" + horario_final

            num_sala = int(input("Informe a sala: "))
            sala_desejada = discover_sala(num_sala)

            if valida_reservas_geral(sala_desejada, data_r, horario, nome_s, registro_geral) != False:
                print("Reserva feita com sucesso")
            else:
                print("Não foi possível realizar a operação")

            opc = input("Deseja fazer outra operação? Digite 'sim' para continuar ou 'q' para sair: ")

            # -------------------------------------Remover reserva---------------------------------------#
        if opc == 'rem':
            num_sala = int(input("Informe a sala que deseja remover a reserva: "))
            sala_desejada = discover_sala(num_sala)

            nome_s = input("Nome do sócio na reserva: ")
            while not valida_nome(nome_s):
                print("Sócio não registrado ou nome estar incorreto")
                nome_s = input("Informe o nome sócio novamente: ")
            nome_s = secrt.buscarSocio(nome_s)

            data_r = input("Informe a data: ")

            horario_incial, horario_final = input("Informe o horário no seguinte formato -> hh:mm-hh:mm ").split("-")
            horario = horario_incial + "-" + horario_final
            while valida_horario(horario, lista_horarios) == False:
                print("Horario não cadastrado.")
                horario_incial, horario_final = input(
                    "Informe novamente o horário no seguinte formato -> hh:mm-hh:mm : ")
                horario = horario_incial + "-" + horario_final

            if sala_desejada.remover_reserva(data_r, horario, nome_s, registro_geral) != False:
                print("Remoção feita com sucesso")

            else:
                print("Não foi possível realizar a operação")

            opc = input("Deseja fazer outra reserva? Digite 'sim' para continuar ou 'q' para sair: ")

        # -----------------------------Alterar Socio-----------------------------------------#
        if opc == 'alt_s':
            num_sala = int(input("Informe a sala que deseja alterar o nome do socio na reserva: "))
            sala_desejada = discover_sala(num_sala)

            nome_s = input("Nome do novo sócio para reserva: ")
            while not valida_nome(nome_s):
                print("Sócio não registrado ou nome estar incorreto")
                nome_s = input("Informe o nome sócio novamente: ")
            nome_s = secrt.buscarSocio(nome_s)

            data_r = input("Informe a data: ")

            horario_incial, horario_final = input("Informe o horário no seguinte formato -> hh:mm-hh:mm ").split("-")
            horario = horario_incial + "-" + horario_final
            while valida_horario(horario, lista_horarios) == False:
                print("Horario não cadastrado.")
                horario_incial, horario_final = input(
                    "Informe novamente o horário no seguinte formato -> hh:mm-hh:mm : ")
                horario = horario_incial + "-" + horario_final

            if sala_desejada.alterar_socio(data_r, horario, nome_s, registro_geral) != False:
                print("Alteração feita com sucesso")
            else:
                print("Não foi possível realizar a operação")

            opc = input("Deseja fazer outra operação? Digite 'sim' para continuar ou 'q' para sair: ")

        # -----------------------------Alterar Horário-----------------------------------------#

        if opc == 'alt_h':
            num_sala = int(input("Informe a sala que deseja alterar o horário: "))
            sala_desejada = discover_sala(num_sala)

            nome_s = input("Nome do novo sócio para reserva: ")
            while not valida_nome(nome_s):
                print("Sócio não registrado ou nome estar incorreto")
                nome_s = input("Informe o nome sócio novamente: ")
            nome_s = secrt.buscarSocio(nome_s)

            data_r = input("Informe a data: ")

            horario_incial, horario_final = input("Informe o horário no seguinte formato -> hh:mm-hh:mm ").split("-")
            horario = horario_incial + "-" + horario_final
            while valida_horario(horario, lista_horarios) == False:
                print("Horario não cadastrado.")
                horario_incial, horario_final = input(
                    "Informe novamente o horário no seguinte formato -> hh:mm-hh:mm : ")
                horario = horario_incial + "-" + horario_final

            if sala_desejada.alterar_horario(data_r, horario, nome_s, registro_geral) != False:
                print("Alteração feita com sucesso")
            else:
                print("Não foi possível realizar a operação")

            opc = input("Deseja fazer outra operação? Digite 'sim' para continuar ou 'q' para sair: ")

        # -----------------------------Consultar Reservas -----------------------------------------#

        if opc == 'const_d':

            nome_s = input("Nome do sócio na reserva: ")
            while not valida_nome(nome_s):
                print("Sócio não registrado ou nome estar incorreto")
                nome_s = input("Informe o nome sócio novamente: ")
            nome_s = secrt.buscarSocio(nome_s)

            data_r = input("Informe a data: ")

            pesquisar_reservas_dia(nome_s, data_r, registro_geral)

            opc = input("Deseja fazer outra operação? Digite 'sim' para continuar ou 'q' para sair: ")

        # -----------------------------Consultar Disponibilidade -----------------------------------------#

        if opc == 'disp':

            data_r = input("Informe a data: ")

            horario_incial, horario_final = input("Informe o horário no seguinte formato -> hh:mm-hh:mm ").split("-")
            horario = horario_incial + "-" + horario_final
            while valida_horario(horario, lista_horarios) == False:
                print("Horario não cadastrado.")
                horario_incial, horario_final = input(
                    "Informe novamente o horário no seguinte formato -> hh:mm-hh:mm : ")
                horario = horario_incial + "-" + horario_final

            pesquisar_salas_livres(data_r, horario)

            opc = input("Deseja fazer outra operação? Digite 'sim' para continuar ou 'q' para sair: ")
        print("Regitos das reservas realizadas")
        print(registro_geral)


if __name__ == '__main__':
    main()