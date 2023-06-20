import os 
import sys
import subprocess

print("HOME:" + os.environ.get("HOME", ""))
print("SHELL:" + os.environ.get("SHELL", ""))
print("FRUIT:" + os.environ.get("FRUIT", ""))

print(sys.path)
print( sys.argv)

result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))


result =subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)  # returncode = 1
print(result.returncode)
print(result.stdout)
print(result.stderr)

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env)

result = subprocess.run(["pwd"], cwd="/opt/myapp")
result = subprocess.run(["ls", "-l"], cwd="/opt/myapp")

result = subprocess.run(["ls", "-l"], cwd="/does_not_exist")  # FileNotFoundError





