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
        opecijestampajzaglavlje = QAction('&zaglavlje', self)        
        
        pacijentiMenu = menubar.addMenu('&Pacijenti')
        pacijentiMenu.addAction(novipacijentAction)
        pacijentiMenu.addAction(pretragapacijentAction)
        pacijentiMenu.addAction(obrisipacijentAction)
        osobljeMenu = menubar.addMenu('&Osoblje')
        osobljeMenu.addAction(izmeniosobljeAction)
        osobljeMenu.addAction(dodajosobljeAction)
        opcije = menubar.addMenu('Opcije')
        opcije.addAction(opecijestampajzaglavlje)
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
          
          
        srednjiwidget = QWidget(); 

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
        srednjiwidget.setLayout(srednji)
                
        donji =   QHBoxLayout()
        donji.SetNoConstraint = True
        tab =  QTabWidget(self)
        tab1 = QWidget();
        tab2 = QWidget();
        tab1layout = QVBoxLayout()
        donjitab1gore =   QHBoxLayout()
        listaposete =  QListWidget(self) 
        listaposete.setFixedWidth(150)
        listanalaz =  QTextEdit(self) 
        donjitab1gore.addWidget(listaposete)
        donjitab1gore.addWidget(listanalaz)
        
        donjitab1dole =   QHBoxLayout()
        labevrsta   = QLabel("Vrsta intervencije:")
        labedoktor   = QLabel("Doktor:")
        intervencija = QLineEdit(self)
        doktor = QLineEdit(self)
        stampaj =  QPushButton("Štampaj nalaz");
        donjitab1dole.addWidget(labevrsta)
        donjitab1dole.addWidget(intervencija)
        donjitab1dole.addWidget(labedoktor)
        donjitab1dole.addWidget(doktor)
        donjitab1dole.addWidget(stampaj)
        
        tab1layout.addLayout(donjitab1gore)
        tab1layout.addLayout(donjitab1dole)
        tab2.setLayout(tab1layout)
        
        tablayout = QVBoxLayout()
        tgornji =   QHBoxLayout()
        
        brojkartona = QVBoxLayout()
        brojkartonalab   = QLabel("Broj Kartona:")
        brojkartonaed = QLineEdit(self)
        brojkartonaed.setMaximumWidth(50)
        brojkartona.addWidget(brojkartonalab)
        brojkartona.addWidget(brojkartonaed)
 
        t1ime = QVBoxLayout()
        t1imelab   = QLabel("Prezime i ime:")
        t1imeaed = QLineEdit(self)
        t1imeaed.setMaximumWidth(250)
        t1ime.addWidget(t1imelab)
        t1ime.addWidget(t1imeaed)
        
        t1datum= QVBoxLayout()
        t1datumlab   = QLabel("Datum rodjenja:")
        t1datumed = QDateTimeEdit (self)
        t1datumed.setDisplayFormat("dd.MM.yyyy");
        t1datumed.setCalendarPopup(True)
        t1datumed.setMaximumWidth(150)
        t1datum.addWidget(t1datumlab)
        t1datum.addWidget(t1datumed)
        
        t1pol = QVBoxLayout()
        t1pollab   = QLabel("Pol:")
        t1poled = QComboBox(self)
        t1pol.addWidget(t1pollab)
        t1pol.addWidget(t1poled)

        t1kontakt= QVBoxLayout()
        t1kontaktlab   = QLabel("Kontakt:")
        t1kontakted = QLineEdit(self)
        t1kontakt.addWidget(t1kontaktlab)
        t1kontakt.addWidget(t1kontakted)
                  
        
        tgornji.addLayout(brojkartona)
        tgornji.addLayout(t1ime)
        tgornji.addLayout(t1datum)
        tgornji.addLayout(t1pol)
        tgornji.addLayout(t1kontakt)
        
        tdonji  =   QHBoxLayout()       
        napomena = QVBoxLayout()
        napomenalab   = QLabel("NAPOMENA:")
        napomenaed = QTextEdit(self)
        napomena.addWidget(napomenalab)
        napomena.addWidget(napomenaed)
        
        alerg = QVBoxLayout()
        alerglab   = QLabel("MEDIKAMENTOZNE ALERGIJE:")
        alerged = QTextEdit(self)
        alerg.addWidget(alerglab)
        alerg.addWidget(alerged)
        
        dalerg = QVBoxLayout()
        dalerglab   = QLabel("DRUGE ALERGIJE:")
        dalerged = QTextEdit(self)
        dalerg.addWidget(dalerglab)
        dalerg.addWidget(dalerged)

        hron = QVBoxLayout()
        hronlab   = QLabel("HRONIČNA OBOLJENJA:")
        hroned = QTextEdit(self)
        hron.addWidget(hronlab)
        hron.addWidget(hroned)
                
        tdonji.addLayout(napomena)   
        tdonji.addLayout(alerg)  
        tdonji.addLayout(dalerg)  
        tdonji.addLayout(hron) 
        
        tablayout.addLayout(tgornji)
        tablayout.addLayout(tdonji)
        tablayout.addStretch()
        tab1.setLayout(tablayout)
       
        tab.addTab(tab1, "O pacijentu")
        tab.addTab(tab2, "posete ordiniciji")
        donji.setSizeConstraint(QLayout.SetMaximumSize)
              
        donji.addWidget(tab)       
        
        
        
        srednjiwidget.setAutoFillBackground(True)
        p = srednjiwidget.palette()
        p.setColor(srednjiwidget.backgroundRole(), Qt.cyan)
        srednjiwidget.setPalette(p)
        
        layout = QVBoxLayout()
        layout.addLayout(gornji)
        layout.addWidget(srednjiwidget)
        layout.addLayout(donji)
        #layout.addStretch()
        
        self.window.setLayout(layout)
        self.setCentralWidget(self.window);
        
    def initUI(self):
        self.setWindowIcon(QIcon('../images/Pill.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Bonadea')
        self.show()
            
   
