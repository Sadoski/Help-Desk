# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da menu de Help
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_menu_help import FormHelpMenu


class HelpMenu(FormHelpMenu):

    def set_form_help_menu(self, frame: QFrame):
        super(HelpMenu, self).setup_frm_help_menu(frame)