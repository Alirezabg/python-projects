guests = open("guests.txt", "w")
initial_guests = ["Ali", "Joe", "Emanuel", "Sally", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()        

guests_to_check = ['Ali', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

            