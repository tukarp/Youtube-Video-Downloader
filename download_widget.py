from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from download_popup import DownloadCompletedPopup

class DownloadStatusWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(20, 250, 400, 30)
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setText("Ready to download")

    def show_message(self, message):
        self.setText(message)
        
    def show_popup(self):
        popup = DownloadCompletedPopup(self)
        popup.exec_()
        
