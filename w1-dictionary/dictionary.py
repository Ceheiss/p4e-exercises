name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email_counter = dict()
email_addresses = list()


for line in handle:
    if line.startswith('From '):
        email_addresses.append(line.split()[1])
   
        
for email in email_addresses:
    email_counter[email] = email_counter.get(email, 0) + 1

biggestNumber = None
biggestEmail = None

for email,times in email_counter.items():
    if biggestNumber == None or times > biggestNumber:
        biggestNumber = times
        biggestEmail = email
        
print(biggestEmail, biggestNumber)