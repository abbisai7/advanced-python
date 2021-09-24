#data access player to perform crud operation on db

from os import chdir
import sqlite3
from sqlite3.dbapi2 import Cursor
from employee import Employee

def connect_db():
    global conn
    conn = sqlite3.connect("emp.db")
    global cursor
    cursor = conn.cursor()
    print("Connected to db")
    
def create_table():
    try:
        cursor.execute(""" CREATE TABLE employees (
             first text,
             last text,
             pay integer
        )""")
        
        print("Table is created")
        
    except Exception as e:
        print(e)

def insert_emp(emp):
    try:
        cursor.execute("""INSERT INTO employees values(:first,:last,:pay)""",
                       {'first':emp.first,'last':emp.last,'pay':emp.pay})
        cursor.execute("commit")
        print("data inserted")
    except Exception as e:
        print(e)

def get_emp_by_last_name(last_name):
    try:
        cursor.execute(" SELECT * FROM employees where last = :last",{"last":last_name})
        return cursor.fetchall()
    except Exception as e:
        print(e)

def remove_emp(name):
    pass


if __name__ == "__main__":
    connect_db()
    #create_table()
    #emp1 = Employee("sai","cha","28000000")
    #emp2 = Employee("murthy","rps","300000000")
    x = get_emp_by_last_name("cha")
    print(x)
    conn.close()
    
    