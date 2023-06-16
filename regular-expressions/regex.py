import re # import the regular expression module
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
# r means raw string
# \d means digit
# + means one or more
# \[ means literal open bracket
# \] means literal close bracket
# () means capture group
# \d+ means one or more digits
# \[\d+\] means one or more digits between square brackets
# \[(\d+)\] means one or more digits between square brackets, but only the digits are captured
result = re.search(regex, log)
print(result[1])