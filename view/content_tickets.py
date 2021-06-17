
# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo das Tags
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_tickets import FormTicketsContent


class TicketsContent(FormTicketsContent):

    def set_form_ticket_content(self, frame: QFrame):
        super(TicketsContent, self).setup_frm_tickets_content(frame)
        self.main.lbl_title.setText("Tickets")

        self.btn_add_tickets.clicked.connect(self.create_ticket)