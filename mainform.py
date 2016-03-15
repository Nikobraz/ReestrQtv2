#!-*-coding:utf-8-*-
import sys
import init
import os
# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

(Ui_MainWindow, QMainWindow) = uic.loadUiType('mainform.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.changedpage()

    def __del__(self):
        self.ui = None

    def dclickedfilelist(self, item):
        print item.toolTip()

    def changedpage(self):
        self.ui.plainTextEdit.clear()
        summW = self.ui.summWidget
        summW.clear()
        cal = self.ui.calendarWidget
        date = cal.selectedDate()
        formatd = QTextCharFormat()
        formatd.setFontWeight(QFont.Bold)
        for x in xrange(1, cal.selectedDate().daysInMonth()+1):
            if not init.get_filelist(str(date.month()), str(x), str(date.year()), str(self.ui.comboBox.currentIndex())) == []:
                cal.setDateTextFormat(QDate(date.year(), date.month(), x), formatd)
        [summW.addItem(str(init.get_summ(str(date.month()), str(date.day()), str(date.year()), str(i)))) for i in xrange(0, 4)]
        summW.addItem(str(sum([(init.get_summ(str(date.month()), str(date.day()), str(date.year()), str(i))) for i in xrange(0, 4)])))

    def searchslot(self):
        self.ui.plainTextEdit.clear()
        self.ui.listWidget.clear()
        cal = self.ui.calendarWidget
        date = cal.selectedDate()
        search_str = str(QString.toUtf8(self.ui.lineEdit.displayText()))
        text = init.search_csv(
                init.get_filelist(
                    str(date.month()), str(date.day()), str(date.year()), str(self.ui.comboBox.currentIndex())),
                search_str)

        files = init.get_filelist(
                    str(date.month()), str(date.day()), str(date.year()), str(self.ui.comboBox.currentIndex()))
        for row in text:
            self.ui.plainTextEdit.appendPlainText(row)

        for i in files:
            f = open(i, 'r').readlines()[1]
            f = unicode(f, 'cp866')
            f = f.lstrip('# ').split(' ')[0]
            self.ui.listWidget.setToolTip(i)
            self.ui.listWidget.addItem(os.path.basename(i) + '    ' + f)


if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('ReestrQt')

    # create widget
    w = MainWindow()
    w.setWindowTitle('ReestrQt')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())
