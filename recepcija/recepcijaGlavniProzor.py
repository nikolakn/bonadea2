'''
Created on Nov 5, 2015

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
#from database import dbhelpers

class recepcijaProzor(QMainWindow):
    
    def __init__(self,login,name):
        super(recepcijaProzor, self).__init__()
        self.initUI()
        self.window = QWidget();
        gornji = QHBoxLayout()
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.setFixedSize(QSize(250,200))
        gornji.setStretch(1,1)
        lista =  QListWidget(self) 
        lista.setFixedHeight(200)
        gornji.addWidget(cal)
        gornji.addWidget(lista)
          
        srednji =  QHBoxLayout()
        button3 =  QPushButton("Three");
        button4 =  QPushButton("Four");
        srednji.addWidget(button3)
        srednji.addWidget(button4)
        srednji.setSizeConstraint(QLayout.SetMaximumSize)
                
        donji =   QHBoxLayout()
        tab =  QTabWidget(self)
        tab1 = QWidget();
        tab2 = QWidget();
        tab.addTab(tab1, "O pacijentu")
        tab.addTab(tab2, "posete ordiniciji")
        donji.setSizeConstraint(QLayout.SetMaximumSize)
        donji.addWidget(tab)       
        
        
        layout = QVBoxLayout()
        layout.addLayout(gornji)
        layout.addLayout(srednji)
        layout.addLayout(donji)
        layout.addStretch()
        
        self.window.setLayout(layout)
        self.setCentralWidget(self.window);
        
    def initUI(self):
        self.setWindowIcon(QIcon('../images/Pill.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Bonadea')
        self.show()
            
   
