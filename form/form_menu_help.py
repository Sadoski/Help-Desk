# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormHelpMenu(object):

    def setup_frm_help_menu(self, frm_menu):
        if not frm_menu.objectName():
            frm_menu.setObjectName(u"frm_menu")
        frm_menu.resize(200, 563)
        frm_menu.setMinimumSize(QSize(200, 563))
        frm_menu.setMaximumSize(QSize(200, 16777215))
        frm_menu.setStyleSheet(u"QFrame#frm_menu {\n"
                                "	background-color: #DBDBDB;\n"
                                "}")

        self.vrl_help_menu = QVBoxLayout(frm_menu)
        self.vrl_help_menu.setSpacing(0)
        self.vrl_help_menu.setObjectName(u"vrl_help_menu")
        self.vrl_help_menu.setContentsMargins(0, 0, 0, 0)

        self.frm_help_menu = QFrame(frm_menu)
        self.frm_help_menu.setObjectName(u"frm_help_menu")
        self.frm_help_menu.setMinimumSize(QSize(200, 563))
        self.frm_help_menu.setMaximumSize(QSize(200, 16777215))
        self.frm_help_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_help_menu.setFrameShadow(QFrame.Raised)

        self.frl_help_menu = QFormLayout(self.frm_help_menu)
        self.frl_help_menu.setObjectName(u"frl_help_menu")
        self.frl_help_menu.setHorizontalSpacing(0)
        self.frl_help_menu.setVerticalSpacing(0)
        self.frl_help_menu.setContentsMargins(0, 0, 0, 0)
        self.vls_between_border_top_and_search_in_help = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.frl_help_menu.setItem(0, QFormLayout.FieldRole, self.vls_between_border_top_and_search_in_help)

        self.hls_between_border_left_and_search_in_help = QSpacerItem(8, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.frl_help_menu.setItem(1, QFormLayout.LabelRole, self.hls_between_border_left_and_search_in_help)

        self.txt_search_help = QLineEdit(self.frm_help_menu)
        self.txt_search_help.setObjectName(u"txt_search_help")
        self.txt_search_help.setMinimumSize(QSize(181, 28))
        self.txt_search_help.setMaximumSize(QSize(181, 28))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.txt_search_help.setFont(font)
        self.txt_search_help.setFocusPolicy(Qt.ClickFocus)
        self.txt_search_help.setStyleSheet(u"QLineEdit#txt_search_help{\n"
                                            "	background-color: #F1F1F1;\n"
                                            "	color: #8C8C8C;\n"
                                            "	border: 1px solid #AFAEAE;\n"
                                            "	border-radius: 5px;\n"
                                            "}")
        self.txt_search_help.setMaxLength(40)

        self.frl_help_menu.setWidget(1, QFormLayout.FieldRole, self.txt_search_help)

        self.vls_between_search_and_buttom_in_help = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.frl_help_menu.setItem(3, QFormLayout.FieldRole, self.vls_between_search_and_buttom_in_help)

        self.btn_profile = QPushButton(self.frm_help_menu)
        self.btn_profile.setObjectName(u"btn_profile")
        self.btn_profile.setMinimumSize(QSize(200, 30))
        self.btn_profile.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.btn_profile.setFont(font1)
        self.btn_profile.setStyleSheet(u"QPushButton#btn_profile {\n"
                                        "	text-align:left;\n"
                                        "	text-decoration: none;\n"
                                        "	margin-left: 20px;\n"
                                        "	border: none;\n"
                                        "	color: #555555;\n"
                                        "}\n"
                                        "QPushButton#btn_profile:hover {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_profile:pressed {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_profile:focus {\n"
                                        "    color: #00B1FF;\n"
                                        "	text-decoration: underline;\n"
                                        "}")
        self.btn_profile.setIconSize(QSize(0, 0))

        self.frl_help_menu.setWidget(4, QFormLayout.SpanningRole, self.btn_profile)

        self.btn_settings = QPushButton(self.frm_help_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(200, 30))
        self.btn_settings.setMaximumSize(QSize(200, 30))
        self.btn_settings.setFont(font1)
        self.btn_settings.setStyleSheet(u"QPushButton#btn_settings {\n"
                                         "	text-align:left;\n"
                                         "	text-decoration: none;\n"
                                         "	margin-left: 20px;\n"
                                         "	border: none;\n"
                                         "	color: #555555;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:hover {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:pressed {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:focus {\n"
                                         "    color: #00B1FF;\n"
                                         "	text-decoration: underline;\n"
                                         "}")
        self.btn_settings.setIconSize(QSize(0, 0))

        self.frl_help_menu.setWidget(6, QFormLayout.SpanningRole, self.btn_settings)

        self.vsl_between_buttom_and_border_in_help = QSpacerItem(184, 438, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.frl_help_menu.setItem(8, QFormLayout.FieldRole, self.vsl_between_buttom_and_border_in_help)

        self.vrl_help_menu.addWidget(self.frm_help_menu)

        self.retranslate_help_menu(frm_menu)

        QMetaObject.connectSlotsByName(frm_menu)

    def retranslate_help_menu(self, frm_menu):
        frm_menu.setWindowTitle("")
        self.txt_search_help.setStatusTip(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_help.setWhatsThis(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_help.setAccessibleName(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_help.setAccessibleDescription(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_help.setText("")
        self.txt_search_help.setPlaceholderText(QCoreApplication.translate("frm_menu", u" Pesquisar", None))
        self.btn_profile.setText(QCoreApplication.translate("frm_menu", u"Ajuda", None))
        self.btn_settings.setText(QCoreApplication.translate("frm_menu", u"Sistema", None))

