#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports data in CSV format."""
import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    finished_tasks = [(user.get("id"), user.get("username"), t.get('completed'), t.get('title')) for t in todos]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished_tasks), len(todos)))
    [print("\t {}".format(c[3])) for c in finished_tasks]

    # Exporting data to CSV file
    csv_file_name = "{}.csv".format(user.get("id"))
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Writing CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Writing task records
        csv_writer.writerows(finished_tasks)

    print("Data exported to {}".format(csv_file_name))

if __name__ == "__main__":
    # Accepting employee ID as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
