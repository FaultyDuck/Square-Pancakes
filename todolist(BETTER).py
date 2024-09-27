todo_list = []

def add_task(name, desc):
    task = {
        'name': name,
        'description': desc,
        'completed': False
    }

    todo_list.append(task)
    test=task['name']
    print(f'Successfully added new task with name: {test}')

def remove_task(name):
    for task in todo_list:
        if task['name'] == name:
            todo_list.remove(task)
            print(f'Successfully removed task {name}')
            break

def mark_complete(name):
    for task in todo_list:
        if task['name'] == name:
            task['completed'] = True
            print(f'Successfully marked task {name} as complete')
            break

def view_all():
    for task in todo_list:
        print(f"Task name: {task['name']}, Description: {task['description']}, Completed: {task['completed']}")

add_task('test', 'buy groceries')
add_task('test two', 'cook')
remove_task('test')
mark_complete('test two')
view_all()