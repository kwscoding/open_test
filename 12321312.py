#애플리케이션에 필요한 라이브러리 추가
import  sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout)
#QMessageBox : 메시지 박스 위젯
from PyQt5.QtGui import QIcon
#icon을 추가히기 위한 라이브러리

class Calculator(QWidget):

    def __init__(self):
        super().__init__() #부모클래스 QWidget을 초기화
        self.initUI() #나머지 초기화는 initUI함수에 정의


    def initUI(self): #UI를 초기화하는 함수
        self.te1 = QPlainTextEdit() #읽기 전용 텍스트 입력 창 생성
        self.te1.setReadOnly(True) #텍스트 입력 창을 읽기 전용으로 설정

        self.btn1 = QPushButton('Message',self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage)
        #버튼 클릭시 핸들러 함수(activateMessage) 연결


        self.btn2 = QPushButton('clear',self)
        self.btn2.clicked.connect(self.clearMessage)

        #버튼들을 수평으로 배치할 수 있는 레이아웃 생성
        hbox = QHBoxLayout()
        hbox.addStretch(1)  #레이아웃에 여백추가
        hbox.addWidget(self.btn1) #"MESSAGE"버튼을 수평레이아웃에 추가
        hbox.addWidget(self.btn2) #"CLEAR"버튼을 수평 레이아웃에 추가

        #수직 레이아웃을 생성하고, 텍스트 입력 창과 버튼 레이아웃을 추가
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
