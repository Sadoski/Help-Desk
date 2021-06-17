# -*- coding: utf-8 -*-
"""
Modulo da estrutura da janela do card do usuário no chat
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions.functions import resource_path


class FormCardChatUser(QFrame):

    def setup_frm_card_chat_user(self, frm_card_chat_user):
        if not frm_card_chat_user.objectName():
            frm_card_chat_user.setObjectName(u"card_chat_user")
        frm_card_chat_user.setMinimumSize(QSize(150, 51))
        frm_card_chat_user.setStyleSheet(u"QFrame#card_chat_user {\n"
                                          "	border-width: 1px; \n"
                                          "	border-style: solid; \n"
                                          "	border-color: #CACACA;\n"
                                          "	border-left-style:none;\n"
                                          "	border-right-style:none;\n"
                                          "}"
                                          "QFrame#card_chat_user:hover {"
                                          " background-color: #BDBDBD"
                                          "}"
                                          "QFrame[pressed=True] {"
                                          " background-color: black"
                                          "}"
                                          "QFrame[pressed=False] {"
                                          " background-color: #DBDBDB"
                                          "}")
        frm_card_chat_user.setFrameShape(QFrame.StyledPanel)
        frm_card_chat_user.setFrameShadow(QFrame.Raised)

        self.lbl_img_user = QLabel(frm_card_chat_user)
        self.lbl_img_user.setObjectName(u"lbl_img_user")
        self.lbl_img_user.setGeometry(QRect(10, 8, 35, 35))
        self.lbl_img_user.setMinimumSize(QSize(35, 35))
        self.lbl_img_user.setMaximumSize(QSize(35, 35))
        self.lbl_img_user.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lbl_img_user.setStyleSheet(u"QLabel {\n"
                                         "  background: transparent;"
                                         "	border-radius: 15px;\n"
                                         "}")
        img = QImage()
        img.load(resource_path(u"../img/profile_user.jpg"), "JPG")
        self.lbl_img_user.resize(img.width(), img.height())
        pixmap = QPixmap(img.width(), img.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        clipPath = QPainterPath()
        clipPath.addRoundedRect(QRectF(img.rect()), img.width() // 2, img.width() // 2)
        painter.setClipPath(clipPath)
        painter.drawPixmap(0, 0, QPixmap(img))
        painter.end()
        self.lbl_img_user.setPixmap(pixmap)
        self.lbl_img_user.setScaledContents(True)
        self.lbl_img_user.setText("")


        self.lbl_name_user = QLabel(frm_card_chat_user)
        self.lbl_name_user.setObjectName(u"lbl_name_user")
        self.lbl_name_user.setGeometry(QRect(50, 8, 141, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.lbl_name_user.setFont(font2)
        self.lbl_name_user.setStyleSheet(u"QLabel {\n"
                                          "  background: transparent;"
                                          "	color: #605D5D;\n"
                                          "}")
        self.lbl_name_user.setText("")

        self.lbl_chat_user = QLabel(frm_card_chat_user)
        self.lbl_chat_user.setObjectName(u"lbl_chat_user")
        self.lbl_chat_user.setGeometry(QRect(52, 25, 141, 16))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.lbl_chat_user.setFont(font3)
        self.lbl_chat_user.setStyleSheet(u"QLabel {\n"
                                          "  background: transparent;"
                                          "	color: #848383;\n"
                                          "}")
        self.lbl_chat_user.setText("")

        self.lbl_user_id = QLabel(frm_card_chat_user)
        self.lbl_user_id.setObjectName(u"lbl_user_id")
        self.lbl_user_id.setEnabled(False)
        self.lbl_user_id.setGeometry(QRect(10, 20, 16, 16))
        self.lbl_user_id.setFont(font3)
        self.lbl_user_id.setStyleSheet(u"QLabel {\n"
                                        "  background: transparent;"
                                        "	color: #848383;\n"
                                        "}")
        self.lbl_user_id.setVisible(False)
        self.lbl_user_id.setText("")





