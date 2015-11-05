'''
Created on Nov 5, 2015

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

class recepcijaProzor(QMainWindow):
    
    def __init__(self,login,name):
        super(recepcijaProzor, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(50, 50, 900, 720)
        self.setWindowTitle('Bonadea')
        self.show()
            
   
