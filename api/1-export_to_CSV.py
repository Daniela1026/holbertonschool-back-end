#!/usr/bin/python3
""" CSV EXPORT"""
import csv
from requests import get
from sys import argv


def csv_expor():
    """CSV EXPORT"""

    user_url = get("https://jsonplaceholder.typicode.com/users").json()
    task_url = get("https://jsonplaceholder.typicode.com/todos").json()

    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        writ = csv.writer(f, quoting=csv.QUOTE_ALL)
        
        for task in task_url:
            writ.writerow([user_url['id'], user_url['username'],
                                task_url['completed'], task_url['title']])
