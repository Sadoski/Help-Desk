# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo das configurações de perfil
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_profile import FormProfileContent


class ProfileContent(FormProfileContent):

    def set_form_profile_content(self, frame: QFrame):
        super(ProfileContent, self).setup_frm_profile_content(frame)
        self.main.lbl_title.setText("Perfil")
