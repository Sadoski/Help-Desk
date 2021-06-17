# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da menu de Tickets
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_menu_ticket import FormTicketMenu
from functions.functions import clear_layout
from view.content_tickets import TicketsContent


class TicketMenu(FormTicketMenu, TicketsContent):

    def set_form_ticket_menu(self, frame: QFrame):
        super(TicketMenu, self).setup_frm_ticket_menu(frame)
        self.tickets_content()

        self.btn_all_ticket.clicked.connect(self.tickets_content)

    def tickets_content(self):
        """
        Metodo para visualizar o formulario conteudo de atualização e visualizaçãoc do perfil do usuário
        """
        clear_layout(self.main.grl_content)
        self.set_form_ticket_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_tickets)