'''
Created on Nov 5, 2015

@author: nikola
'''
import mysql.connector
from mysql.connector import  Error

class db(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def open(self):
        try:   
            self.cnx = mysql.connector.connect(user='root', password='proba',
                              host='192.168.0.19',
                              database='bonadea')
            self.cursor = self.cnx.cursor()
            
        except Error as e:
            print(e)
            return False

        return True
        
    def close(self):
        self.cursor.close()
        self.cnx.close()    
        
    def osobljeList(self):
        data = []
        data.append("")
        self.cursor.execute("SELECT * FROM osoblje")
        row = self.cursor.fetchone()
        while row is not None:
            data.append(row[5])
            row = self.cursor.fetchone()   
        return data
    
    def login(self,ime,password):
        self.cursor.execute("SELECT * FROM osoblje WHERE UNAME='"+ime+"'")
        rows = self.cursor.fetchall()
        if (self.cursor.rowcount != 1):
            return -1
        sifra = rows[0][6]
        pristup = rows[0][2]
        if(sifra != password):
            return -1
        return pristup




'''
def insert_book(title, isbn):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
    args = (title, isbn)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   insert_book('A Sudden Light','9781439187036')

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_books(books):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.executemany(query, books)
 
        conn.commit()
    except Error as e:
        print('Error:', e)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
    books = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
             ('Gone with the Wind', '9780446675536'),
             ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
    insert_books(books)
 
if __name__ == '__main__':
    main()


from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def delete_book(book_id):
    db_config = read_db_config()
 
    query = "DELETE FROM books WHERE id = %s"
 
    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)
 
        # execute the query
        cursor = conn.cursor()
        cursor.execute(query, (book_id,))
 
        # accept the change
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    delete_book(102)
'''    