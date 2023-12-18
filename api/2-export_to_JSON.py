#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""

import requests
import sys
import json

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"
    todos_url = f"{employee_url}/todos"

    try:
        # Fetch employee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        user_id = employee_data.get('id')
        employee_name = employee_data.get('username')

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

		# Prepare data for json
        json_data = {user_id: []}
        for todo in todos_data:
            task_completed_status = todo['completed']
            task_title = todo['title']
            json_data[user_id].append({"task": task_title, "completed": task_completed_status, "username": employee_name})

        # Write to CSV file
        json_filename = f"{user_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
