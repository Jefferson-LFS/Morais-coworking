from modelo.sala import Sala
class Sala_1(Sala):
    def __init__(self, data: str = None, horario: str = None, socio: str = None):
        super().__init__(data, horario, socio)

        self.num_sala = "1"
        self.num_lugares = "5"






