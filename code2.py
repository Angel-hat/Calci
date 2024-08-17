# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calci.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_Dialog(object):
    exp=""
    pp=''
    new=""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 398)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 70, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 150, 41, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 150, 41, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 150, 41, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 110, 41, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 110, 41, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 110, 41, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 110, 41, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 70, 41, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 70, 41, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 70, 41, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(190, 150, 41, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(190, 190, 41, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(140, 190, 41, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(90, 190, 41, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(40, 190, 41, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 19, 191, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "9"))
        self.pushButton_3.setText(_translate("Dialog", "8"))
        self.pushButton_4.setText(_translate("Dialog", "7"))
        self.pushButton_5.setText(_translate("Dialog", "4"))
        self.pushButton_6.setText(_translate("Dialog", "5 "))
        self.pushButton_7.setText(_translate("Dialog", "6"))
        self.pushButton_8.setText(_translate("Dialog", "+"))
        self.pushButton_9.setText(_translate("Dialog", "/"))
        self.pushButton_10.setText(_translate("Dialog", "3"))
        self.pushButton_11.setText(_translate("Dialog", "2"))
        self.pushButton_12.setText(_translate("Dialog", "-"))
        self.pushButton_14.setText(_translate("Dialog", "*"))
        self.pushButton_15.setText(_translate("Dialog", "="))
        self.pushButton_16.setText(_translate("Dialog", "0"))
        self.pushButton_17.setText(_translate("Dialog", "c"))
        self.init()
    def init(self):
        btn=[self.pushButton,self.pushButton_11,self.pushButton_10,
              self.pushButton_5,self.pushButton_6,self.pushButton_7,
              self.pushButton_4,self.pushButton_3,self.pushButton_2,
              self.pushButton_16,self.pushButton_9,self.pushButton_8,
              self.pushButton_12,self.pushButton_14,self.pushButton_15
              ]
        values=[1,2,3,4,5,6,7,8,9,0,'/','+','-','*','=']
        btns=list(zip(btn,values))
        self.sign="=-/*+"
        self.pushButton_17.clicked.connect(partial(self.add,"abc"))
        
        for i in btns:
           i[0].clicked.connect(partial(self.add,i[1]))
                
            

    def add(self,x):
        if self.exp=="0" or self.exp=="/" or self.exp=="*":
            self.exp=""
        self.exp+=str(x)
        if self.exp=="=":
            self.exp="0"
        if len(self.exp)>=2:
            if self.exp[-1] in self.sign and self.exp[-2] in self.sign :
                self.exp=self.exp[:-2]+str(x)


        self.lineEdit.setText(self.exp)
        if x=="=":
            #if len(self.exp)>=2 and self.exp[:-1].isalnum() :
                #self.exp=self.exp[:-1]
            if self.exp!="0" :
                self.ss=eval(self.exp[:-1])
                self.clear()
                self.lineEdit.setText(str(self.ss))
                self.new=self.ss
        elif x=="abc":
            self.clear()

    def clear(self):
        self.exp=self.pp
        self.lineEdit.setText(self.pp)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())