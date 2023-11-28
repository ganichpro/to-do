import PySimpleGUI as sg
import functions

lables = sg.Text("Type in to do")

input_text = sg.InputText(tooltip="enter to do", key="todo")
add_button = sg.Button(button_text="Add")

window = sg.Window('To do list App',
                   layout=[[lables, input_text, add_button]],
                   font=("Calibre", 15))

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break


