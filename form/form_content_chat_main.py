# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions.functions import resource_path


class FormChatMainContent(object):

    def setup_frm_chat_main_content(self, frm_content):
        if not frm_content.objectName():
            frm_content.setObjectName(u"frm_content")
        frm_content.resize(683, 565)
        frm_content.setMinimumSize(QSize(682, 561))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        frm_content.setFont(font)
        frm_content.setStyleSheet(u"QFrame#frm_content{\n"
                                   "	background-color:#F5F5F5;\n"
                                   "   border-bottom-right-radius: 15px;"
                                   "}")
        self.vrl_frm_content_department = QVBoxLayout(frm_content)
        self.vrl_frm_content_department.setSpacing(0)
        self.vrl_frm_content_department.setObjectName(u"vrl_frm_content_department")
        self.vrl_frm_content_department.setContentsMargins(0, 0, 0, 0)
        
        self.frm_content_chat_main = QFrame(frm_content)
        self.frm_content_chat_main.setObjectName(u"frm_content_chat_main")
        self.frm_content_chat_main.setMinimumSize(QSize(682, 561))
        self.frm_content_chat_main.setFont(font)
        self.frm_content_chat_main.setFrameShape(QFrame.StyledPanel)
        self.frm_content_chat_main.setFrameShadow(QFrame.Raised)

        self.grl_content_chat_main = QGridLayout(self.frm_content_chat_main)
        self.grl_content_chat_main.setObjectName(u"grl_content_chat_main")

        self.lbl_chat_main = QLabel(self.frm_content_chat_main)
        self.lbl_chat_main.setObjectName(u"lbl_chat_main")
        self.lbl_chat_main.setMinimumSize(QSize(663, 545))
        self.lbl_chat_main.setMaximumSize(QSize(663, 545))
        self.lbl_chat_main.setPixmap(QPixmap(resource_path(u"../img/chat.png")))
        self.lbl_chat_main.setScaledContents(True)

        self.grl_content_chat_main.addWidget(self.lbl_chat_main, 1, 1, 1, 1)

        self.hls_between_border_right_and_label_chat_main = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_chat_main.addItem(self.hls_between_border_right_and_label_chat_main, 1, 2, 1, 1)

        self.vls_between_border_top_and_label_chat_main = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_content_chat_main.addItem(self.vls_between_border_top_and_label_chat_main, 0, 1, 1, 1)

        self.hls_between_border_left_and_label_chat_main = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_chat_main.addItem(self.hls_between_border_left_and_label_chat_main, 1, 0, 1, 1)

        self.vls_between_border_bottom_and_label_chat_main = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_content_chat_main.addItem(self.vls_between_border_bottom_and_label_chat_main, 2, 1, 1, 1)

        self.vrl_frm_content_department.addWidget(self.frm_content_chat_main)

        self.retranslate_frm_chat_main_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_chat_main_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Chat", None))
        self.lbl_chat_main.setText("")
    # retranslateUi

