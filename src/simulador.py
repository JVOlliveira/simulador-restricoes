from time import time
import pyodbc
from interface import UI
from repositorios.stage import RepositorioStage
from modelos.fotorestricao import Fotorestricao

try:
  print("Tentando conexão com Stage [10.200.92.45]")
  connection = pyodbc.connect('DRIVER={SQL Server};SERVER=10.200.92.45;DATABASE=all_stage;Trusted_Connection=yes')
  print("Stage conectado com sucesso...")
except Exception as erro:
  print("Não foi possível conectar-se ao Stage motivo:", erro)

if __name__ == "__main__":
  interface = UI()
  repositorioStage = RepositorioStage(connection)
  fotos = []

  tempoInicio = time()

  print("Gerando fotorestriçoes atuais")
  dados = repositorioStage.carregarFotorestricoes(2022, 6)

  for indice, foto in enumerate(dados):
    # Formatação dos dados
    tipoANTT = "" # Iniciar variavel como nulo caso não seja uma restrição de ANTT

    if foto[1] == "LPL" or foto[1] == "LDL":
      linha = foto[1][:-1]
    else:
      linha = foto[1]
    
    if "ANTT" in foto[6]:
      origem = "ANTT"

      if "PN" in foto[6]:
        tipoANTT = "PN"
      else:
        tipoANTT = "PU"
    else:
      origem = "VIA"

    fotos.append(Fotorestricao(
      cod_sub=foto[0],
      linha=linha,
      kmInicio=foto[2],
      kmFim=foto[3],
      velocidade=foto[4],
      data=foto[5].strftime('%d/%m/%Y %H:%M:%S'),
      motivo=foto[6],
      dataFoto=foto[7].strftime('%d/%m/%Y %H:%M:%S'),
      origem=origem,
      tipoANTT=tipoANTT
    ).dict())

    if indice == 10:
      break
  
  print("Fechando conexão com Stage")
  try:
    dados.close()
    connection.close()
  except Exception as erro:
    print("Não foi possível fechar conexão, motivo:", erro)
  
  tempoTotal = time() - tempoInicio
  
  print(f"Tempo total de execução: {tempoTotal}s")

  interface.montar()