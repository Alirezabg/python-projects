
file = open("./spider.txt")
print(file.readline())
print(file.read())
file.close()
## always close the file after reading it

with open("./spider.txt") as file:
    print(file.readline())
## when using with we don't need to close the file

