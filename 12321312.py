import  sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout)
#QMessageBox : 메시지 박스 위젯
from PyQt5.QtGui import QIcon
#icon을 추가히기 위한 라이브러리

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message',self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage)
        #버튼 클릭시 핸들러 함수 연결


        self.btn2 = QPushButton('clear',self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout()    #수직 레이아웃 위젯 생성
        hbox.addStretch(1)  #빈 공간
        hbox.addWidget(self.btn1) #버튼 위젯
        hbox.addWidget(self.btn2) #빈 공간

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('calculator')
        self.setWindowIcon(QIcon('icon.png'))#window icon 추가
        self.resize(256,256)
        self.show()


    def activateMessage(self):
        #버튼을 클릭할때 동작하는 함수 : 메시지 박스 출력
        #QMessagebox.information(self, "information","Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
