from modelo.sala import Sala
class Sala_4(Sala):
    def __init__(self, data: str = None, horario: str = None, socio: str = None):
        super().__init__(data, horario, socio)

        self.num_sala = "4"
        self.num_lugares = "30"
