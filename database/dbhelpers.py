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


    def addNewOsoblje(self,ime,potpis,tip,password):
        try:
            query = "INSERT INTO osoblje(TIP,UNAME,PSW,POTPIS) VALUES(%s,%s,%s,%s)"
            args = (tip, ime, password, potpis)
            self.cursor.execute(query, args)
            #self.cursor.executemany(query, books)
            self.cnx.commit()
            return True
        except Error as error:
            print(error)
            return False

    def delOsoblje(self,ime):
        try:
            query = "DELETE FROM osoblje WHERE UNAME = %s"
            self.cursor.execute(query, (ime,))
            self.cnx.commit()
            return True
        except Error as error:
            print(error)
            return False

