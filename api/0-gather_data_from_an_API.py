#!/usr/bin/python3
"""Return the infor for employee
whose ID is passed in the script"""
from requests import get
from sys import argv


def api_todo():
    """Data struct"""
    employee_id = int(argv[1])
    employee_name = ""
    number_of_task = 0
    number_of_done_task = 0
    titles_of_task = []
    user_url = get("https://jsonplaceholder.typicode.com/users").json()
    task_url = get("https://jsonplaceholder.typicode.com/todos").json()

    for user in user_url:
        if user['id'] == employee_id:
            employee_name = user['name']

    for task in task_url:
        if task['userId'] == employee_id:
            if task['completed']:
                titles_of_task.append(task['title'])
                number_of_done_task += 1
            number_of_task += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          number_of_done_task,
                                                          number_of_task))

    for title in titles_of_task:
        print("\t {}".format(title))


if __name__ == "__main__":
    api_todo()


# Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

# Requirements:

# You must use urllib or requests module
# The script must accept an integer as a parameter, which is the employee ID
# The script must display on the standard output the employee  list progress in this exact format:
# First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
# EMPLOYEE_NAME: name of the employee
# NUMBER_OF_DONE_TASKS: number of completed tasks
# TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
# Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)


# for user in user_url:
    #     if user['id'] == employee_id:
    #         employee_name = user['name']

    # for task in  task_url:
    #     # if task['userId'] == employee_id:
    #         if task['completed'] is True:
    #             titles_of_task.append(task['title'])
    #             number_of_done_task += 1
    #         number_of_task_total += 1
    # if task.get('userId') == (userId):
