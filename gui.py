import PySimpleGUI as sg
import functions
import time

sg.theme("LightGreen1")

clock = sg.Text("", key="clock")
labels = sg.Text("Type in to do")

input_text = sg.InputText(tooltip="enter to do", key="todo")
add_button = sg.Button(button_text="Add")
list_box = sg.Listbox(values=functions.get_todo(), size=(40, 15), key="todos", enable_events=True)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
layout = [[clock], [labels, input_text, add_button],
          [list_box, edit_button, complete_button], [exit_button]]
window = sg.Window('To do list App',
                   layout=layout,
                   font=("Sitka, Text", 12))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%Y %m %d %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                print(new_todo)

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                print(index)
                todos[index] = new_todo + "\n"
                functions.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select list item to edit",
                         background_color="gray", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todo()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                # todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select item to complete", background_color="gray", font=("Helvetica", 14))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            exit()

window.close()
