import PySimpleGUI as sg
import functions

lables = sg.Text("Type in to do")
print(type(lables))
input_text = sg.InputText(tooltip="enter to do")
add_button = sg.Button(button_text='add to to')

window = sg.Window('To do list App', layout=[[lables, input_text, add_button]])
print(type(window))
window.read()
window.close()


