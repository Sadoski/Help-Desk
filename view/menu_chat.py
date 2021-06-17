# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da menu de Chats
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_menu_chat import FormChatMenu
from functions.functions import clear_layout
from view.card_chat_user import CardChatUser
from view.content_chat_main import ChatMainContent


class ChatMenu(FormChatMenu, ChatMainContent):

    def set_form_chat_menu(self, frame: QFrame):
        super(ChatMenu, self).setup_frm_chat_menu(frame)
        self.chat_main_content()
        self.card_chat_user()

    def chat_main_content(self):
        """
        Metodo para visualizar o formulario inicial do chat
        """
        clear_layout(self.main.grl_content)
        self.set_form_chat_main_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_chat_main)

    def card_chat_user(self):
        user = ("1", "Jefferson A. Sadoski", "Oi, tudo bem com você...")
        for card_user in range(15):
            id_user = user[0]
            name = user[1]
            chat = user[2]
            card_user = CardChatUser()
            card_user.card_user.lbl_user_id.setText(id_user)
            card_user.card_user.lbl_name_user.setText(name)
            card_user.card_user.lbl_chat_user.setText(chat)
            self.vrl_user_chat.addWidget(card_user)
        self.vrl_user_chat.addItem(self.vsl_between_user_and_border)




