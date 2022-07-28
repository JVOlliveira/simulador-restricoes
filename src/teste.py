import PySimpleGUI as GUI

layout = [[
  GUI.Column([
    [
      GUI.Listbox(values=[], enable_events=True, size=(70, 25), key="_lista_")
    ]
  ]),
  GUI.VSep(),
  GUI.Column([
    [
      GUI.In(size=(30, 1)),
      GUI.B("PESQUISAR", size=(10, 1))
    ],
    [
      GUI.Listbox(values=[], size=(45, 25))
    ]
  ])
]]

GUI.Window(
  title="Teste",
  layout=layout,
  size=(900, 425)
).read()
