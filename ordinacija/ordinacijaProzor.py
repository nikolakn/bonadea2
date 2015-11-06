'''
Created on Nov 6, 2015

@author: nikola
'''

#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

class ordinacijaProzor(QMainWindow):
    
    def __init__(self,login,name):
        super(ordinacijaProzor, self).__init__()
        self.initUI(name)
        
    def initUI(self, nn):
        self.setWindowIcon(QIcon('../images/Pill.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle("Bonadea - "+nn)
        self.show()