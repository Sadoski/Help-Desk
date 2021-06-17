# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions.functions import resource_path


class FormChatMessageReceived(QFrame):
    
    def __init__(self):
        QFrame.__init__(self)
        #self.setObjectName(u"frm_chat_message_received")
        self.setMinimumSize(QSize(642, 80))
        self.setStyleSheet(u"QFrame {\n"
                            "	background: white;\n"
                            "}")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.grl_chat_message_received = QGridLayout(self)
        self.grl_chat_message_received.setSpacing(0)
        self.grl_chat_message_received.setObjectName(u"grl_chat_message_received")
        self.grl_chat_message_received.setSizeConstraint(QLayout.SetMaximumSize)
        self.grl_chat_message_received.setContentsMargins(0, 0, 0, 0)

        self.frm_content_icon_user_message_chat_received = QFrame(self)
        self.frm_content_icon_user_message_chat_received.setObjectName(u"frm_content_icon_user_message_chat_received")
        self.frm_content_icon_user_message_chat_received.setMinimumSize(QSize(71, 78))
        self.frm_content_icon_user_message_chat_received.setFrameShape(QFrame.StyledPanel)
        self.frm_content_icon_user_message_chat_received.setFrameShadow(QFrame.Raised)

        self.vrl_content_icon_user_message_chat_received = QVBoxLayout(self.frm_content_icon_user_message_chat_received)
        self.vrl_content_icon_user_message_chat_received.setSpacing(0)
        self.vrl_content_icon_user_message_chat_received.setObjectName(u"vrl_content_icon_user_message_chat_received")
        self.vrl_content_icon_user_message_chat_received.setContentsMargins(10, 0, 0, 0)

        self.lbl_img_user_received = QLabel(self.frm_content_icon_user_message_chat_received)
        self.lbl_img_user_received.setObjectName(u"lbl_img_user_received")
        self.lbl_img_user_received.setMinimumSize(QSize(50, 50))
        self.lbl_img_user_received.setMaximumSize(QSize(35, 35))
        self.lbl_img_user_received.setStyleSheet(u"QLabel {\n"
                                                 "	border-radius: 15px;\n"
                                                 "}")
        img = QImage()
        img.load(resource_path(u"../img/profile_user.jpg"), "JPG")
        self.lbl_img_user_received.resize(img.width(), img.height())
        pixmap = QPixmap(img.width(), img.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        clipPath = QPainterPath()
        clipPath.addRoundedRect(QRectF(img.rect()), img.width() // 2, img.width() // 2)
        painter.setClipPath(clipPath)
        painter.drawPixmap(0, 0, QPixmap(img))
        painter.end()
        self.lbl_img_user_received.setPixmap(pixmap)
        self.lbl_img_user_received.setScaledContents(True)
        self.lbl_img_user_received.setText("")

        self.vrl_content_icon_user_message_chat_received.addWidget(self.lbl_img_user_received)

        self.vls_between_icon_user_and_border_bottom_chat_message_received = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vrl_content_icon_user_message_chat_received.addItem(self.vls_between_icon_user_and_border_bottom_chat_message_received)

        self.grl_chat_message_received.addWidget(self.frm_content_icon_user_message_chat_received, 0, 0, 2, 1)

        self.frm_content_header_message_chat_received = QFrame(self)
        self.frm_content_header_message_chat_received.setObjectName(u"frm_content_header_message_chat_received")
        self.frm_content_header_message_chat_received.setMinimumSize(QSize(571, 30))
        self.frm_content_header_message_chat_received.setMaximumSize(QSize(16777215, 30))
        self.frm_content_header_message_chat_received.setFrameShape(QFrame.StyledPanel)
        self.frm_content_header_message_chat_received.setFrameShadow(QFrame.Raised)

        self.hzl_content_header_message_chat_received = QHBoxLayout(self.frm_content_header_message_chat_received)
        self.hzl_content_header_message_chat_received.setSpacing(0)
        self.hzl_content_header_message_chat_received.setObjectName(u"hzl_content_header_message_chat_received")
        self.hzl_content_header_message_chat_received.setContentsMargins(0, 0, 0, 0)

        self.lbl_name_user_received = QLabel(self.frm_content_header_message_chat_received)
        self.lbl_name_user_received.setObjectName(u"lbl_name_user_received")
        self.lbl_name_user_received.setMinimumSize(QSize(341, 16))
        self.lbl_name_user_received.setMaximumSize(QSize(341, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name_user_received.setFont(font)
        self.lbl_name_user_received.setStyleSheet(u"QLabel {\n"
                                                  "	color: #605D5D;\n"
                                                  "}")
        self.lbl_name_user_received.setText(u"Jefferson A. Sadoski")

        self.hzl_content_header_message_chat_received.addWidget(self.lbl_name_user_received)

        self.hls_between_name_user_and_border_right_chat_message_received = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_header_message_chat_received.addItem(self.hls_between_name_user_and_border_right_chat_message_received)

        self.btn_menu_message_chat_receiverd = QToolButton(self.frm_content_header_message_chat_received)
        self.btn_menu_message_chat_receiverd.setObjectName(u"btn_menu_message_chat_receiverd")
        self.btn_menu_message_chat_receiverd.setMinimumSize(QSize(25, 25))
        self.btn_menu_message_chat_receiverd.setMaximumSize(QSize(25, 25))
        self.btn_menu_message_chat_receiverd.setStyleSheet(u"QToolButton#btn_menu_message_chat_receiverd {\n"
                                                            "	background: transparent;\n"
                                                            "	color: white;\n"
                                                            "	border: 3px solid  transparent;\n"
                                                            "	border-radius: 5px;\n"
                                                            "}\n"
                                                            "QToolButton#btn_menu_message_chat_receiverd:hover {\n"
                                                            "}\n"
                                                            "QToolButton#btn_menu_message_chat_receiverd:pressed {\n"
                                                            "}\n")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/menu-.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_message_chat_receiverd.setIcon(icon1)

        self.hzl_content_header_message_chat_received.addWidget(self.btn_menu_message_chat_receiverd)

        self.grl_chat_message_received.addWidget(self.frm_content_header_message_chat_received, 0, 1, 1, 1)

        self.frm_content_message_chat_received = QFrame(self)
        self.frm_content_message_chat_received.setObjectName(u"frm_content_message_chat_received")
        self.frm_content_message_chat_received.setMinimumSize(QSize(571, 48))
        self.frm_content_message_chat_received.setFrameShape(QFrame.StyledPanel)
        self.frm_content_message_chat_received.setFrameShadow(QFrame.Raised)

        self.vrl_content_message_chat_received = QVBoxLayout(self.frm_content_message_chat_received)
        self.vrl_content_message_chat_received.setSpacing(0)
        self.vrl_content_message_chat_received.setObjectName(u"vrl_content_message_chat_received")
        #self.vrl_content_message_chat_received.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.vrl_content_message_chat_received.setContentsMargins(0, 0, 0, 0)

        self.lbl_message_chat_received = QLabel(self.frm_content_message_chat_received)
        self.lbl_message_chat_received.setObjectName(u"lbl_message_chat_received")
        self.lbl_message_chat_received.setFont(font)
        self.lbl_message_chat_received.setWordWrap(True)
        self.lbl_message_chat_received.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.lbl_message_chat_received.setStyleSheet(u"QLabel{ "
                                                      "   background: #D6EAF8;"
                                                      "   padding: 5px;"
                                                      "   border-top-right-radius: 5px;"
                                                      "   border-bottom-left-radius: 5px;"
                                                      "   border-bottom-right-radius: 5px;"
                                                      "   margin-top: 10px;"
                                                      "   margin-bottom: 10px;"
                                                      "   margin-right: 10px;"
                                                      "   margin-left: 10px;"
                                                      "}")

        self.vrl_content_message_chat_received.addWidget(self.lbl_message_chat_received)

        self.vls_content_message_chat_received = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.vrl_content_message_chat_received.addItem(self.vls_content_message_chat_received)

        self.grl_chat_message_received.addWidget(self.frm_content_message_chat_received, 1, 1, 1, 1)


