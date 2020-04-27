import sys
import os
args = sys.argv

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

dir_command = args[1]

# Creates a local directory in your machine to store data
try:
    os.mkdir(dir_command)
except IOError:
    pass

# Stores already visited tabs
tabs = []

# Stores websites in the world
websites = ["bloomberg", "nytimes"]
history = []

# Browser interaction starts here
while True:
    command = input()
    if "." in command:

        command = command.rstrip(".com")
        print(command)
        file_dir = dir_command + "/" + command + ".txt"

        # If command was url to website 0
        if command == websites[0]:
            print(bloomberg_com)
            if command not in tabs:
                tabs.append(command)
            with open(file_dir, "w") as file:
                file.write(bloomberg_com)
                history.append(file_dir)

        # If command was url to website 1
        elif command == websites[1]:
            print(nytimes_com)
            if command not in tabs:
                tabs.append(command)
            with open(file_dir, "w") as file:
                file.write(nytimes_com)
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