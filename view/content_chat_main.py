# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo das Tags
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_chat_main import FormChatMainContent


class ChatMainContent(FormChatMainContent):

    def set_form_chat_main_content(self, frame: QFrame):
        super(ChatMainContent, self).setup_frm_chat_main_content(frame)
        self.main.lbl_title.setText("Chat")

