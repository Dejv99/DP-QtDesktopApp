# Form implementation generated from reading ui file 'UIs/TerminalTab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TerminalTab(object):
    def setupUi(self, TerminalTab):
        TerminalTab.setObjectName("TerminalTab")
        TerminalTab.resize(350, 280)
        TerminalTab.setMaximumSize(QtCore.QSize(450, 450))
        self.verticalLayout = QtWidgets.QVBoxLayout(TerminalTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSerialCom = QtWidgets.QLabel(parent=TerminalTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.labelSerialCom.setFont(font)
        self.labelSerialCom.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.labelSerialCom.setObjectName("labelSerialCom")
        self.verticalLayout.addWidget(self.labelSerialCom)
        self.gLayoutComSelect = QtWidgets.QGridLayout()
        self.gLayoutComSelect.setContentsMargins(10, -1, -1, -1)
        self.gLayoutComSelect.setObjectName("gLayoutComSelect")
        self.comboBoxComSelect = QtWidgets.QComboBox(parent=TerminalTab)
        self.comboBoxComSelect.setMinimumSize(QtCore.QSize(70, 0))
        self.comboBoxComSelect.setEditable(True)
        self.comboBoxComSelect.setCurrentText("")
        self.comboBoxComSelect.setObjectName("comboBoxComSelect")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.comboBoxComSelect.addItem("")
        self.gLayoutComSelect.addWidget(self.comboBoxComSelect, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gLayoutComSelect.addItem(spacerItem, 0, 2, 1, 1)
        self.setSerialCom = QtWidgets.QLabel(parent=TerminalTab)
        self.setSerialCom.setObjectName("setSerialCom")
        self.gLayoutComSelect.addWidget(self.setSerialCom, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gLayoutComSelect)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.vLayoutConfiguration = QtWidgets.QVBoxLayout()
        self.vLayoutConfiguration.setContentsMargins(10, -1, -1, -1)
        self.vLayoutConfiguration.setObjectName("vLayoutConfiguration")
        self.labelSerialComConfig = QtWidgets.QLabel(parent=TerminalTab)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelSerialComConfig.setFont(font)
        self.labelSerialComConfig.setObjectName("labelSerialComConfig")
        self.vLayoutConfiguration.addWidget(self.labelSerialComConfig)
        self.gLayoutConfiguration = QtWidgets.QGridLayout()
        self.gLayoutConfiguration.setContentsMargins(10, -1, -1, -1)
        self.gLayoutConfiguration.setObjectName("gLayoutConfiguration")
        self.lineEditBaud = QtWidgets.QLineEdit(parent=TerminalTab)
        self.lineEditBaud.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditBaud.setMaximumSize(QtCore.QSize(150, 25))
        self.lineEditBaud.setMaxLength(8)
        self.lineEditBaud.setObjectName("lineEditBaud")
        self.gLayoutConfiguration.addWidget(self.lineEditBaud, 0, 1, 1, 1)
        self.labelFlowCtrl = QtWidgets.QLabel(parent=TerminalTab)
        self.labelFlowCtrl.setObjectName("labelFlowCtrl")
        self.gLayoutConfiguration.addWidget(self.labelFlowCtrl, 4, 0, 1, 1)
        self.labelParity = QtWidgets.QLabel(parent=TerminalTab)
        self.labelParity.setObjectName("labelParity")
        self.gLayoutConfiguration.addWidget(self.labelParity, 3, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(parent=TerminalTab)
        self.comboBox_3.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_3.setCurrentText("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gLayoutConfiguration.addWidget(self.comboBox_3, 4, 1, 1, 1)
        self.lineEdit_stopBitCount = QtWidgets.QLineEdit(parent=TerminalTab)
        self.lineEdit_stopBitCount.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_stopBitCount.setMaximumSize(QtCore.QSize(150, 25))
        self.lineEdit_stopBitCount.setMaxLength(2)
        self.lineEdit_stopBitCount.setObjectName("lineEdit_stopBitCount")
        self.gLayoutConfiguration.addWidget(self.lineEdit_stopBitCount, 2, 1, 1, 1)
        self.labelBaud = QtWidgets.QLabel(parent=TerminalTab)
        self.labelBaud.setObjectName("labelBaud")
        self.gLayoutConfiguration.addWidget(self.labelBaud, 0, 0, 1, 1)
        self.lineEditDataBitCount = QtWidgets.QLineEdit(parent=TerminalTab)
        self.lineEditDataBitCount.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditDataBitCount.setMaximumSize(QtCore.QSize(150, 25))
        self.lineEditDataBitCount.setText("")
        self.lineEditDataBitCount.setMaxLength(2)
        self.lineEditDataBitCount.setObjectName("lineEditDataBitCount")
        self.gLayoutConfiguration.addWidget(self.lineEditDataBitCount, 1, 1, 1, 1)
        self.labelDataBitCount = QtWidgets.QLabel(parent=TerminalTab)
        self.labelDataBitCount.setObjectName("labelDataBitCount")
        self.gLayoutConfiguration.addWidget(self.labelDataBitCount, 1, 0, 1, 1)
        self.labelStopBitCount = QtWidgets.QLabel(parent=TerminalTab)
        self.labelStopBitCount.setObjectName("labelStopBitCount")
        self.gLayoutConfiguration.addWidget(self.labelStopBitCount, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=TerminalTab)
        self.comboBox_2.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gLayoutConfiguration.addWidget(self.comboBox_2, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gLayoutConfiguration.addItem(spacerItem2, 0, 2, 1, 1)
        self.vLayoutConfiguration.addLayout(self.gLayoutConfiguration)
        self.verticalLayout.addLayout(self.vLayoutConfiguration)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.setSerialCom.setBuddy(self.comboBoxComSelect)
        self.labelFlowCtrl.setBuddy(self.comboBox_3)
        self.labelParity.setBuddy(self.comboBox_2)
        self.labelBaud.setBuddy(self.lineEditBaud)
        self.labelDataBitCount.setBuddy(self.lineEditDataBitCount)
        self.labelStopBitCount.setBuddy(self.lineEdit_stopBitCount)

        self.retranslateUi(TerminalTab)
        QtCore.QMetaObject.connectSlotsByName(TerminalTab)
        TerminalTab.setTabOrder(self.lineEditBaud, self.lineEditDataBitCount)
        TerminalTab.setTabOrder(self.lineEditDataBitCount, self.lineEdit_stopBitCount)
        TerminalTab.setTabOrder(self.lineEdit_stopBitCount, self.comboBox_2)
        TerminalTab.setTabOrder(self.comboBox_2, self.comboBox_3)

    def retranslateUi(self, TerminalTab):
        _translate = QtCore.QCoreApplication.translate
        TerminalTab.setWindowTitle(_translate("TerminalTab", "Form"))
        self.labelSerialCom.setText(_translate("TerminalTab", "Možnosti ovládání sériové kounikace přes RS-485"))
        self.comboBoxComSelect.setPlaceholderText(_translate("TerminalTab", "COM1"))
        self.comboBoxComSelect.setItemText(0, _translate("TerminalTab", "COM1"))
        self.comboBoxComSelect.setItemText(1, _translate("TerminalTab", "COM2"))
        self.comboBoxComSelect.setItemText(2, _translate("TerminalTab", "COM3"))
        self.comboBoxComSelect.setItemText(3, _translate("TerminalTab", "COM4"))
        self.comboBoxComSelect.setItemText(4, _translate("TerminalTab", "COM5"))
        self.comboBoxComSelect.setItemText(5, _translate("TerminalTab", "COM6"))
        self.comboBoxComSelect.setItemText(6, _translate("TerminalTab", "COM7"))
        self.comboBoxComSelect.setItemText(7, _translate("TerminalTab", "COM8"))
        self.comboBoxComSelect.setItemText(8, _translate("TerminalTab", "COM9"))
        self.setSerialCom.setText(_translate("TerminalTab", "Vyberte sériovou linku k připojení"))
        self.labelSerialComConfig.setText(_translate("TerminalTab", "Konfigurace sériové linky"))
        self.lineEditBaud.setPlaceholderText(_translate("TerminalTab", "9600"))
        self.labelFlowCtrl.setText(_translate("TerminalTab", "Řízení toku"))
        self.labelParity.setText(_translate("TerminalTab", "Parita"))
        self.comboBox_3.setPlaceholderText(_translate("TerminalTab", "Žádné"))
        self.comboBox_3.setItemText(0, _translate("TerminalTab", "Žádné"))
        self.comboBox_3.setItemText(1, _translate("TerminalTab", "XON/XOFF"))
        self.comboBox_3.setItemText(2, _translate("TerminalTab", "RTS/CTS"))
        self.comboBox_3.setItemText(3, _translate("TerminalTab", "DSR/DTR"))
        self.lineEdit_stopBitCount.setPlaceholderText(_translate("TerminalTab", "1"))
        self.labelBaud.setText(_translate("TerminalTab", "Rychlost (baud)"))
        self.lineEditDataBitCount.setPlaceholderText(_translate("TerminalTab", "8"))
        self.labelDataBitCount.setText(_translate("TerminalTab", "Počet datových bitů"))
        self.labelStopBitCount.setText(_translate("TerminalTab", "Počet stop bitů"))
        self.comboBox_2.setPlaceholderText(_translate("TerminalTab", "Žádná"))
        self.comboBox_2.setItemText(0, _translate("TerminalTab", "Žádná"))
        self.comboBox_2.setItemText(1, _translate("TerminalTab", "Lichá"))
        self.comboBox_2.setItemText(2, _translate("TerminalTab", "Sudá"))