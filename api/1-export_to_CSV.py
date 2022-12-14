#!/usr/bin/python3
""" CSV EXPORT"""
import csv
from requests import get
from sys import argv


def csv_expor():
    """CSV EXPORT"""
    user_id = int(argv[1])

    user_url = get("https://jsonplaceholder.typicode.com/users").json()
    task_url = get("https://jsonplaceholder.typicode.com/todos").json()

    with open('{}.csv'.format(user_id), 'w') as f:
        for task in task_url:
            f.write('"{}","{}","{}","{}"\n'.format(
                user_id, user_name, task_completed_status, task_title))
