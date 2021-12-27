import sqlite3

conn = sqlite3.connect('./mydata.db')
c = conn.cursor()

# select all rows
c.execute(
    '''
    SELECT * FROM persons;
    '''
    )
print('all rows in the table are:\n ',c.fetchall())

# select specific row
c.execute('''
          SELECT * FROM persons WHERE last_name = 'Ndambuki';
          ''')
print('row with last name being Ndambuki are:\n ',c.fetchall())
conn.commit()
conn.close()