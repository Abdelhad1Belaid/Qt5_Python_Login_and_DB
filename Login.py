from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sys


class Ui_Form(object):
    def __init__(self):
        self.open_DB()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(623, 466)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 590, 420))
        self.widget.setStyleSheet("#login_btn {\n"
                                  "background-color:rgba(85, 98, 112, 255);\n"
                                  "color:rgba(255, 255, 255, 200);\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "#login_btn:pressed {\n"
                                  "padding-left:5px;\n"
                                  "padding-top:5px;\n"
                                  "background-color:rgba(255, 107, 107, 255);\n"
                                  "background-position:calc(100%-10px)center;\n"
                                  "}\n"
                                  "\n"
                                  "#login_btn:hover {\n"
                                  "background-color:rgba(255, 107, 107, 255);\n"
                                  "}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.label.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                 "border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.label_2.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112 , 255), "
            "stop:1 rgba(255, 107, 207, 255));\n "
            "border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(290, 65, 260, 50))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0, 0, 200);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(340, 140, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border: 2px solid rgba(0, 0, 0, 0 );\n"
                                    "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                    "color:rgb(0, 0, 0);\n"
                                    "padding-bottom: 7px;")
        self.username.setPlaceholderText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(340, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border: 2px solid rgba(0, 0, 0, 0 );\n"
                                    "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                    "color:rgb(0, 0, 0);\n"
                                    "padding-bottom: 7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setGeometry(QtCore.QRect(340, 270, 190, 40))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 270, 51))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(45, 120, 260, 51))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(313, 140, 31, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(46, 82, 101, 200);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(313, 200, 31, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(46, 82, 101, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(36, 203, 281, 211))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(210)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 107, 107, 255);;\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.close = QtWidgets.QPushButton(self.widget)
        self.close.setGeometry(QtCore.QRect(40, 25, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(17)
        self.close.setFont(font)
        self.close.setStyleSheet("background-color:rgb(93, 98, 116);\n"
                                 "border:0px;\n"
                                 "border-radius:15px;")
        self.close.setObjectName("close")

        self.retranslateUi(Form)
        self.close.pressed.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # connecting login button
        self.login_btn.clicked.connect(self.check_Credentials)

    def open_DB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database.sqlite")
        if not self.db.open():
            print("Error !! DB not open")
        self.query = QtSql.QSqlQuery()

    def check_Credentials(self):
        User = self.username.text()
        Pwd = self.password.text()
        print("Username => {}\nPassword => {}".format(User, Pwd))
        self.db.open()
        self.query.exec_("SELECT * FROM userdata WHERE username == '{}' AND password == '{}';".format(User, Pwd))
        self.query.first()
        if self.query.value("username") != None and self.query.value("password") != None:
            print("Welcome")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Login"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "Mountains"))
        self.label_5.setText(_translate("Form", "Live the Adventure "))
        self.label_6.setText(_translate("Form", ""))
        self.label_7.setText(_translate("Form", ""))
        self.label_8.setText(_translate("Form", ""))
        self.close.setText(_translate("Form", ""))
