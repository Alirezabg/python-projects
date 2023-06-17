import re
result = re.search(r"aza", "plaza")
print(result)
# <re.Match object; span=(2, 5), match='aza'>
# span=(2, 5) means the match starts at index 2 and ends at index 5¬
result = re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(1, 4), match='aza'>
# span=(1, 4) means the match starts at index 1 and ends at index 4
result = re.search(r"aza", "maze")
print(result)
# None
result = re.search(r"^x","xenon")
print(result)
# <re.Match object; span=(0, 1), match='x'>
result = re.search(r"p.ng", "penguin")
print(result)
# <re.Match object; span=(0, 4), match='peng'>
result = re.search(r"p.ng", "clapping")
print(result)
# <re.Match object; span=(4, 8), match='ping'>