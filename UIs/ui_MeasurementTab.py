# Form implementation generated from reading ui file 'c:\Users\xstejs30\Documents\PythonProjects\PyWinApp\main\DP\UIs\MeasurementTab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MeasurementTab(object):
    def setupUi(self, MeasurementTab):
        MeasurementTab.setObjectName("MeasurementTab")
        MeasurementTab.resize(534, 323)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MeasurementTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelGroupTitle = QtWidgets.QLabel(parent=MeasurementTab)
        self.labelGroupTitle.setObjectName("labelGroupTitle")
        self.verticalLayout.addWidget(self.labelGroupTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setContentsMargins(-1, -1, 80, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4v = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_4v.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4v.setFont(font)
        self.lineEdit_4v.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_4v.setReadOnly(True)
        self.lineEdit_4v.setObjectName("lineEdit_4v")
        self.gridLayout.addWidget(self.lineEdit_4v, 2, 1, 1, 1)
        self.lineEdit_3v3 = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_3v3.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3v3.setFont(font)
        self.lineEdit_3v3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_3v3.setReadOnly(True)
        self.lineEdit_3v3.setObjectName("lineEdit_3v3")
        self.gridLayout.addWidget(self.lineEdit_3v3, 3, 1, 1, 1)
        self.btn_3v3 = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_3v3.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_3v3.setText("")
        self.btn_3v3.setCheckable(True)
        self.btn_3v3.setChecked(False)
        self.btn_3v3.setObjectName("btn_3v3")
        self.gridLayout.addWidget(self.btn_3v3, 3, 2, 1, 1)
        self.label_5v = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_5v.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_5v.setObjectName("label_5v")
        self.gridLayout.addWidget(self.label_5v, 1, 0, 1, 1)
        self.btn_vdd = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_vdd.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_vdd.setText("")
        self.btn_vdd.setCheckable(True)
        self.btn_vdd.setChecked(True)
        self.btn_vdd.setObjectName("btn_vdd")
        self.gridLayout.addWidget(self.btn_vdd, 0, 2, 1, 1)
        self.lineEdit_vdd = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_vdd.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_vdd.setFont(font)
        self.lineEdit_vdd.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_vdd.setReadOnly(True)
        self.lineEdit_vdd.setObjectName("lineEdit_vdd")
        self.gridLayout.addWidget(self.lineEdit_vdd, 0, 1, 1, 1)
        self.lineEdit_5v = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_5v.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5v.setFont(font)
        self.lineEdit_5v.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_5v.setReadOnly(True)
        self.lineEdit_5v.setObjectName("lineEdit_5v")
        self.gridLayout.addWidget(self.lineEdit_5v, 1, 1, 1, 1)
        self.label_4v = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_4v.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4v.setObjectName("label_4v")
        self.gridLayout.addWidget(self.label_4v, 2, 0, 1, 1)
        self.btn_5v = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_5v.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_5v.setText("")
        self.btn_5v.setCheckable(True)
        self.btn_5v.setChecked(False)
        self.btn_5v.setObjectName("btn_5v")
        self.gridLayout.addWidget(self.btn_5v, 1, 2, 1, 1)
        self.btn_4v = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_4v.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_4v.setText("")
        self.btn_4v.setCheckable(True)
        self.btn_4v.setChecked(False)
        self.btn_4v.setObjectName("btn_4v")
        self.gridLayout.addWidget(self.btn_4v, 2, 2, 1, 1)
        self.label_3v3 = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_3v3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3v3.setObjectName("label_3v3")
        self.gridLayout.addWidget(self.label_3v3, 3, 0, 1, 1)
        self.label_vdd = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_vdd.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_vdd.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_vdd.setObjectName("label_vdd")
        self.gridLayout.addWidget(self.label_vdd, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_2.setContentsMargins(0, -1, 80, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_air = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_air.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_air.setFont(font)
        self.lineEdit_air.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_air.setReadOnly(True)
        self.lineEdit_air.setObjectName("lineEdit_air")
        self.gridLayout_2.addWidget(self.lineEdit_air, 1, 1, 1, 1)
        self.label_vcc = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_vcc.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_vcc.setObjectName("label_vcc")
        self.gridLayout_2.addWidget(self.label_vcc, 0, 0, 1, 1)
        self.lineEdit_do0 = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_do0.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_do0.setFont(font)
        self.lineEdit_do0.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_do0.setReadOnly(True)
        self.lineEdit_do0.setObjectName("lineEdit_do0")
        self.gridLayout_2.addWidget(self.lineEdit_do0, 3, 1, 1, 1)
        self.label_air = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_air.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_air.setObjectName("label_air")
        self.gridLayout_2.addWidget(self.label_air, 1, 0, 1, 1)
        self.btn_vcc = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_vcc.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_vcc.setText("")
        self.btn_vcc.setCheckable(True)
        self.btn_vcc.setChecked(False)
        self.btn_vcc.setObjectName("btn_vcc")
        self.gridLayout_2.addWidget(self.btn_vcc, 0, 2, 1, 1)
        self.lineEdit_do1 = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_do1.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_do1.setFont(font)
        self.lineEdit_do1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_do1.setReadOnly(True)
        self.lineEdit_do1.setObjectName("lineEdit_do1")
        self.gridLayout_2.addWidget(self.lineEdit_do1, 2, 1, 1, 1)
        self.btn_do0 = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_do0.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_do0.setText("")
        self.btn_do0.setCheckable(True)
        self.btn_do0.setChecked(False)
        self.btn_do0.setObjectName("btn_do0")
        self.gridLayout_2.addWidget(self.btn_do0, 3, 2, 1, 1)
        self.btn_do1 = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_do1.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_do1.setText("")
        self.btn_do1.setCheckable(True)
        self.btn_do1.setChecked(False)
        self.btn_do1.setObjectName("btn_do1")
        self.gridLayout_2.addWidget(self.btn_do1, 2, 2, 1, 1)
        self.lineEdit_vcc = QtWidgets.QLineEdit(parent=MeasurementTab)
        self.lineEdit_vcc.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_vcc.setFont(font)
        self.lineEdit_vcc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_vcc.setReadOnly(True)
        self.lineEdit_vcc.setObjectName("lineEdit_vcc")
        self.gridLayout_2.addWidget(self.lineEdit_vcc, 0, 1, 1, 1)
        self.btn_air = QtWidgets.QPushButton(parent=MeasurementTab)
        self.btn_air.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_air.setText("")
        self.btn_air.setCheckable(True)
        self.btn_air.setChecked(False)
        self.btn_air.setObjectName("btn_air")
        self.gridLayout_2.addWidget(self.btn_air, 1, 2, 1, 1)
        self.label_do0 = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_do0.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_do0.setObjectName("label_do0")
        self.gridLayout_2.addWidget(self.label_do0, 3, 0, 1, 1)
        self.label_do1 = QtWidgets.QLabel(parent=MeasurementTab)
        self.label_do1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_do1.setObjectName("label_do1")
        self.gridLayout_2.addWidget(self.label_do1, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.graphWidget = PlotWidget(parent=MeasurementTab)
        self.graphWidget.setObjectName("graphWidget")
        self.verticalLayout_2.addWidget(self.graphWidget)

        self.retranslateUi(MeasurementTab)
        QtCore.QMetaObject.connectSlotsByName(MeasurementTab)

    def retranslateUi(self, MeasurementTab):
        _translate = QtCore.QCoreApplication.translate
        MeasurementTab.setWindowTitle(_translate("MeasurementTab", "Form"))
        self.labelGroupTitle.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Měření napětí:</span></p></body></html>"))
        self.lineEdit_4v.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_4v.setText(_translate("MeasurementTab", " V"))
        self.lineEdit_3v3.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_3v3.setText(_translate("MeasurementTab", " V"))
        self.label_5v.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">5 V:</span></p></body></html>"))
        self.lineEdit_vdd.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_vdd.setText(_translate("MeasurementTab", " V"))
        self.lineEdit_5v.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_5v.setText(_translate("MeasurementTab", " V"))
        self.label_4v.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">4 V:</span></p></body></html>"))
        self.label_3v3.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">3,3 V:</span></p></body></html>"))
        self.label_vdd.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">VDD:</span></p></body></html>"))
        self.lineEdit_air.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_air.setText(_translate("MeasurementTab", " V"))
        self.label_vcc.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">VCC:</span></p></body></html>"))
        self.lineEdit_do0.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_do0.setText(_translate("MeasurementTab", " V"))
        self.label_air.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Air:</span></p></body></html>"))
        self.lineEdit_do1.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_do1.setText(_translate("MeasurementTab", " V"))
        self.lineEdit_vcc.setInputMask(_translate("MeasurementTab", "00 V"))
        self.lineEdit_vcc.setText(_translate("MeasurementTab", " V"))
        self.label_do0.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">DO0:</span></p></body></html>"))
        self.label_do1.setText(_translate("MeasurementTab", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">DO1:</span></p></body></html>"))
from pyqtgraph import PlotWidget
