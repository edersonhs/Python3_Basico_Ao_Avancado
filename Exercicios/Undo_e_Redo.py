"""
Faça uma lista de tarefas com as seguintes opções:
    Adicionar tarefa
    Listar tarefas
    Opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação)
    Opção de refazer (a acda vez que chamarmos, refaz a ultima ação)
"""

def show_op(todo_list):
    print('\nTarefas: ')
    print(todo_list)
    print()


def do_add(todo, todo_list):   # Adiciona tarefa
    todo_list.append(todo)


def do_undo(todo_list, redo_list):
    if not todo_list:   # Se a lista estiver vazia == True
        print('Nada a desfazer.')
        return
    
    last_todo = todo_list.pop()   # remove o ultimo valor da lista de tarefaz e salva o valor na last_todo
    redo_list.append(last_todo)   # Adiciona o ultimo valor da lista de tarefas na lista de refazer

def do_redo(todo_list, redo_list):
    if not redo_list: # Se a lista estiver vazia == True
        print('Nada a refazer.')
        return
    
    last_redo = redo_list.pop()   # remove o ultimo valor da lista de refazer e salva na last_redo
    todo_list.append(last_redo)   # Adiciona o ultimo valor da lista de refazer na lista de tarefas


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':   # Listar
            show_op(todo_list)
            continue
        elif todo == 'undo':   # Desfazer
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':   # Refazer
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)
