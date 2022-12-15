#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    response_users = requests.request("GET", "{}users".format(url))
    response_tasks = requests.request("GET", "{}todos".format(url))
    users_json = response_users.json()
    tasks_json = response_tasks.json()
    array = []
    for user in users_json:

        user_id = user['id']
        user_name = user['username']

        for task in tasks_json:
            if task['userId'] == user_id:
                tasks_dict = {}
                tasks_dict["username"] = user_name
                tasks_dict["task"] = task["title"]
                tasks_dict["completed"] = task["completed"]
                array.append(tasks_dict)

dict = {}
try:
    for user in users_json:
        user_id = user['id']
        user_name = user['username']
        arry = []
        for i in array:
            if i['username'] == user_name:
                arry.append(i)
        dict[user_id] = arry

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict, file)
except NameError:
    pass
