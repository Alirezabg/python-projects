with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

## we can use the write method to write to a file
## if the file doesn't exist it will be created
## if the file does exist it will be overwritten
## we can use the append mode to append to the file

with open("novel.txt", "a") as file:
    file.write("It was a dark and stormy night")


