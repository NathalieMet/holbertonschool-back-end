#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
 data in the CSV format.
"""

import requests
import sys
import csv

if __name__ == "__main__":
    """Actions to be performed only when the script
    is run directly"""

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
        user_id = str(employee_data.get('id'))
        employee_name = employee_data.get('username')

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare data for CSV
        csv_data = []
        for todo in todos_data:
            task_completed_status = str(todo['completed'])
            task_title = todo['title']
            csv_data.append([user_id, employee_name,
                             task_completed_status, task_title])

        # Write to CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(["USER_ID", "USERNAME",
                                 "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            csv_writer.writerows(csv_data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
