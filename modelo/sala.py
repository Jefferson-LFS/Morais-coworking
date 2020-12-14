class Sala():
    def __init__(self, data: str = None, horario: str = None, socio: str = None):
        self.__data = data
        self.__horario = horario
        self.__socio = socio
        self.__num_sala = ""
        self.__num_lugares = ""
        self.__registros_reserva = []


    def get_data(self):
        return self.__data

    def set_data(self, novaData):
            self.__data = novaData

    def get_horario(self):
        return self.__horario

    def set_horario(self, novoHorario: str):
        self.__horario = novoHorario


    def get_socio(self):
        return self.__socio

    def set_socio(self, novoSocio):
        self.__socio = novoSocio

    def get_num_sala(self):
        return self.__num_sala

    def set_num_sala(self, novoValor):
        self.__num_sala = novoValor

    def get_num_lugares(self):
        return self.__num_lugares

    def set_num_lugares(self, novoValor):
        self.__num_lugares = novoValor

    def reservar(self, data, horario, socio, lista_geral):
        self.data = data
        self.horario = horario
        self.socio = socio
        self.__registros_reserva.append([" "] * 4)
        self.__registros_reserva[len(self.__registros_reserva) - 1][0] = self.data
        self.__registros_reserva[len(self.__registros_reserva) - 1][1] = self.horario
        self.__registros_reserva[len(self.__registros_reserva) - 1][2] = self.__socio
        self.__registros_reserva[len(self.__registros_reserva) - 1][3] = self.__num_sala
        self.registro_geral(lista_geral)

    def registro_geral(self, lista_geral):
        lista_geral.append(self.__registros_reserva[len(self.__registros_reserva) - 1])

    def registros(self):
        if self.__registros_reserva:
            return self.__registros_reserva
        else:
            return False

    def remover_reserva(self, data, horario, socio, lista_geral):
        if [data, horario, socio, self.__num_sala] in (self.registros() and lista_geral):
            self.registros().remove([data, horario, socio, self.__num_sala])
            lista_geral.remove([data, horario, socio, self.__num_sala])
        else:
            return False

    def alterar_socio(self, data, horario, novo_socio, lista_geral):
        for rl in self.registros():
            if data == rl[0] and horario == rl[1]:
                rl[2] = novo_socio
                lista_geral[lista_geral.index(rl)][2] = novo_socio
                return "altereção feita com sucesso"
            if rl[2] == novo_socio:
                return "Já tem uma reserva para esse sócio"
        return False

    def alterar_horario(self, data, novo_horario, socio, lista_geral):
        for rl in self.registros():
            if data == rl[0] and socio == rl[2]:
                rl[1] = novo_horario
                lista_geral[lista_geral.index(rl)][1] = novo_horario
                return "altereção feita com sucesso"
            if rl[1] == novo_horario:
                return "Já tem uma reserva nesse horario"
        return False

    def disp_reserva(self, data, horario):
        if self.registros():
            for rl in self.registros():
                if data == rl[0] and horario == rl[1]:
                    return "Não está disponivel neste dia e horario"
        return f"Sala:{self.__num_sala}, número de lugares: {self.__num_lugares}"

    # property
    data = property(get_data, set_data)
    horario = property(get_horario, set_horario)
    socio = property(get_socio, set_socio)
    num_sala = property(get_num_sala, set_num_sala)
    num_lugares = property(get_num_lugares, set_num_lugares)
