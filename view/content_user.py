# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo das configurações de perfil
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_user import FormUserContent


class UserContent(FormUserContent):

    def set_form_user_content(self, frame: QFrame):
        super(UserContent, self).setup_frm_user_content(frame)
        self.main.lbl_title.setText("Usuário")