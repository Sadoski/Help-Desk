# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormHomeMenu(object):

    def setup_frm_home_menu(self, frm_menu):
        if not frm_menu.objectName():
            frm_menu.setObjectName(u"frm_menu")
        frm_menu.resize(200, 563)
        frm_menu.setMinimumSize(QSize(200, 563))
        frm_menu.setMaximumSize(QSize(200, 16777215))
        frm_menu.setStyleSheet(u"QFrame#frm_menu {\n"
                                "	background-color: #DBDBDB;\n"
                                "}")

        self.vrl_menu = QVBoxLayout(frm_menu)
        self.vrl_menu.setSpacing(0)
        self.vrl_menu.setObjectName(u"vrl_menu")
        self.vrl_menu.setContentsMargins(0, 0, 0, 0)

        self.frm_home_menu = QFrame(frm_menu)
        self.frm_home_menu.setObjectName(u"frm_home_menu")
        self.frm_home_menu.setMinimumSize(QSize(200, 563))
        self.frm_home_menu.setMaximumSize(QSize(200, 16777215))
        self.frm_home_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_home_menu.setFrameShadow(QFrame.Raised)

        self.txt_search = QLineEdit(self.frm_home_menu)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setGeometry(QRect(9, 10, 181, 28))
        self.txt_search.setMinimumSize(QSize(181, 28))
        self.txt_search.setMaximumSize(QSize(181, 28))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.txt_search.setFont(font)
        self.txt_search.setFocusPolicy(Qt.ClickFocus)
        self.txt_search.setStyleSheet(u"QLineEdit#txt_search {\n"
                                       "	background-color: #F1F1F1;\n"
                                       "	color: #8C8C8C;\n"
                                       "	border: 1px solid #AFAEAE;\n"
                                       "	border-radius: 5px;\n"
                                       "}")
        self.txt_search.setMaxLength(40)

        self.btn_dashboad = QPushButton(self.frm_home_menu)
        self.btn_dashboad.setObjectName(u"btn_dashboad")
        self.btn_dashboad.setGeometry(QRect(0, 70, 200, 30))
        self.btn_dashboad.setMinimumSize(QSize(200, 30))
        self.btn_dashboad.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.btn_dashboad.setFont(font1)
        self.btn_dashboad.setStyleSheet(u"QPushButton#btn_dashboad {\n"
                                         "	text-align:left;\n"
                                         "	text-decoration: none;\n"
                                         "	margin-left: 20px;\n"
                                         "	border: none;\n"
                                         "	color: #555555;\n"
                                         "}\n"
                                         "QPushButton#btn_dashboad:hover {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_dashboad:pressed {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_dashboad:focus {\n"
                                         "    color: #00B1FF;\n"
                                         "	text-decoration: underline;\n"
                                         "}")
        self.btn_dashboad.setIconSize(QSize(0, 0))

        self.vrl_menu.addWidget(self.frm_home_menu)

        self.retranslate_home_menu(frm_menu)

        QMetaObject.connectSlotsByName(frm_menu)

    def retranslate_home_menu(self, frm_menu):
        frm_menu.setWindowTitle("")
        self.txt_search.setStatusTip(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setWhatsThis(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setAccessibleName(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setAccessibleDescription(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setText("")
        self.txt_search.setPlaceholderText(QCoreApplication.translate("frm_menu", u" Pesquisar", None))
        self.btn_dashboad.setText(QCoreApplication.translate("frm_menu", u"Dashboard", None))

