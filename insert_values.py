import sqlite3

conn = sqlite3.connect('./mydata.db')
c = conn.cursor()

# Inserting values
c.execute("""INSERT INTO persons VALUES ('Ricky','Sensei',12),
          ('Zashil','Ndambuki',21),
          ('Natasha','Ndambuki',24);
          """)
conn.commit()
conn.close()
