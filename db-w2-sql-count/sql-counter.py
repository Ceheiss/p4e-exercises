import sqlite3

conn = sqlite3.connect('organizations-emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    # we get the content after the personal e-mail signature
    # that way we get the organization
    organization_email = pieces[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organization_email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (organization_email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (organization_email,))

conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("TOP TEN of organizations with most emails are:")
count = 0
for row in cur.execute(sqlstr):
    count = count + 1
    # Info comes as a tuple, row[0] is the email, row[1] the count
    print(count, "-", str(row[0]), row[1])

cur.close()