#!/usr/bin/env python3
import sys
import re


pattern = r"USER \((\w+)\)$"
logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"

        result = re.search(pattern, line)
        print(result[1])

## log file
# Jul  1 09:11:01 mycomputer CRON[29440]: USER (naomi)
# Jul  1 09:11:01 mycomputer CRON[29441]: USER (naomi)
# Jul  1 09:11:01 mycomputer CRON[29442]: USER (naomi)
# Jul  1 09:11:01 mycomputer CRON[29443]: USER (naomi)
# Jul  1 09:11:01 mycomputer CRON[29444]: USER (naomi)

# python3 log_file.py /var/log/syslog
# Jul  1 09:11:01 mycomputer CRON[29440]: USER (naomi)
# Jul  1 09:11:01 mycomputer CRON[29441]: USER (naomi)


