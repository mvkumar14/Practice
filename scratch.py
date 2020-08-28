import sqlite3
class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y
    def __conform__(self,protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x,self.y)

p = Point(4.0,-3.2)

conn = sqlite3.connect(':memory:')

c = conn.cursor()

# create table
c.execute('''CREATE TABLE points
    (x,y)''')

# insert a row of data
c.execute("INSERT INTO points VALUES (?)", (p,))

# save changes
conn.commit()

# read data
c.execute("SELECT * FROM points")
print(c.fetchone())

conn.close()
