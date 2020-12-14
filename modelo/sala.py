from abc import ABC, abstractmethod
class Sala(ABC):
    def __init__(self, data: str = None, horario: str = None):
        self.__data = data
        self.__horario = horario

    def get_data(self):
        return self.__data

    def set_data(self, novaData):
        self.__data = novaData

    def get_horario(self):
        return self.__horario

    def set_horario(self, novoHorario: str):
        self.__horario = novoHorario

    @abstractmethod
    def reservar(self):
        pass

    # def disp_reserva(self, data, horario):
    #     if is self.registros() != False:
    #       for rl in self.registros():
    #           if data != rl[0] and horario != rl[1]:
    #             print(f"Sala 1:{self.__num_sala}, número de lugares: {self.__num_lugares}")

    #     else:
    #       print(f"Sala 1:{self.__num_sala}, número de lugares: {self.__num_lugares}")

    # property
    data = property(get_data, set_data)
    horario = property(get_horario, set_horario)