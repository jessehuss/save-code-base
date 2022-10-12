import json
import os

def write_file(path, contents):
    print("Wrote contents to: " + path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(contents)
        f.close

def write_directory(path):
    print("Writing Directory: ", path)
    try: 
        if not os.path.exists(path):
            os.mkdir(path) 
    except OSError as error: 
        print(error) 

def destruct_directory(path, contents):
    write_directory(path)

    for x in contents:
        if (contents[x]['isDir']):
            print ('Destructing Directory')
            destruct_directory(path + '/' + x, contents[x]['content'])
        else:
            print ('Writing File Contents')
            write_file(path + '/' + x, contents[x]['content'])
            

# repo_path = "C:/Users/laptop/Documents/Projects/Laravel-Livewire-Tailwind-Boilerplate"
# file = open("C:/Users/laptop/Documents/laravel-livewire-tailwind-boilerplate.json")
repo_path = "PROJECT PATH"
file = open("PROJECT DIRECTORY JSON FILE")
data = json.load(file)

# WRITE PROJECT DIRECTORY
destruct_directory(repo_path, data)
