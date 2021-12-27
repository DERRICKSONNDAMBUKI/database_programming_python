import sqlite3

conn= sqlite3.connect('./mydata.db')
c= conn.cursor()

class Person():
    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age
        
    def clone_person(self,result):
        self.first = result[0]
        self.last=result[1]
        self.age = result[2]

c.execute('''
          SELECT * FROM persons WHERE last_name = 'Ndambuki'
          ''')
person1= Person()
person1.clone_person(c.fetchone())
conn.commit()
conn.close()
# Here we fetch the first entry of our query results, by using the fetchone
# function.
print(person1.first)
print(person1.last)
print(person1.age)