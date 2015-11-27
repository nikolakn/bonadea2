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
        
        menubar = self.menuBar()
        
        novipacijentAction = QAction('&Novi pacijent', self)        
        novipacijentAction.setShortcut('Ctrl+N')
        #novipacijentAction.triggered.connect(QtGui.qApp.quit)
        pretragapacijentAction = QAction('&Pretraga', self)        
        pretragapacijentAction.setShortcut('Ctrl+P')       
        obrisipacijentAction = QAction('&Obriši pacijenta', self)        
        obrisipacijentAction.setShortcut('Ctrl+O')
        
        izmeniosobljeAction = QAction('&izmeni podatke', self)        
        izmeniosobljeAction.setShortcut('Ctrl+i')       
        dodajosobljeAction = QAction('&Dodaj osoblje', self)        
        dodajosobljeAction.setShortcut('Ctrl+d')
        
        pacijentiMenu = menubar.addMenu('&Pacijenti')
        pacijentiMenu.addAction(novipacijentAction)
        pacijentiMenu.addAction(pretragapacijentAction)
        pacijentiMenu.addAction(obrisipacijentAction)
        osobljeMenu = menubar.addMenu('&Osoblje')
        osobljeMenu.addAction(izmeniosobljeAction)
        osobljeMenu.addAction(dodajosobljeAction)
        #fileMenu.addAction(exitAction)
        
        
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
        
        srednjilevi = QVBoxLayout()
        
        srednjivreme =  QHBoxLayout()
        label    = QLabel("Vreme: "+QTime.currentTime().toString("hh:mm"))
        f = QFont( "Arial", 10, QFont.Bold);
        label.setFont(f);
        label.setFixedWidth(250)
        button3 =  QPushButton("Zakazati");
        button4 =  QPushButton("Poništi zakazano");
        srednjivreme.addWidget(label)
        srednjivreme.addWidget(button3)
        srednjivreme.addWidget(button4)
        
        srednjiime =  QHBoxLayout()
        labelime    = QLabel("Prezime i ime:")
        labelime.setFont(f);
        self.comboime = QComboBox()
        self.comboime.setEditable(True)
        self.comboime.setFixedWidth(150)
        button5 =  QPushButton("Novi");
        button6 =  QPushButton("Obriši");
        srednjiime.addWidget(labelime)
        srednjiime.addWidget(self.comboime)
        srednjiime.addWidget(button5)
        srednjiime.addWidget(button6)
    
        srednjilevi.addLayout(srednjivreme)
        srednjilevi.addLayout(srednjiime)
        
        srednjidesni =  QHBoxLayout()
        listazavrsenih =  QListWidget(self) 
        listazavrsenih.setFixedHeight(100)
        button7 =  QPushButton("Očisti");
        srednjidesni.addWidget(listazavrsenih)
        srednjidesni.addWidget(button7)
        
        srednji.addLayout(srednjilevi)
        srednji.addStretch()
        srednji.addLayout(srednjidesni)
        srednji.setSizeConstraint(QLayout.SetMaximumSize)
                
        donji =   QHBoxLayout()
        donji.SetNoConstraint = True
        tab =  QTabWidget(self)
        tab1 = QWidget();
        tab2 = QWidget();
        donjitab1levo =   QHBoxLayout()
        listaposete =  QListWidget(self) 
        listaposete.setFixedWidth(150)
        listanalaz =  QTextEdit(self) 
        donjitab1levo.addWidget(listaposete)
        donjitab1levo.addWidget(listanalaz)
        tab2.setLayout(donjitab1levo)
        
        tab.addTab(tab1, "O pacijentu")
        tab.addTab(tab2, "posete ordiniciji")
        donji.setSizeConstraint(QLayout.SetMaximumSize)
        donji.addWidget(tab)       
        
        
        layout = QVBoxLayout()
        layout.addLayout(gornji)
        layout.addLayout(srednji)
        layout.addLayout(donji)
        #layout.addStretch()
        
        self.window.setLayout(layout)
        self.setCentralWidget(self.window);
        
    def initUI(self):
        self.setWindowIcon(QIcon('../images/Pill.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Bonadea')
        self.show()
            
   
