# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1133, 810)
        self.lblName = QtWidgets.QLabel(main)
        self.lblName.setEnabled(True)
        self.lblName.setGeometry(QtCore.QRect(390, 10, 381, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblName.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblName.setFont(font)
        self.lblName.setAutoFillBackground(False)
        self.lblName.setFrameShape(QtWidgets.QFrame.Box)
        self.lblName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblName.setLineWidth(3)
        self.lblName.setMidLineWidth(0)
        self.lblName.setTextFormat(QtCore.Qt.AutoText)
        self.lblName.setScaledContents(False)
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setWordWrap(False)
        self.lblName.setObjectName("lblName")
        self.question_label = QtWidgets.QLabel(main)
        self.question_label.setGeometry(QtCore.QRect(970, 60, 151, 91))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.question_label.setFont(font)
        self.question_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_label.setAutoFillBackground(False)
        self.question_label.setObjectName("question_label")
        self.question_1 = QtWidgets.QLabel(main)
        self.question_1.setGeometry(QtCore.QRect(140, 140, 951, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.question_1.setFont(font)
        self.question_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_1.setAutoFillBackground(False)
        self.question_1.setObjectName("question_1")
        self.question_2 = QtWidgets.QLabel(main)
        self.question_2.setGeometry(QtCore.QRect(570, 220, 481, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_2.setFont(font)
        self.question_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_2.setAutoFillBackground(False)
        self.question_2.setObjectName("question_2")
        self.question_3 = QtWidgets.QLabel(main)
        self.question_3.setGeometry(QtCore.QRect(360, 220, 151, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_3.setFont(font)
        self.question_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_3.setAutoFillBackground(False)
        self.question_3.setObjectName("question_3")
        self.question_4 = QtWidgets.QLabel(main)
        self.question_4.setGeometry(QtCore.QRect(120, 220, 171, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_4.setFont(font)
        self.question_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_4.setAutoFillBackground(False)
        self.question_4.setObjectName("question_4")
        self.question_5 = QtWidgets.QLabel(main)
        self.question_5.setGeometry(QtCore.QRect(900, 270, 151, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_5.setFont(font)
        self.question_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_5.setAutoFillBackground(False)
        self.question_5.setObjectName("question_5")
        self.question_6 = QtWidgets.QLabel(main)
        self.question_6.setGeometry(QtCore.QRect(760, 270, 71, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_6.setFont(font)
        self.question_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_6.setAutoFillBackground(False)
        self.question_6.setObjectName("question_6")
        self.question_7 = QtWidgets.QLabel(main)
        self.question_7.setGeometry(QtCore.QRect(590, 350, 461, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_7.setFont(font)
        self.question_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_7.setAutoFillBackground(False)
        self.question_7.setObjectName("question_7")
        self.question_8 = QtWidgets.QLabel(main)
        self.question_8.setGeometry(QtCore.QRect(360, 350, 151, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_8.setFont(font)
        self.question_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_8.setAutoFillBackground(False)
        self.question_8.setObjectName("question_8")
        self.question_9 = QtWidgets.QLabel(main)
        self.question_9.setGeometry(QtCore.QRect(30, 350, 251, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_9.setFont(font)
        self.question_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_9.setAutoFillBackground(False)
        self.question_9.setObjectName("question_9")
        self.question_10 = QtWidgets.QLabel(main)
        self.question_10.setGeometry(QtCore.QRect(840, 400, 151, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_10.setFont(font)
        self.question_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_10.setAutoFillBackground(False)
        self.question_10.setObjectName("question_10")
        self.question_11 = QtWidgets.QLabel(main)
        self.question_11.setGeometry(QtCore.QRect(700, 400, 71, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_11.setFont(font)
        self.question_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_11.setAutoFillBackground(False)
        self.question_11.setObjectName("question_11")
        self.line = QtWidgets.QFrame(main)
        self.line.setGeometry(QtCore.QRect(10, 480, 1111, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.answer_1 = QtWidgets.QLabel(main)
        self.answer_1.setGeometry(QtCore.QRect(1000, 490, 121, 71))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.answer_1.setFont(font)
        self.answer_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.answer_1.setAutoFillBackground(False)
        self.answer_1.setObjectName("answer_1")
        self.answer_2 = QtWidgets.QLabel(main)
        self.answer_2.setGeometry(QtCore.QRect(10, 520, 51, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.answer_2.setFont(font)
        self.answer_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.answer_2.setAutoFillBackground(False)
        self.answer_2.setObjectName("answer_2")
        self.answer_3 = QtWidgets.QLabel(main)
        self.answer_3.setGeometry(QtCore.QRect(80, 500, 31, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.answer_3.setFont(font)
        self.answer_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.answer_3.setAutoFillBackground(False)
        self.answer_3.setObjectName("answer_3")
        self.line_2 = QtWidgets.QFrame(main)
        self.line_2.setGeometry(QtCore.QRect(70, 530, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line_2.setFont(font)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.answer_4 = QtWidgets.QLabel(main)
        self.answer_4.setGeometry(QtCore.QRect(80, 550, 31, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.answer_4.setFont(font)
        self.answer_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.answer_4.setAutoFillBackground(False)
        self.answer_4.setObjectName("answer_4")
        self.question_12 = QtWidgets.QLabel(main)
        self.question_12.setGeometry(QtCore.QRect(750, 570, 341, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_12.setFont(font)
        self.question_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_12.setAutoFillBackground(False)
        self.question_12.setObjectName("question_12")
        self.question_13 = QtWidgets.QLabel(main)
        self.question_13.setGeometry(QtCore.QRect(750, 680, 341, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_13.setFont(font)
        self.question_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_13.setAutoFillBackground(False)
        self.question_13.setObjectName("question_13")
        self.question_14 = QtWidgets.QLabel(main)
        self.question_14.setGeometry(QtCore.QRect(300, 570, 91, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.question_14.setFont(font)
        self.question_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_14.setAutoFillBackground(False)
        self.question_14.setObjectName("question_14")
        self.question_15 = QtWidgets.QLabel(main)
        self.question_15.setGeometry(QtCore.QRect(300, 680, 91, 61))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.question_15.setFont(font)
        self.question_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_15.setAutoFillBackground(False)
        self.question_15.setObjectName("question_15")
        self.calculate = QtWidgets.QPushButton(main)
        self.calculate.setGeometry(QtCore.QRect(50, 440, 171, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculate.setFont(font)
        self.calculate.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.calculate.setObjectName("calculate")
        self.distance_1 = QtWidgets.QTextEdit(main)
        self.distance_1.setGeometry(QtCore.QRect(520, 230, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.distance_1.setFont(font)
        self.distance_1.setObjectName("distance_1")
        self.velocity_1 = QtWidgets.QTextEdit(main)
        self.velocity_1.setGeometry(QtCore.QRect(300, 230, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.velocity_1.setFont(font)
        self.velocity_1.setObjectName("velocity_1")
        self.distance_2 = QtWidgets.QTextEdit(main)
        self.distance_2.setGeometry(QtCore.QRect(60, 230, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.distance_2.setFont(font)
        self.distance_2.setObjectName("distance_2")
        self.velocity_2 = QtWidgets.QTextEdit(main)
        self.velocity_2.setGeometry(QtCore.QRect(840, 280, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.velocity_2.setFont(font)
        self.velocity_2.setObjectName("velocity_2")
        self.time_1 = QtWidgets.QTextEdit(main)
        self.time_1.setGeometry(QtCore.QRect(530, 360, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.time_1.setFont(font)
        self.time_1.setObjectName("time_1")
        self.velocity_3 = QtWidgets.QTextEdit(main)
        self.velocity_3.setGeometry(QtCore.QRect(300, 360, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.velocity_3.setFont(font)
        self.velocity_3.setObjectName("velocity_3")
        self.time_2 = QtWidgets.QTextEdit(main)
        self.time_2.setGeometry(QtCore.QRect(1000, 410, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.time_2.setFont(font)
        self.time_2.setObjectName("time_2")
        self.velocity_4 = QtWidgets.QTextEdit(main)
        self.velocity_4.setGeometry(QtCore.QRect(780, 410, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.velocity_4.setFont(font)
        self.velocity_4.setObjectName("velocity_4")
        self.answer_a = QtWidgets.QTextEdit(main)
        self.answer_a.setGeometry(QtCore.QRect(400, 580, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.answer_a.setFont(font)
        self.answer_a.setObjectName("answer_a")
        self.answer_b = QtWidgets.QTextEdit(main)
        self.answer_b.setGeometry(QtCore.QRect(400, 690, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.answer_b.setFont(font)
        self.answer_b.setObjectName("answer_b")

        self.retranslateUi(main)
        self.calculate.clicked.connect(self.solve) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(main)

    def solve(self):

        ## first question
        q1_distance_1 = float(self.distance_1.toPlainText())
        q1_velocity_1 = float(self.velocity_1.toPlainText())
        q1_distance_2 = float(self.distance_2.toPlainText())
        q1_velocity_2 = float(self.velocity_2.toPlainText())

        q1_distance = q1_distance_1 + q1_distance_2
        q1_time = (q1_distance_1 / q1_velocity_1) + (q1_distance_2 / q1_velocity_2)

        q1_velocity = q1_distance / q1_time

        self.answer_a.setPlainText(str(q1_velocity))

        ## second question
        q2_time_1 = float(self.time_1.toPlainText()) * 60
        q2_velocity_1 = float(self.velocity_3.toPlainText())
        q2_time_2 = float(self.time_2.toPlainText()) * 60
        q2_velocity_2 = float(self.velocity_4.toPlainText())

        q2_distance = (q2_time_1 * q2_velocity_1) + (q2_time_2 * q2_velocity_2)
        q2_time = q2_time_1 + q2_time_2

        q2_velocity = q2_distance / q2_time
        
        self.answer_b.setPlainText(str(q2_velocity))


    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.lblName.setText(_translate("main", "physic solver"))
        self.question_label.setText(_translate("main", "مثال :"))
        self.question_1.setText(_translate("main", "سرعت متوسط خود را در دو حالت زیر با هم مقایسه کنید."))
        self.question_2.setText(_translate("main", "الف ) در امتداد یک مسیر مستقیم، ابتدا مسافت"))
        self.question_3.setText(_translate("main", "متر را با سرعت"))
        self.question_4.setText(_translate("main", "راه بروید و سپس"))
        self.question_5.setText(_translate("main", "متر را با سرعت"))
        self.question_6.setText(_translate("main", " بدوید."))
        self.question_7.setText(_translate("main", "ب ) در امتداد یک مسیر مستقیم ابتدا به مدت"))
        self.question_8.setText(_translate("main", "دقیقه با سرعت"))
        self.question_9.setText(_translate("main", "راه بروید و سپس به مدت"))
        self.question_10.setText(_translate("main", "دقیقه با سرعت"))
        self.question_11.setText(_translate("main", " بدوید."))
        self.answer_1.setText(_translate("main", "پاسخ :"))
        self.answer_2.setText(_translate("main", "V ="))
        self.answer_3.setText(_translate("main", "x"))
        self.answer_4.setText(_translate("main", "t"))
        self.question_12.setText(_translate("main", " سرعت متوسط در قسمت (الف) : "))
        self.question_13.setText(_translate("main", " سرعت متوسط در قسمت (ب) : "))
        self.question_14.setText(_translate("main", " متر بر ثانیه"))
        self.question_15.setText(_translate("main", " متر بر ثانیه"))
        self.calculate.setText(_translate("main", "محاسبه"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
