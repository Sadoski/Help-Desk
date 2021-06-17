# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo dos Departamento
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_department import FormDepartmentContent


class DepartmentContent(FormDepartmentContent):

    def set_form_department_content(self, frame: QFrame):
        super(DepartmentContent, self).setup_frm_department_content(frame)
        self.main.lbl_title.setText("Departamento")
