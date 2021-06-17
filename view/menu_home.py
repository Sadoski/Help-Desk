# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da menu Inicial
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_menu_home import FormHomeMenu


class HomeMenu(FormHomeMenu):

    def set_form_home_menu(self, frame: QFrame):
        super(HomeMenu, self).setup_frm_home_menu(frame)

