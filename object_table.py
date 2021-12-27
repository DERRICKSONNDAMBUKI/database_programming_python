# From object to table

import sqlite3

conn = sqlite3.connect('./mydata.db')
c = conn.cursor()


class Person():
    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]


person2 = Person('Sensei', 'Ricky', 15)
c.execute(
    '''
    INSERT INTO persons VALUES (
        '{}',
        '{}',
        '{}'
    );
    '''.format(
        person2.first,
        person2.last,
        person2.age
    )
)

c.execute('''
          SELECT * FROM persons;
          ''')
print(c.fetchall())
conn.commit()
conn.close()
