# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets,uic
import sys


class Calculadora(QtWidgets.QDialog):
    def __init__(self):
        super(Calculadora,self).__init__()
        uic.loadUi("Calculadora.ui",self)
        self.Numbers=self.findChild(QtWidgets.QButtonGroup,"Numbers")
        self.Numbers.buttonClicked.connect(self.SetText)
        self.Operations=self.findChild(QtWidgets.QButtonGroup,"Operations")
        self.Operations.buttonClicked.connect(self.SetText)
        self.Resultado=self.findChild(QtWidgets.QLineEdit,"Resultado")
        self.Equal=self.findChild(QtWidgets.QPushButton,"Equal")
        self.Equal.clicked.connect(self.calculateResult)
        self.Clear=self.findChild(QtWidgets.QPushButton,"Clear")
        self.Clear.clicked.connect(self.ClearText)
        self.show()
        
    def ClearText(self):
        self.Resultado.setText("")
        
    def SetText(self,button):
        if self.GetText()=="ERROR":
            self.ClearText()
        Text=self.Resultado.text()
        Text+=button.text()
        self.Resultado.setText(Text)
    
    def GetText(self):
        return self.Resultado.text()

    def calculateResult(self):
        resultado=self.evaluateExpression()
        self.Resultado.setText(resultado)
        
    def evaluateExpression(self):
        expression=self.GetText()
        try:
            result=str(eval(expression))
        except Exception:
            result="ERROR"
        return result
        
        

app=QtWidgets.QApplication(sys.argv)
window=Calculadora()
app.exec_()



        

