from modelo.sala import Sala
class Sala_3(Sala):
    def __init__(self, data: str = None, horario: str = None, socio: str = None):
        super().__init__(data, horario, socio)

        self.num_sala = "3"
        self.num_lugares = "30"
