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

# write your code here

dir_url = args[1]

try:
    os.mkdir(dir_url)
except IOError:
    pass

tabs = []

websites = ["bloomberg", "nytimes"]

while True:
    url = input()
    if "." in url:

        url = url.rstrip(".com")
        print(url)
        tabs_location =  dir_url + "/" + url + ".txt"

        if url == websites[0]:
            print(bloomberg_com)
            if url not in tabs:
                tabs.append(url)
            with open(tabs_location, "w") as file:
                file.write(bloomberg_com)
        elif url == websites[1]:
            print(nytimes_com)
            if url not in tabs:
                tabs.append(url)
            with open(tabs_location, "w") as file:
                file.write(nytimes_com)
        else:
            print("error")
    elif url in tabs:
        with open(dir_url + "/" + url + ".txt", "r") as file:
            print(file.read())

    elif url == "exit":
        break
    else:
        print("error")