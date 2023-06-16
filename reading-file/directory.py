import os 
print("Current working directory: ", os.getcwd())

os.mkdir("./new_dir")


## list all files in the current directory
print(os.listdir("./"))

## check if a file is a directory or a file
dir = "./"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
## cheat sheet https://docs.python.org/3/library/os.path.html

os.rmdir("./new_dir")
