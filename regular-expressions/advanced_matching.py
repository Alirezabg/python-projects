import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

print(result.groups())
# ('Lovelace', 'Ada')

print(result[0])
# Lovelace, Ada

print(result[1])
# Lovelace

print(result[2])
# Ada

print("{} {}".format(result[2], result[1]))
# Ada Lovelace

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w* .-])$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
# Ada Lovelace

print(rearrange_name("Ritchie, Dennis"))
# Dennis Ritchie

print(rearrange_name("Hopper, Grace M."))
# Grace M. Hopper

print(rearrange_name("Voltaire"))
# Voltaire


print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# <re.Match object; span=(2, 7), match='ghost'>
# {5} means exactly 5

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# <re.Match object; span=(2, 7), match='scary'>
# {5} means exactly 5

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# ['scary', 'ghost', 'appea']

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
# ['scary', 'ghost']
# \b means word boundary

print(re.findall(r"\w{5,10}", "I really like strawberries"))
# ['really', 'strawberri']
# {5,10} means between 5 and 10

print(re.findall(r"\w{5,}", "I really like strawberries"))
# ['really', 'strawberries']
# {5,} means 5 or more

print(re.findall(r"s\w{,20}", "I really like strawberries"))
# ['strawberries']
# {,20} means 20 or less

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
# 12345

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])
# 34567

result =re.search(regex, "99 elephants in a [cage]")
# AttributeError: 'NoneType' object has no attribute 'groups'

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))
# 12345

print(extract_pid("99 elephants in a [cage]"))
# 

re.split (r"[.?!]", "One sentence. Another one? And the last one!")
# ['One sentence', ' Another one', ' And the last one', '']

re.split (r"([.?!])", "One sentence. Another one? And the last one!")
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
# 'Received an email for [REDACTED]'
# \w means word character
# + means one or more
# * means zero or more
# % means literal percent sign
# - means literal hyphen
# @ means literal at sign
# - means literal hyphen

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# 'Ada Lovelace'
# \2 means second capture group
# \1 means first capture group
# r means raw string

re.split(r"the|a", "One sentence. Another one? And the last one!")
# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']

