# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions.functions import resource_path


class FormChatMessageSent(QFrame):
    resized = Signal()

    def __init__(self):
        QFrame.__init__(self)
        #self.setObjectName(u"frm_chat_message_sent")
        self.setMinimumSize(QSize(642, 80))
        self.setStyleSheet(u"QFrame {\n"
                            "	background: white;\n"
                            "}")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.grl_chat_content_message_sent = QGridLayout(self)
        self.grl_chat_content_message_sent.setSpacing(0)
        self.grl_chat_content_message_sent.setObjectName(u"grl_chat_content_message_sent")
        self.grl_chat_content_message_sent.setSizeConstraint(QLayout.SetMaximumSize)
        self.grl_chat_content_message_sent.setContentsMargins(0, 0, 0, 0)

        self.frm_content_icon_user_message_chat_sent = QFrame(self)
        self.frm_content_icon_user_message_chat_sent.setObjectName(u"frm_content_icon_user_message_chat_sent")
        self.frm_content_icon_user_message_chat_sent.setMinimumSize(QSize(71, 78))
        self.frm_content_icon_user_message_chat_sent.setFrameShape(QFrame.StyledPanel)
        self.frm_content_icon_user_message_chat_sent.setFrameShadow(QFrame.Raised)

        self.vrl_content_icon_user_message_chat_sent = QVBoxLayout(self.frm_content_icon_user_message_chat_sent)
        self.vrl_content_icon_user_message_chat_sent.setSpacing(0)
        self.vrl_content_icon_user_message_chat_sent.setObjectName(u"vrl_content_icon_user_message_chat_sent")
        self.vrl_content_icon_user_message_chat_sent.setContentsMargins(10, 0, 0, 0)

        self.lbl_img_user_sent = QLabel(self.frm_content_icon_user_message_chat_sent)
        self.lbl_img_user_sent.setObjectName(u"lbl_img_user_sent")
        self.lbl_img_user_sent.setMinimumSize(QSize(50, 50))
        self.lbl_img_user_sent.setMaximumSize(QSize(35, 35))
        self.lbl_img_user_sent.setStyleSheet(u"QLabel {\n"
                                             "	border-radius: 15px;\n"
                                             "}")
        img = QImage()
        img.load(resource_path(u"../img/profile_user.jpg"), "JPG")
        self.lbl_img_user_sent.resize(img.width(), img.height())
        pixmap = QPixmap(img.width(), img.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        clipPath = QPainterPath()
        clipPath.addRoundedRect(QRectF(img.rect()), img.width() // 2, img.width() // 2)
        painter.setClipPath(clipPath)
        painter.drawPixmap(0, 0, QPixmap(img))
        painter.end()
        self.lbl_img_user_sent.setPixmap(pixmap)
        self.lbl_img_user_sent.setScaledContents(True)
        self.lbl_img_user_sent.setText("")

        self.vrl_content_icon_user_message_chat_sent.addWidget(self.lbl_img_user_sent)

        self.vls_between_icon_user_and_border_bottom_chat_message_sent = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vrl_content_icon_user_message_chat_sent.addItem(self.vls_between_icon_user_and_border_bottom_chat_message_sent)

        self.grl_chat_content_message_sent.addWidget(self.frm_content_icon_user_message_chat_sent, 0, 1, 2, 1)

        self.frm_content_header_message_chat_sent = QFrame(self)
        self.frm_content_header_message_chat_sent.setObjectName(u"frm_content_header_message_chat_sent")
        self.frm_content_header_message_chat_sent.setMinimumSize(QSize(571, 30))
        self.frm_content_header_message_chat_sent.setMaximumSize(QSize(16777215, 30))
        self.frm_content_header_message_chat_sent.setFrameShape(QFrame.StyledPanel)
        self.frm_content_header_message_chat_sent.setFrameShadow(QFrame.Raised)

        self.hzl_content_header_message_chat_sent = QHBoxLayout(self.frm_content_header_message_chat_sent)
        self.hzl_content_header_message_chat_sent.setSpacing(0)
        self.hzl_content_header_message_chat_sent.setObjectName(u"hzl_content_header_message_chat_sent")
        self.hzl_content_header_message_chat_sent.setContentsMargins(0, 0, 0, 0)

        self.btn_menu_message_chat_sent = QToolButton(self.frm_content_header_message_chat_sent)
        self.btn_menu_message_chat_sent.setObjectName(u"btn_menu_message_chat_sent")
        self.btn_menu_message_chat_sent.setMinimumSize(QSize(25, 25))
        self.btn_menu_message_chat_sent.setMaximumSize(QSize(25, 25))
        self.btn_menu_message_chat_sent.setStyleSheet(u"QToolButton#btn_menu_message_chat_sent {\n"
                                                      "	background: transparent;\n"
                                                      "	color: white;\n"
                                                      "	border: 3px solid  transparent;\n"
                                                      "	border-radius: 5px;\n"
                                                      "}\n"
                                                      "QToolButton#btn_menu_message_chat_sent:hover {\n"
                                                      "}\n"
                                                      "QToolButton#btn_menu_message_chat_sent:pressed {\n"
                                                      "}\n")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/menu-.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_message_chat_sent.setIcon(icon1)

        self.hzl_content_header_message_chat_sent.addWidget(self.btn_menu_message_chat_sent)

        self.hls_between_name_user_and_border_right_chat_message_sent = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_header_message_chat_sent.addItem(self.hls_between_name_user_and_border_right_chat_message_sent)

        self.lbl_name_user_sent = QLabel(self.frm_content_header_message_chat_sent)
        self.lbl_name_user_sent.setObjectName(u"lbl_name_user_sent")
        self.lbl_name_user_sent.setMinimumSize(QSize(341, 16))
        self.lbl_name_user_sent.setMaximumSize(QSize(341, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name_user_sent.setFont(font)
        self.lbl_name_user_sent.setStyleSheet(u"QLabel {\n"
                                              "	color: #605D5D;\n"
                                              "}")
        self.lbl_name_user_sent.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lbl_name_user_sent.setText(u"Jefferson A. Sadoski")

        self.hzl_content_header_message_chat_sent.addWidget(self.lbl_name_user_sent)

        self.grl_chat_content_message_sent.addWidget(self.frm_content_header_message_chat_sent, 0, 0, 1, 1)

        self.frm_content_message_chat_sent = QFrame(self)
        self.frm_content_message_chat_sent.setObjectName(u"frm_content_message_chat_sent")
        self.frm_content_message_chat_sent.setMinimumSize(QSize(571, 48))
        self.frm_content_message_chat_sent.setFrameShape(QFrame.StyledPanel)
        self.frm_content_message_chat_sent.setFrameShadow(QFrame.Raised)
        """
        self.vrl_content_message_chat_sent = QVBoxLayout(self.frm_content_message_chat_sent)
        self.vrl_content_message_chat_sent.setSpacing(0)
        self.vrl_content_message_chat_sent.setObjectName(u"vrl_content_message_chat_sent")
        #self.vrl_content_message_chat_sent.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.vrl_content_message_chat_sent.setContentsMargins(0, 0, 0, 0)
        """
        self.grl_content_message_chat_sent = QGridLayout(self.frm_content_message_chat_sent)
        self.grl_content_message_chat_sent.setObjectName(u"grl_content_message_chat_sent")
        self.grl_content_message_chat_sent.setSizeConstraint(QLayout.SetMaximumSize)
        self.grl_content_message_chat_sent.setContentsMargins(0, 0, 0, 0)

        self.vls_content_message_chat_sent = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.grl_content_message_chat_sent.addItem(self.vls_content_message_chat_sent, 1, 1, 1, 1)

        self.lbl_message_chat_sent = QLabel(self.frm_content_message_chat_sent)
        self.lbl_message_chat_sent.setObjectName(u"lbl_message_chat_sent")
        self.lbl_message_chat_sent.setFont(font)
        self.lbl_message_chat_sent.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.lbl_message_chat_sent.setStyleSheet(u"QLabel{ "
                                                  "  background: #D5F5E3;"
                                                  "  padding: 10px;"
                                                  "  border-top-left-radius: 5px;"
                                                  "  border-bottom-left-radius: 5px;"
                                                  "  border-bottom-right-radius: 5px;"
                                                  "  margin-top: 10px;"
                                                  "  margin-bottom: 10px;"
                                                  "  margin-right: 10px;"
                                                  "  margin-left: 10px;"
                                                  "}")
        #self.lbl_message_chat_sent.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lbl_message_chat_sent.setWordWrap(True)
        self.lbl_message_chat_sent.setMinimumSize(QSize(0, 0))
        #self.lbl_message_chat_sent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred )
        #self.lbl_message_chat_sent.setTextFormat(Qt.AutoText)

        self.grl_content_message_chat_sent.addWidget(self.lbl_message_chat_sent, 0, 1, 1, 1)

        self.hls_between_border_left_and_message_chat = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.grl_content_message_chat_sent.addItem(self.hls_between_border_left_and_message_chat, 0, 0, 1, 1)

        self.grl_chat_content_message_sent.addWidget(self.frm_content_message_chat_sent, 1, 0, 1, 1)
        """
        self.vrl_content_message_chat_sent.addWidget(self.lbl_message_chat_sent)

        self.vls_content_message_chat_sent = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.vrl_content_message_chat_sent.addItem(self.vls_content_message_chat_sent)

        self.grl_chat_content_message_sent.addWidget(self.frm_content_message_chat_sent, 1, 0, 1, 1)

        """

