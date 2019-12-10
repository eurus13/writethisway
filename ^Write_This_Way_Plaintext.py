from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QPushButton


class PlainTextEdit(QtWidgets.QPlainTextEdit):
    def keyPressEvent(self, event):
        
        
        if event.key() == QtCore.Qt.Key_Backspace:
           
           
           self.Play()
           #find a way that doesn't involve an erro
           
           self.insertPlainText( '  __[xXx_OOPSIE NoNo!_xXx]__    ' )
        super(PlainTextEdit, self).keyPressEvent(event)
           
           
            
        if event.key() == QtCore.Qt.Key_Left:
           self.Play()
           self.insertPlainText( '  __[xXx_OOPSIE NoNo!_xXx]__   ' )
        super(PlainTextEdit, self).keyPressEvent(event)

    def mousePressEvent(self, event):

        self.Play()
        self.insertPlainText( '  __[xXx_OOPSIE NoNo!_xXx]__    ' )

    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")

    def Play(self):
       
        QSound.play("bike_horn.wav")

   
     
# def eventFilter(self, obj, event):
#         if obj in self.m_widgets and event.type() == QtCore.QEvent.KeyPress:
#             if event.key() == QtCore.Qt.Key_Backspace:
#                 # create new event
#                 new_event = QtGui.QKeyEvent(self.Play())
#                 # new_event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress, 
#                 #     QtCore.Qt.Key_Down, 
#                 #     QtCore.Qt.NoModifier)
#                 # send new event
#                 QtCore.QCoreApplication.postEvent(obj, new_event)
#                 # if True, the event is discarded
#                 return True
#         return super(PlainTextEdit, self).eventFilter(obj, event)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = PlainTextEdit()
    w.show()
   
    sys.exit(app.exec_())

    # https://stackoverflow.com/questions/54846450/transparently-get-backspace-event-in-pyqt

    # https://stackoverflow.com/questions/48668670/replacing-qkeyevents-in-qapp-eventfilter


    