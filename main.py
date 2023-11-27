# from functions import get_todo, write_todo
import functions

while True:
    user_prompt = input("Enter add, show, edit, complete or exit: ".title()).strip()

    if user_prompt.startswith("add"):
        user_prompt = user_prompt[4:]
        todos = functions.get_todo()
        todos.append(user_prompt + "\n")

        functions.write_todo(todos)

    elif user_prompt.startswith("show"):
        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}.{item}".title())

    elif user_prompt.startswith("edit"):
        user_prompt = int(user_prompt[5:])
        todos = functions.get_todo()
        new_todo = input("Enter new todo: ")
        todos[user_prompt - 1] = new_todo + "\n"
        functions.write_todo(todos)

    elif user_prompt.startswith("complete"):
        user_prompt = int(user_prompt[9:])
        index = user_prompt - 1

        todos = functions.get_todo()

        to_complete = todos[index].strip("\n")
        todos.pop(index)
        functions.write_todo(todos)
        print(f"you have completed '{to_complete}'")

    elif user_prompt.startswith("exit"):
        break
    else:
        print("command not valid:")

print("Bye!")


