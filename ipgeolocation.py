from colorama import Fore, Back, Style
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys, json, urllib, urllib.request
import scapy.all as scapy

################################################
#
# IP Geolocation
#
# Authors - Sir809, c0deninja
#
#################################################

def geolocation(ip):
        try:
                print('\n')
                url = ("https://ipinfo.io/{}/json".format(gui.lineEdit.text()))
                v =  urllib.request.urlopen(url)
                j = json.loads(v.read())
                for dato in j:
                        gui.textEdit.setText(gui.textEdit.toPlainText() + dato + ": " +j[dato] + "\n")
        except urllib.error.HTTPError:
                gui.textEdit.setText(gui.textEdit.toPlainText() + Fore.RED + "NOT FOUND!")        

def btnclick():
        completed = 0
        while completed < 100:
            completed += 0.0001
            gui.progress.setValue(completed)
        geolocation(gui.lineEdit.text())

def btnclear():
        gui.textEdit.setText(gui.textEdit.setPlainText(''))

QtWidgets.QAction.triggered.connect(version())

def version():
    QtWidgets.QMessageBox.information(gui, 'Version', 'Netdiscovery by c0deninja', QtWidgets.QMessageBox.Ok)


app = QtWidgets.QApplication(sys.argv)
gui = uic.loadUi("netdiscovery.ui")

gui.setFixedSize(252, 325)

icon = QtGui.QIcon("icon.png")
gui.scan_btn.setIcon(icon)

icon2 = QtGui.QIcon('clear.png')
gui.clear_btn.setIcon(icon2)

gui.show()
sys.exit(app.exec_())
