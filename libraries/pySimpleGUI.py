import PySimpleGUI as sg

layout = [
    [sg.Canvas(size=(200, 200), background_color='white', key='canvas')],
    [sg.Button('Draw')]
]

window = sg.Window('Simple Drawing', layout, finalize=True)
canvas_elem = window['canvas'].TKCanvas
canvas = canvas_elem.create_line(10, 10, 100, 100, fill='blue')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Draw':
        canvas_elem.create_oval(50, 50, 150, 150, fill='red')

window.close()
