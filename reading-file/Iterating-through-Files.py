with open("./spider.txt") as file:
    for line in file:
        print(line.upper())
# ## we can iterate through the file line by line
# ## we can also use the readlines() method to read the file into a list

with open("./spider.txt") as file:
    for line in file.readlines():
        print(line.strip().upper())
# ## we can use strip() to remove the new line character