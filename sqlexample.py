# Import modules
import sqlite3

# Connect a handler to the external file
pupils10 = sqlite3.connect('class.db')

# Create a new cursor object to manipulate the database
xxxx = pupils10.cursor()

# Create a table
xxxx.execute('''CREATE TABLE Students
(ID text,
firstname text,
surname text,
dateOB text,
tutorGroup text)
''')

# Insert data into table
xxxx.execute('''INSERT INTO Students VALUES ('P007','Bill','Gates','28/10/1955','48F')''')

#Save changes [commit]
pupils10.commit()

#Close connection to the database
pupils10.close()

