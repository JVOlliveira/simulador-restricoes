class RepositorioStage:
  def __init__(self, connection) -> None:
    self.connection = connection
  
  def carregarFotorestricoes(self, ano, mes):
    query = """
      SELECT
        COD_SUBDIVISAO AS COD_SUB,
        LINHA,
        KM_INICIO,
        KM_FIM,
        VELOCIDADE,
        DATA_RESTRICAO,
        MOTIVO,
        DATA_FOTO
      FROM RESTRICAO.FOTO_RESTRICAO (NOLOCK)
      WHERE (DATA_RETIRADA IS NULL)
        AND (YEAR(CONVERT(date,DATA_FOTO,103)) = """ + str(ano) + """)
        AND (MONTH(CONVERT(date,DATA_FOTO,103)) >= """ + str(mes) + """)
        AND (DAY(CONVERT(date,DATA_FOTO,103)) >= 1)
        AND (COD_SUBDIVISAO IN(68, 70, 71, 73, 74, 98, 53, 55, 56, 92))
        AND (LINHA <> 'LPE') AND (LINHA <> 'LDE')
      ORDER BY DATA_FOTO
    """

    cursor = self.connection.cursor()
    return cursor.execute(query)