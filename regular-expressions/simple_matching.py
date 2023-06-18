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


print(re.search(r"[Pp]ython", "Python"))
# <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'>
print(re.search(r"[a-z]way", "What a way to go"))
# None
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
# <re.Match object; span=(0, 6), match='cloud9'>
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# <re.Match object; span=(4, 5), match=' '>
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# <re.Match object; span=(30, 31), match='.'>


print(re.search(r"cat|dog", "I like cats."))
# <re.Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I like dogs."))
# <re.Match object; span=(7, 10), match='dog'>
print(re.findall(r"cat|dog", "I like both cats and dogs."))
# ['cat', 'dog']
print(re.search(r"Py.*n", "Pygmalion"))
# <re.Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>
print(re.search(r"Py[a-z]*n", "Python Programming"))
# <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"Py[a-z]*n", "Pyn"))
# <re.Match object; span=(0, 3), match='Pyn'>
print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", "boil"))
# None
print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "I like peaches"))
# <re.Match object; span=(7, 12), match='peach'>

print(re.search(r"p+","piiiii"))
# <re.Match object; span=(0, 6), match='p'>

print(re.search(r".com","welcome"))
# <re.Match object; span=(2, 6), match='lcom'>
# . means any character
# \ means escape
print(re.search(r"\.com","welcome"))
# None
print(re.search(r"\.com","mydomain.com"))
# <re.Match object; span=(8, 12), match='.com'>

print(re.search(r"\w*", "This is an example"))
# <re.Match object; span=(0, 4), match='This'>
# \w means word character
# * means zero or more
print(re.search(r"\w*", "And_this_is_another"))
# <re.Match object; span=(0, 20), match='And_this_is_another'>
print(re.search(r"\w*", "And_this_is_another"))
# <re.Match object; span=(0, 20), match='And_this_is_another'>

print(re.search(r"\d*", "This is an example"))
# <re.Match object; span=(0, 0), match=''>
# \d means digit

print(re.search(r"\s*", "This is an example"))
# <re.Match object; span=(0, 0), match=''>
# \s means whitespace

print(re.search(r"\b\w{6}\b", "The End"))
# <re.Match object; span=(4, 7), match='End'>
# \b means word boundary

print(re.search(r"A.*a", "Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"A.*a", "Azerbaijan"))
# <re.Match object; span=(0, 9), match='Azerbaija'>
# * is greedy

print(re.search(r"^A.*a$", "Azerbaijan"))
# None
# ^ means start of string
# $ means end of string

print(re.search(r"^A.*a$", "Australia"))
# <re.Match object; span=(0, 9), match='Australia'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
# <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>

print(re.search(pattern,"my_variable1"))
# <re.Match object; span=(0, 12), match='my_variable1'>
print(re.search(pattern,"2my_variable1"))
# None