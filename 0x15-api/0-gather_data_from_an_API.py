#!/usr/bin/python3
"""Will return information about a given employee ID's TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [tt_l.get('title') for tt_l in todos if
                 tt_l.get('completed') is True]
    print("Employee {} is done with tasks({}/{})".format(user.get('name'),
          len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
