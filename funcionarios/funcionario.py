class Funcionario:
  def __init__(self, nomeF: str, cargo: str, ramal: int):
    self.__nomeF = nomeF
    self.__cargo = cargo
    self.__ramal = ramal

  def get_nomeF(self):
      return self.__nomeF

  def set_nomeF(self, novoNomeF):
      self.__nomeF = novoNomeF

  def get_cargo(self):
      return self.__cargo

  def set_cargo(self, novoCargo):
      self.__cargo = novoCargo

  def get_ramal(self):
      return self.__ramal

  def set_ramal(self, novoRamal):
      self.__ramal = novoRamal

  @property
  def nomeF(self):
    return self.__nomeF

  @nomeF.setter
  def nomeF(self, novoNomeF: str):
    self.__nomeF = novoNomeF

  @property
  def cargo(self):
    return self.__cargo

  @cargo.setter
  def cargo(self, novoCargo: str):
    self.__cargo = novoCargo

  @property
  def ramal(self):
    return self.__ramal

  @ramal.setter
  def ramal(self, novoRamal: int):
    self.__ramal = novoRamal
