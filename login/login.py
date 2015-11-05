'''
Created on Nov 5, 2015

@author: nikola
'''


import sys
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from recepcija import recepcijaGlavniProzor
from database import dbhelpers
        

class LoginDialog(QDialog):
    
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.login = False   
        self.ime = ""
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
        self.login = True
        self.close()
            
def main():
    
    app = QApplication(sys.argv)
    ex = LoginDialog()
    ex.exec()
    if (ex.login == True):
        print("ulazi")
        ex = recepcijaGlavniProzor.recepcijaProzor(True,"ime")
        sys.exit(app.exec_())
    else:   
        pass 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    