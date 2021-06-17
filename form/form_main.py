# -*- coding: utf-8 -*-
"""
Modulo específico do designer do corpo principal do sistema
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions.functions import resource_path


class FormMain(object):

    def setupUi(self, form_main):
        if not form_main.objectName():
            form_main.setObjectName(u"form_main")
        form_main.setWindowModality(Qt.NonModal)
        form_main.resize(932, 600)
        form_main.setMinimumSize(QSize(932, 600))
        form_main.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowCloseButtonHint)
        form_main.setAttribute(Qt.WA_TranslucentBackground)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        form_main.setFont(font)
        icon = QIcon()
        icon.addFile(resource_path(u"..\img\help-desk.png"), QSize(), QIcon.Normal, QIcon.Off)
        form_main.setWindowIcon(icon)
        form_main.setStyleSheet(u"QMainWindow {\n"
                                 "	background-color: #F5F5F5;\n"
                                 "	border-radius: 13px;\n"
                                 "}")

        self.wdg_main = QWidget(form_main)
        self.wdg_main.setObjectName(u"wdg_main")
        self.wdg_main.setStyleSheet(u"QWidget#wdg_main {\n"
                       "	background-color: #F5F5F5;\n"
                       "	border-radius: 13px;\n"
                       "}")

        self.grl_main = QGridLayout(self.wdg_main)
        self.grl_main.setSpacing(0)
        self.grl_main.setObjectName(u"grl_main")
        self.grl_main.setContentsMargins(0, 0, 0, 0)

        self.wdg_menu = QFrame(self.wdg_main)
        self.wdg_menu.setObjectName(u"wdg_menu")
        self.wdg_menu.setMinimumSize(QSize(200, 0))
        self.wdg_menu.setMaximumSize(QSize(200, 16777215))
        self.wdg_menu.setStyleSheet(u"QFrame#wdg_menu {\n"
                                     "	background-color: #DBDBDB;\n"
                                     "}")

        self.vrl_menu = QVBoxLayout(self.wdg_menu)
        self.vrl_menu.setSpacing(0)
        self.vrl_menu.setObjectName(u"vrl_menu")
        self.vrl_menu.setContentsMargins(0, 0, 0, 0)

        self.frm_top_menu = QFrame(self.wdg_menu)
        self.frm_top_menu.setObjectName(u"frm_top_menu")
        self.frm_top_menu.setMinimumSize(QSize(200, 41))
        self.frm_top_menu.setMaximumSize(QSize(200, 41))
        self.frm_top_menu.setStyleSheet(u"QFrame#frm_top_menu {\n"
                                         "	border-width: 2px; \n"
                                         "	border-style: solid; \n"
                                         "	border-color: #CACACA;\n"
                                         "	border-top-style:none;\n"
                                         "	border-left-style:none;\n"
                                         "	border-right-style:none;\n"
                                         "}")
        self.frm_top_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_top_menu.setFrameShadow(QFrame.Raised)

        self.hzl_top_menu = QHBoxLayout(self.frm_top_menu)
        self.hzl_top_menu.setSpacing(0)
        self.hzl_top_menu.setObjectName(u"hzl_top_menu")
        self.hzl_top_menu.setContentsMargins(0, 0, 0, 0)

        self.lbl_help_desk = QLabel(self.frm_top_menu)
        self.lbl_help_desk.setObjectName(u"lbl_help_desk")
        self.lbl_help_desk.setMinimumSize(QSize(111, 21))
        self.lbl_help_desk.setMaximumSize(QSize(111, 21))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(14)
        self.lbl_help_desk.setFont(font1)
        self.lbl_help_desk.setStyleSheet(u"QLabel {\n"
                                          "	color: #454545;\n"
                                          "}")

        self.hzl_top_menu.addWidget(self.lbl_help_desk)

        self.btn_new_ticket = QPushButton(self.frm_top_menu)
        self.btn_new_ticket.setObjectName(u"btn_new_ticket")
        self.btn_new_ticket.setMinimumSize(QSize(70, 31))
        self.btn_new_ticket.setMaximumSize(QSize(70, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_new_ticket.setFont(font2)
        self.btn_new_ticket.setFocusPolicy(Qt.NoFocus)
        self.btn_new_ticket.setStyleSheet(u"QPushButton#btn_new_ticket {\n"
                                           "	background-color: #2FB7F3;\n"
                                           "	color: white;\n"
                                           "	border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton#btn_new_ticket:hover {\n"
                                           "	background-color:#009CE1;\n"
                                           "}\n"
                                           "QPushButton#btn_new_ticket:pressed {\n"
                                           "	background-color:#0082BC;\n"
                                           "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"..\img\plus-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_ticket.setIcon(icon1)
        self.btn_new_ticket.setIconSize(QSize(10, 10))

        self.hzl_top_menu.addWidget(self.btn_new_ticket)

        self.vrl_menu.addWidget(self.frm_top_menu)

        self.frm_menu = QFrame(self.wdg_menu)
        self.frm_menu.setObjectName(u"frm_menu")
        self.frm_menu.setMinimumSize(QSize(200, 561))
        self.frm_menu.setMaximumSize(QSize(200, 16777215))
        self.frm_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_menu.setFrameShadow(QFrame.Raised)

        self.vrl_main_menu = QVBoxLayout(self.frm_menu)
        self.vrl_main_menu.setSpacing(0)
        self.vrl_main_menu.setObjectName(u"vrl_main_menu")
        self.vrl_main_menu.setContentsMargins(0, 0, 0, 0)

        self.vrl_menu.addWidget(self.frm_menu)

        self.grl_main.addWidget(self.wdg_menu, 0, 1, 3, 1)

        self.frm_button_menu = QFrame(self.wdg_main)
        self.frm_button_menu.setObjectName(u"frm_button_menu")
        self.frm_button_menu.setMinimumSize(QSize(50, 0))
        self.frm_button_menu.setMaximumSize(QSize(41, 16777215))
        self.frm_button_menu.setStyleSheet(u"QFrame#frm_button_menu {\n"
                                            "	background-color: #454545;\n"
                                            "   border-bottom-left-radius: 10px;\n"
                                            "   border-top-left-radius: 10px;\n"
                                            "}\n")
        self.frm_button_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_button_menu.setFrameShadow(QFrame.Raised)

        self.vrl_button_menu = QVBoxLayout(self.frm_button_menu)
        self.vrl_button_menu.setSpacing(0)
        self.vrl_button_menu.setObjectName(u"vrl_button_menu")
        self.vrl_button_menu.setContentsMargins(0, 0, 0, 0)

        self.btn_home = QPushButton(self.frm_button_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(50, 41))
        self.btn_home.setStyleSheet(u"QPushButton#btn_home{\n"
                                     "	background: transparent;\n"
                                     " border-top-left-radius: 10px;\n"
                                     "}\n"
                                     "QPushButton#btn_home:hover {\n"
                                     "	background-color:#929292;\n"
                                     "}\n"
                                     "QPushButton#btn_home:pressed {\n"
                                     "	background-color:#6A6A6A;\n"
                                     "}\n"
                                     "QPushButton#btn_home:focus {\n"
                                     "    background-color:#FC3A3A;\n"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"..\img\home.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon2)
        self.btn_home.setIconSize(QSize(25, 25))

        self.vrl_button_menu.addWidget(self.btn_home)

        self.btn_help_desk = QPushButton(self.frm_button_menu)
        self.btn_help_desk.setObjectName(u"btn_help_desk")
        self.btn_help_desk.setMinimumSize(QSize(50, 41))
        self.btn_help_desk.setStyleSheet(u"QPushButton#btn_help_desk {\n"
                                          "	background: transparent;\n"
                                          "}\n"
                                          "QPushButton#btn_help_desk:hover {\n"
                                          "	background-color:#929292;\n"
                                          "}\n"
                                          "QPushButton#btn_help_desk:pressed {\n"
                                          "	background-color:#6A6A6A;\n"
                                          "}\n"
                                          "QPushButton#btn_help_desk:focus {\n"
                                          "    background-color:#FC3A3A;\n"
                                          "}")
        icon3 = QIcon()
        icon3.addFile(resource_path(u"..\img\chat-help-desk.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help_desk.setIcon(icon3)
        self.btn_help_desk.setIconSize(QSize(25, 25))

        self.vrl_button_menu.addWidget(self.btn_help_desk)

        self.btn_chat = QPushButton(self.frm_button_menu)
        self.btn_chat.setObjectName(u"btn_chat")
        self.btn_chat.setEnabled(True)
        self.btn_chat.setMinimumSize(QSize(50, 41))
        self.btn_chat.setStyleSheet(u"QPushButton#btn_chat {\n"
                                     "	background: transparent;\n"
                                     "}\n"
                                     "QPushButton#btn_chat:hover {\n"
                                     "	background-color:#929292;\n"
                                     "}\n"
                                     "QPushButton#btn_chat:pressed {\n"
                                     "	background-color:#6A6A6A;\n"
                                     "}\n"
                                     "QPushButton#btn_chat:checked {\n"
                                     "    background-color: #929292;\n"
                                     "}\n"
                                     "QPushButton#btn_chat:focus {\n"
                                     "    background-color:#FC3A3A;\n"
                                     "}\n")
        icon4 = QIcon()
        icon4.addFile(resource_path(u"..\img\chat.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chat.setIcon(icon4)
        self.btn_chat.setIconSize(QSize(33, 33))

        self.vrl_button_menu.addWidget(self.btn_chat)

        self.vls_between_setting_ = QSpacerItem(20, 308, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.vrl_button_menu.addItem(self.vls_between_setting_)

        self.btn_settings = QPushButton(self.frm_button_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setEnabled(True)
        self.btn_settings.setMinimumSize(QSize(50, 41))
        self.btn_settings.setStyleSheet(u"QPushButton#btn_settings {\n"
                                         "	background: transparent;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:hover {\n"
                                         "	background-color:#929292;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:pressed {\n"
                                         "	background-color:#6A6A6A;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:checked {\n"
                                         "    background-color: #929292;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:focus {\n"
                                         "    background-color:#FC3A3A;\n"
                                         "}\n")
        icon5 = QIcon()
        icon5.addFile(resource_path(u"..\img\settings.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon5)
        self.btn_settings.setIconSize(QSize(25, 25))

        self.vrl_button_menu.addWidget(self.btn_settings)

        self.btn_help = QPushButton(self.frm_button_menu)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setEnabled(True)
        self.btn_help.setMinimumSize(QSize(50, 41))
        self.btn_help.setStyleSheet(u"QPushButton#btn_help {\n"
                                     "	background: transparent;\n"
                                     "}\n"
                                     "QPushButton#btn_help:hover {\n"
                                     "	background-color:#929292;\n"
                                     "}\n"
                                     "QPushButton#btn_help:pressed {\n"
                                     "	background-color:#6A6A6A;\n"
                                     "}\n"
                                     "QPushButton#btn_help:checked {\n"
                                     "    background-color: #929292;\n"
                                     "}\n"
                                     "QPushButton#btn_help:focus {\n"
                                     "    background-color:#FC3A3A;\n"
                                     "}\n")
        icon6 = QIcon()
        icon6.addFile(resource_path(u"..\img\help.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon6)
        self.btn_help.setIconSize(QSize(38, 38))

        self.vrl_button_menu.addWidget(self.btn_help)

        self.vls_between_photo_and_help = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vrl_button_menu.addItem(self.vls_between_photo_and_help)

        self.lbl_photo_user = QLabel(self.frm_button_menu)
        self.lbl_photo_user.setObjectName(u"lbl_photo_user")
        self.lbl_photo_user.setMinimumSize(QSize(50, 50))
        self.lbl_photo_user.setMaximumSize(QSize(50, 50))
        self.lbl_photo_user.setPixmap(QPixmap(u"./img/user.png"))
        self.lbl_photo_user.setScaledContents(True)
        self.lbl_photo_user.setMargin(3)

        self.vrl_button_menu.addWidget(self.lbl_photo_user)

        self.vls_between_border_and_photo = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vrl_button_menu.addItem(self.vls_between_border_and_photo)

        self.grl_main.addWidget(self.frm_button_menu, 0, 0, 3, 1)

        self.frm_top_content = QFrame(self.wdg_main)
        self.frm_top_content.setObjectName(u"frm_top_content")
        self.frm_top_content.setMinimumSize(QSize(591, 41))
        self.frm_top_content.setMaximumSize(QSize(16777215, 41))
        self.frm_top_content.setStyleSheet(u"QFrame#frm_top_content {\n"
                                            "	background-color: #F5F5F5;\n"
                                            "	border-width: 2px; \n"
                                            "	border-style: solid; \n"
                                            "	border-color: #E7E4E4;\n"
                                            "	border-top-style:none;\n"
                                            "	border-left-style:none;\n"
                                            "	border-right-style:none;\n"
                                            "   border-top-right-radius: 10px;"
                                            "}")
        self.frm_top_content.setFrameShape(QFrame.StyledPanel)
        self.frm_top_content.setFrameShadow(QFrame.Raised)

        self.hzl_content = QHBoxLayout(self.frm_top_content)
        self.hzl_content.setSpacing(0)
        self.hzl_content.setObjectName(u"hzl_content")
        self.hzl_content.setContentsMargins(0, 0, 0, 0)

        self.frm_header_content = QFrame(self.frm_top_content)
        self.frm_header_content.setObjectName(u"frm_header_content")
        self.frm_header_content.setMinimumSize(QSize(531, 41))
        self.frm_header_content.setFrameShape(QFrame.StyledPanel)
        self.frm_header_content.setFrameShadow(QFrame.Raised)

        self.lbl_title = QLabel(self.frm_header_content)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setGeometry(QRect(10, 13, 120, 17))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.lbl_title.setFont(font3)

        self.hzl_content.addWidget(self.frm_header_content)

        self.frm_event_window = QFrame(self.frm_top_content)
        self.frm_event_window.setObjectName(u"frm_event_window")
        self.frm_event_window.setMinimumSize(QSize(61, 41))
        self.frm_event_window.setMaximumSize(QSize(61, 41))
        self.frm_event_window.setFrameShape(QFrame.StyledPanel)
        self.frm_event_window.setFrameShadow(QFrame.Raised)

        self.btn_close = QPushButton(self.frm_event_window)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(40, 0, 21, 21))
        self.btn_close.setMinimumSize(QSize(21, 21))
        self.btn_close.setMaximumSize(QSize(21, 21))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"QPushButton#btn_close {\n"
                                      "	background: transparent;\n"
                                      "	border: none;\n"
                                      "   border-top-right-radius: 10px;"
                                      "}\n"
                                      "QPushButton#btn_close:hover {\n"
                                      "	background-color:#EBEAEA;\n"
                                      "	text-decoration: none;\n"
                                      "}\n"
                                      "QPushButton#btn_close:pressed {\n"
                                      "	background-color:#DBDBDB;\n"
                                      "}")
        icon7 = QIcon()
        icon7.addFile(resource_path(u"..\img\close_window.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon7)
        self.btn_close.setIconSize(QSize(10, 10))
        self.btn_close.setFlat(True)

        self.btn_maximize_and_restore = QPushButton(self.frm_event_window)
        self.btn_maximize_and_restore.setObjectName(u"btn_maximize_and_restore")
        self.btn_maximize_and_restore.setGeometry(QRect(20, 0, 21, 21))
        self.btn_maximize_and_restore.setMinimumSize(QSize(21, 21))
        self.btn_maximize_and_restore.setMaximumSize(QSize(21, 21))
        self.btn_maximize_and_restore.setFocusPolicy(Qt.NoFocus)
        self.btn_maximize_and_restore.setStyleSheet(u"QPushButton#btn_maximize_and_restore {\n"
                                                     "	background: transparent;\n"
                                                     "	border: none;\n"
                                                     "}\n"
                                                     "QPushButton#btn_maximize_and_restore:hover {\n"
                                                     "	background-color:#EBEAEA;\n"
                                                     "	text-decoration: none;\n"
                                                     "}\n"
                                                     "QPushButton#btn_maximize_and_restore:pressed {\n"
                                                     "	background-color:#DBDBDB;\n"
                                                     "}")
        icon8 = QIcon()
        icon8.addFile(resource_path(u"..\img\window-maximize.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_and_restore.setIcon(icon8)
        self.btn_maximize_and_restore.setIconSize(QSize(10, 10))
        self.btn_maximize_and_restore.setFlat(True)

        self.btn_minimize = QPushButton(self.frm_event_window)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(0, 0, 21, 21))
        self.btn_minimize.setMinimumSize(QSize(21, 21))
        self.btn_minimize.setMaximumSize(QSize(21, 21))
        self.btn_minimize.setFocusPolicy(Qt.NoFocus)
        self.btn_minimize.setStyleSheet(u"QPushButton#btn_minimize {\n"
                                         "	background: transparent;\n"
                                         "	border: none;\n"
                                         "}\n"
                                         "QPushButton#btn_minimize:hover {\n"
                                         "	background-color:#EBEAEA;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_minimize:pressed {\n"
                                         "	background-color:#DBDBDB;\n"
                                         "}\n")
        icon9 = QIcon()
        icon9.addFile(resource_path(u"..\img\minimize-window.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon9)
        self.btn_minimize.setIconSize(QSize(10, 10))

        self.hzl_content.addWidget(self.frm_event_window)

        self.grl_main.addWidget(self.frm_top_content, 0, 2, 1, 1)

        self.frm_content = QFrame(self.wdg_main)
        self.frm_content.setObjectName(u"frm_content")
        self.frm_content.setMinimumSize(QSize(591, 561))
        self.frm_content.setStyleSheet(u"QFrame#frm_content {\n"
                                        "	background-color: #F5F5F5;\n"
                                        "   border-bottom-right-radius: 15px;"
                                        "}")
        self.frm_content.setFrameShape(QFrame.StyledPanel)
        self.frm_content.setFrameShadow(QFrame.Raised)

        self.grl_content = QGridLayout(self.frm_content)
        self.grl_content.setSpacing(0)
        self.grl_content.setObjectName(u"grl_content")
        self.grl_content.setContentsMargins(0, 0, 0, 0)

        self.grl_main.addWidget(self.frm_content, 1, 2, 2, 1)

        form_main.setCentralWidget(self.wdg_main)

        self.retranslate_main(form_main)

        QMetaObject.connectSlotsByName(form_main)
    # setupUi

    def retranslate_main(self, form_main):
        form_main.setWindowTitle(QCoreApplication.translate("form_main", u"Help Desk", None))
        self.lbl_help_desk.setText(QCoreApplication.translate("form_main", u"Help Desk", None))
        self.btn_new_ticket.setText(QCoreApplication.translate("form_main", u"Ticket", None))
        self.btn_home.setText("")
        self.btn_help_desk.setText("")
        self.btn_chat.setText("")
        self.btn_settings.setText("")
        self.btn_help.setText("")
        self.lbl_photo_user.setText("")
        self.lbl_title.setText("")
        self.btn_close.setText("")
        self.btn_maximize_and_restore.setText("")
        self.btn_minimize.setText("")
    # retranslateUi

