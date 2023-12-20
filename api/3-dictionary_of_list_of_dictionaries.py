#!/usr/bin/python3
"""
Records all tasks from all employees, export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    """Actions to be performed only when the script
    is run directly"""

    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_id_response = requests.get(base_url)
    employee_id_data = employee_id_response.json()

    json_data = {}

    for employee_data in employee_id_data:
        user_id = employee_data['id']
        employee_name = employee_data['username']
        employee_url = f"{base_url}/{user_id}"
        todos_url = f"{employee_url}/todos"

        try:
            # Fetch TODO list for the employee
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            # Prepare data for json
            json_data[user_id] = []
            for todo in todos_data:
                task_completed_status = todo['completed']
                task_title = todo['title']
                json_data[user_id].append({
                    "username": employee_name,
                    "task": task_title,
                    "completed": task_completed_status})

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            sys.exit(1)

        # Write to CSV file
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)
