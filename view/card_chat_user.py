# -*- coding: utf-8 -*-
"""
Modulo de visualição do card do usuário no chat
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_card_chat_user import FormCardChatUser
from functions.functions import resource_path


class CardChatUser(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.card_user = FormCardChatUser()
        self.card_user.setup_frm_card_chat_user(self)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            print("Esquerdo")
        elif event.button() == Qt.RightButton:
            print("Direito")
        else:
            pass

