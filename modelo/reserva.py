class Reserva:
    def __init__(self, data: str, horario: str, num_sala: int, socio: str):
        self.__data = data
        self.__horario = horario
        self.__num_sala = num_sala
        self.__socio = socio

    def get_data(self):
        return self.__data

    def set_data(self, novaData):
        self.__data = novaData

    def get_horario(self):
        return self.__horario

    def set_horario(self, novoHorario):
        self.__horario = novoHorario

    def get_num_sala(self):
        return self.__num_sala

    def set_num_sala(self, novoNum_Sala):
        self.__num_sala = novoNum_Sala

    def get_socio(self):
        return self.__socio

    def set_socio(self, novoSocio):
        self.__socio = novoSocio

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data: str):
        self.__data = nova_data

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, novo_horario: str):
        self.__horario = novo_horario

    @property
    def num_sala(self):
        return self.__num_sala

    @num_sala.setter
    def num_sala(self, nova_sala: int):
        self.__num_sala = nova_sala

    @property
    def socio(self):
        return self.__data

    @socio.setter
    def socio(self, novo_socio: str):
        self.__socio = novo_socio

