'''
Created on Nov 5, 2015

@author: nikola
'''


import sys
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from recepcija import recepcijaGlavniProzor
from ordinacija.ordinacijaProzor import ordinacijaProzor
from database import dbhelpers
        

class LoginDialog(QDialog):
    
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.login = False   
        self.ime = ""
        self.password = ""
        self.tip = -1
        self.combo = QComboBox()
        self.combo.setEditable(True)
        self.dugme = QPushButton("Prijavi se", self)
        self.dugme.clicked.connect(self.loginclick)  
        self.editor = QLineEdit()
        self.editor.setEchoMode(QLineEdit.Password)
        data=[]
        baza = dbhelpers.db()
        if(baza.open()):
            data = baza.osobljeList()
        baza.close()    
        model = QStringListModel(data, self.combo)
        self.combo.setModel(model)
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.editor)
        layout.addWidget(self.dugme)
        self.setLayout(layout)
        #self.setGeometry(50, 50, 900, 720)
        self.setWindowTitle('Bonadea - Login')
                
    def loginclick(self):
        self.ime = str(self.combo.currentText())
        self.password = str(self.editor.text())
        if (self.ime == "" or self.password==""):
            self.login = False
        else:    
            baza = dbhelpers.db()
            if(baza.open()):
                rez = baza.login(self.ime,self.password)
                baza.close()  
                if(rez == -1):
                    self.login = False
                else:    
                    self.tip = rez    
                    self.login = True
            else:
                #ispisati obavestenje da ne moze da se konektuje na bazu
                self.login = False
        self.close()
            
def main():
    
    app = QApplication(sys.argv)
    ex = LoginDialog()
    ex.exec()
    if (ex.login == True):
        if (ex.tip == 2):
            ex = ordinacijaProzor(True,ex.ime)
            sys.exit(app.exec_())
        else:
            ex = recepcijaGlavniProzor.recepcijaProzor(True,ex.ime)
            sys.exit(app.exec_())    
       
    else:   
        print("pristup odbijen")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    