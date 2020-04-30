import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

args = sys.argv
dir_command = args[1]

# Creates a local directory in your machine to store data
try:
    os.mkdir(dir_command)
except IOError:
    pass

# Stores already visited tabs
tabs = []

# Stores websites in the world
websites = []
history = []


def isurl(string):
    if string.endswith(".com") or string.endswith(".org"):
        return True
    else:
        return False


def get_response(url):
    r = requests.get("https://" + url)

    return r


# Browser interaction starts here

init(autoreset=True)
while True:
    command = input('> ')
    if isurl(command):
        response = get_response(command)
        if response:
            soup = BeautifulSoup(response.content, "html.parser")
            command = command.rstrip(".com")
            file_dir = dir_command + "/" + command + ".txt"

            data_rows = []
            tags = ['a', 'p', 'ul', 'ol', 'li']
            for tag in soup.find_all(tags):
                if tag.name == 'a':
                    data_rows.append(Fore.BLUE + tag.get_text() + Fore.RESET)
                else:
                    data_rows.append(tag.get_text())

            web_content = '\n'.join(data_rows)

            print(web_content)
            if command not in tabs:
                tabs.append(command)
            with open(file_dir, "w", encoding="utf-8") as file:
                file.write(web_content)
                history.append(file_dir)
        else:
            print("error")

    # Command to go back one page
    elif command == "back":
        history.pop()
        with open(history.pop(), "r") as file:
            print(file.read())

    # Saves visited pages in local machine, and saves history
    elif command in tabs:
        file_dir = dir_command + "/" + command + ".txt"
        with open(file_dir, "r") as file:
            print(file.read())
            history.append(file_dir)

    elif command == "exit":
        break
    else:
        print("error")
