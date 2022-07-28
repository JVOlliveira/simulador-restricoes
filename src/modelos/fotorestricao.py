class Fotorestricao:
  def __init__(self, cod_sub, linha, kmInicio, kmFim, velocidade, data, motivo, dataFoto, origem, tipoANTT) -> None:
    self.cod_sub = cod_sub
    self.linha = linha
    self.kmInicio = kmInicio
    self.kmFim = kmFim
    self.velocidade = velocidade
    self.data = data
    self.motivo = motivo
    self.dataFoto = dataFoto
    self.origem = origem
    self.tipoANTT = tipoANTT

  def dict(self):
    return self.__dict__
