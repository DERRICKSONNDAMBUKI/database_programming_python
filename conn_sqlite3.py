import sqlite3

# create a new database file on our disk
conn = sqlite3.connect('mydata.db')
c= conn.cursor()
# creating tables
c.execute("""
          CREATE TABLE persons(
              first_name TEXT,
              last_name TEXT,
              age INTEGER
          );
          """)

# Inserting values
c.execute('''
          INSERT INTO persons VALUES 
          ('Ricky','Sensei',12)
          ('Zashil','Ndambuki',21)
          ('Natasha','Ndambuki',24);
          ''')
conn.commit()
conn.close()

