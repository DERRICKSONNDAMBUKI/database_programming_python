import sqlite3

conn = sqlite3.connect('./mydata.db')
c = conn.cursor()

# select all rows
c.execute(
    '''
    SELECT * FROM persons;
    '''
    )
print(c.fetchall())

# select specific row
c.execute('''
          SELECT * FROM persons WHERE last_name = 'Ndambuki';
          ''')
print(c.fetchall())
conn.commit()
conn.close()