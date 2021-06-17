# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da menu de Settings
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_menu_settings import FormSettingsMenu
from functions.functions import clear_layout
from view.content_department import DepartmentContent
from view.content_profile import ProfileContent
from view.content_tags import TagsContent
from view.content_user import UserContent


class SettingsMenu(FormSettingsMenu, ProfileContent, UserContent, TagsContent, DepartmentContent):

    def set_form_settings_menu(self, frame: QFrame):
        super(SettingsMenu, self).setup_frm_settings_menu(frame)
        self.profile_content()

        self.btn_profile.clicked.connect(self.profile_content)
        self.btn_user.clicked.connect(self.user_content)
        self.btn_department.clicked.connect(self.department_content)
        self.btn_tags.clicked.connect(self.tags_content)

    def profile_content(self):
        """
        Metodo para visualizar o formulario conteudo de atualização e visualizaçãoc do perfil do usuário
        """
        clear_layout(self.main.grl_content)
        self.set_form_profile_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_profile)

    def user_content(self):
        """
        Metodo para visualizar o formulario de cadastro, atualização, deleção e visualização de usuários
        """
        clear_layout(self.main.grl_content)
        self.set_form_user_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_user)

    def department_content(self):
        """
        Metodo para visualizar o formulario de cadastro, atualização, deleção e visualização de usuários
        """
        clear_layout(self.main.grl_content)
        self.set_form_department_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_department)

    def tags_content(self):
        """
        Metodo para visualizar o formulario de cadastro, atualização, deleção e visualização de usuários
        """
        clear_layout(self.main.grl_content)
        self.set_form_tags_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_tags)