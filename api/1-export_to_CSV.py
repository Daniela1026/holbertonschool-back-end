#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import json
import requests


def export_csv():
    """
        EXPORT_CSV
    """

    task_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users?id="
    response_todo = requests.get(task_url)
    response_users = requests.get(user_url)

    content_task = list(response_todo.json())
    content_users = list(response_users.json())

    total_tasks = {}
    for user in content_users:

        response = []
        for i in content_task:
            todo = {}
            todo['username'] = user['username']
            todo['task'] = i['title']
            todo['completed'] = i['completed']

            if user['id'] == i['userId']:
                response.append(todo)

        total_tasks[user['id']] = response

    jsonString = json.dumps(total_tasks)
    with open('todo_all_employees.json', 'w') as f:
        f.write(jsonString)


if __name__ == "__main__":
    export_csv()
