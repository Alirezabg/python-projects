import csv
f = open('data.csv')
csv_f =csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print('Name: {}, Phone: {}, Role: {}'.format(name, phone, role))
f.close()

hosts = [["workstation.local", "192.168.1.1"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

f2 = open('hosts.csv')
csv_f2 =csv.reader(f2)
for row in csv_f2:
    name, ip = row
    print('Domain: {}, IP: {}'.format(name, ip))
f.close()

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
            {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)