new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop()) #перенёс элемент в одно действие

new_tasks.remove('task_007') #удалил 007

print(f'Задача с высшим приоритетом - {new_tasks[2]}') #если просто вывести на экран, не меняя расположение в списке

print(new_tasks)
print(completed_tasks)