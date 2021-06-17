# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions.functions import resource_path


class FormChatMenu(object):

    def setup_frm_chat_menu(self, frm_menu):
        if not frm_menu.objectName():
            frm_menu.setObjectName(u"frm_menu")
        frm_menu.resize(200, 563)
        frm_menu.setMinimumSize(QSize(200, 563))
        frm_menu.setMaximumSize(QSize(200, 16777215))
        frm_menu.setStyleSheet(u"QFrame#frm_menu {\n"
                                "	background-color: #DBDBDB;\n"
                                "}")

        self.vrl_chat_menu = QVBoxLayout(frm_menu)
        self.vrl_chat_menu.setSpacing(0)
        self.vrl_chat_menu.setObjectName(u"vrl_chat_menu")
        self.vrl_chat_menu.setContentsMargins(0, 0, 0, 0)

        self.frm_chat_menu = QFrame(frm_menu)
        self.frm_chat_menu.setObjectName(u"frm_chat_menu")
        self.frm_chat_menu.setMinimumSize(QSize(200, 563))
        self.frm_chat_menu.setMaximumSize(QSize(200, 16777215))
        self.frm_chat_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_chat_menu.setFrameShadow(QFrame.Raised)

        self.grl_chat_menu = QGridLayout(self.frm_chat_menu)
        self.grl_chat_menu.setSpacing(0)
        self.grl_chat_menu.setObjectName(u"grl_chat_menu")
        self.grl_chat_menu.setContentsMargins(0, 0, 0, 0)

        self.hls_between_border_left_and_search_in_chat = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.grl_chat_menu.addItem(self.hls_between_border_left_and_search_in_chat, 1, 1, 1, 1)

        self.vls_between_buttom_and_title_chat_in_chat = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grl_chat_menu.addItem(self.vls_between_buttom_and_title_chat_in_chat, 7, 2, 1, 1)

        self.lbl_chats = QLabel(self.frm_chat_menu)
        self.lbl_chats.setObjectName(u"lbl_chats")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_chats.setFont(font)
        self.lbl_chats.setStyleSheet(u"QLabel#lbl_chats {\n"
                                     "	color: #909090;\n"
                                     "}")

        self.grl_chat_menu.addWidget(self.lbl_chats, 8, 2, 1, 1)

        self.hls_between_border_left_and_title_chat_in_chat = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.grl_chat_menu.addItem(self.hls_between_border_left_and_title_chat_in_chat, 8, 1, 1, 1)

        self.vls_between_title_and_chat_in_chat = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grl_chat_menu.addItem(self.vls_between_title_and_chat_in_chat, 9, 2, 1, 1)

        self.sra_chat = QScrollArea(self.frm_chat_menu)
        self.sra_chat.setObjectName(u"sra_chat")
        self.sra_chat.setMinimumSize(QSize(200, 371))
        self.sra_chat.setMaximumSize(QSize(200, 16777215))
        self.sra_chat.setFocusPolicy(Qt.NoFocus)
        self.sra_chat.setStyleSheet(u"QScrollArea QWidget {   \n"
                                    "    background-color:#DBDBDB;\n"
                                    "}\n"
                                    "QScrollArea {\n"
                                    "	border-width: 1px;\n"
                                    "	border-style: solid;\n"
                                    "	border-color: #CACACA;\n"
                                    "	border-left-style:none;\n"
                                    "	border-right-style:none;\n"
                                    "}\n")
        self.sra_chat.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sra_chat.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sra_chat.setWidgetResizable(True)

        self.sra_user_chat = QWidget()
        self.sra_user_chat.setObjectName(u"sra_user_chat")
        self.sra_user_chat.setGeometry(QRect(0, 0, 198, 382))

        self.vrl_user_chat = QVBoxLayout(self.sra_user_chat)
        self.vrl_user_chat.setSpacing(0)
        self.vrl_user_chat.setObjectName(u"vrl_user_chat")
        self.vrl_user_chat.setContentsMargins(0, 0, 0, 0)

        self.vsl_between_user_and_border = QSpacerItem(1, 317, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #self.vrl_user_chat.addItem(self.vsl_between_user_and_border)

        self.sra_chat.setWidget(self.sra_user_chat)

        self.grl_chat_menu.addWidget(self.sra_chat, 11, 1, 1, 7)

        self.txt_search_chat = QLineEdit(self.frm_chat_menu)
        self.txt_search_chat.setObjectName(u"txt_search_chat")
        self.txt_search_chat.setMinimumSize(QSize(181, 28))
        self.txt_search_chat.setMaximumSize(QSize(181, 28))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.txt_search_chat.setFont(font1)
        self.txt_search_chat.setFocusPolicy(Qt.ClickFocus)
        self.txt_search_chat.setStyleSheet(u"QLineEdit#txt_search_chat{\n"
                                           "	background-color: #F1F1F1;\n"
                                           "	color: #8C8C8C;\n"
                                           "	border: 1px solid #AFAEAE;\n"
                                           "	border-radius: 5px;\n"
                                           "}")
        self.txt_search_chat.setMaxLength(40)

        self.grl_chat_menu.addWidget(self.txt_search_chat, 1, 2, 1, 1)

        self.btn_all_chats = QPushButton(self.frm_chat_menu)
        self.btn_all_chats.setObjectName(u"btn_all_chats")
        self.btn_all_chats.setMinimumSize(QSize(200, 30))
        self.btn_all_chats.setMaximumSize(QSize(200, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        self.btn_all_chats.setFont(font2)
        self.btn_all_chats.setStyleSheet(u"QPushButton#btn_all_chats {\n"
                                         "	text-align:left;\n"
                                         "	text-decoration: none;\n"
                                         "	margin-left: 20px;\n"
                                         "	border: none;\n"
                                         "	color: #555555;\n"
                                         "}\n"
                                         "QPushButton#btn_all_chats:hover {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_all_chats:pressed {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_all_chats:focus {\n"
                                         "    color: #00B1FF;\n"
                                         "	text-decoration: underline;\n"
                                         "}")
        self.btn_all_chats.setIconSize(QSize(0, 0))

        self.grl_chat_menu.addWidget(self.btn_all_chats, 4, 1, 1, 7)

        self.btn_recent = QPushButton(self.frm_chat_menu)
        self.btn_recent.setObjectName(u"btn_recent")
        self.btn_recent.setMinimumSize(QSize(200, 30))
        self.btn_recent.setMaximumSize(QSize(200, 30))
        self.btn_recent.setFont(font2)
        self.btn_recent.setStyleSheet(u"QPushButton#btn_recent {\n"
                                      "	text-align:left;\n"
                                      "	text-decoration: none;\n"
                                      "	margin-left: 20px;\n"
                                      "	border: none;\n"
                                      "	color: #555555;\n"
                                      "}\n"
                                      "QPushButton#btn_recent:hover {\n"
                                      "	color: #00B1FF;\n"
                                      "	text-decoration: none;\n"
                                      "}\n"
                                      "QPushButton#btn_recent:pressed {\n"
                                      "	color: #00B1FF;\n"
                                      "	text-decoration: none;\n"
                                      "}\n"
                                      "QPushButton#btn_recent:focus {\n"
                                      "    color: #00B1FF;\n"
                                      "	text-decoration: underline;\n"
                                      "}")
        self.btn_recent.setIconSize(QSize(0, 0))

        self.grl_chat_menu.addWidget(self.btn_recent, 5, 1, 2, 7)

        self.vls_between_search_and_buttom_in_chat = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grl_chat_menu.addItem(self.vls_between_search_and_buttom_in_chat, 2, 2, 1, 1)

        self.vls_between_border_top_and_search_in_chat = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grl_chat_menu.addItem(self.vls_between_border_top_and_search_in_chat, 0, 2, 1, 1)

        self.vrl_chat_menu.addWidget(self.frm_chat_menu)

        self.retranslate_chat_menu(frm_menu)

        QMetaObject.connectSlotsByName(frm_menu)

    def retranslate_chat_menu(self, frm_menu):
        frm_menu.setWindowTitle("")
        self.btn_all_chats.setText(QCoreApplication.translate("frm_menu", u"Todos Chats", None))
        self.lbl_chats.setText(QCoreApplication.translate("frm_menu", u"Chats", None))
        self.txt_search_chat.setStatusTip(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_chat.setWhatsThis(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_chat.setAccessibleName(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_chat.setAccessibleDescription(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_chat.setText("")
        self.txt_search_chat.setPlaceholderText(QCoreApplication.translate("frm_menu", u" Pesquisar", None))
        self.btn_recent.setText(QCoreApplication.translate("frm_menu", u"Recentes", None))

