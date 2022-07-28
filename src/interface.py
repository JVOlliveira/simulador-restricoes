import PySimpleGUI as GUI

class UI:
  def __init__(self) -> None:
    self.layout = [[
      GUI.Column([
        [
          GUI.Listbox(values=[], enable_events=True, size=(70, 25), key="_lista_")
        ]
      ]),
      GUI.VSep(),
      GUI.Column([
        [
          GUI.In(size=(30, 1)),
          GUI.B("PESQUISAR", size=(10, 1), enable_events=True, key="_pesquisar_")
        ],
        [
          GUI.Listbox(values=[], size=(45, 25))
        ]
      ])
    ]]
  
  def montar(self):
    GUI.Window(
      title="Simulador de Restrições",
      layout=self.layout,
      size=(900, 425)
    ).read()

    

