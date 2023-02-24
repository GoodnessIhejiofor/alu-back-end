#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    json_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo_task = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo_task = todo_task.format(employee_id)

    user_info = requests.request("GET", json_url).json()
    todo_info = requests.request("GET", todo_task).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_completed = len(total_tasks)
    total_task_done = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_completed, total_task_done))
    
    [print("\t " + task["title"]) for task in task_completed]