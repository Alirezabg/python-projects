import os 
import datetime
import subprocess

## remove file
## first run python3 writing-file.py to create novel.txt
os.remove("./novel.txt")


os.rename("./spider.txt", "./spider_rename.txt")

os.rename("./spider_rename.txt", "./spider.txt")

## check if file exists
os.path.exists("./novel.txt")

os.path.exists("./spider.txt")

if os.path.exists("./novel.txt"):
    print("novel File found")
elif not os.path.exists("./novel.txt"):
    print("novel File Not found")
    subprocess.run(["python3", "writing-file.py"])
    print("novel File created")
    

if os.path.exists("./spider.txt"):
    print("spider File found")
    print("Spider File size: ", os.path.getsize("./spider.txt"))
    times = os.path.getmtime("./spider.txt")
    datetime.datetime.fromtimestamp(times)
    print("Spider File last modified: ", datetime.datetime.fromtimestamp(times))


