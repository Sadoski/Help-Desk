# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da corpo principal do sistema
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_main import FormMain
from functions.functions import clear_layout, resource_path
from view.content_profile import ProfileContent
from view.create_ticket import CreateTicketContent
from view.menu_chat import ChatMenu
from view.menu_help import HelpMenu
from view.menu_home import HomeMenu
from view.menu_settings import SettingsMenu
from view.menu_ticket import TicketMenu


class Main(QMainWindow, HomeMenu, TicketMenu, ChatMenu, SettingsMenu, HelpMenu, CreateTicketContent):
    """
    Classe da visualização da janela principal da aplicação.
    Herança:
        - QMainWindow: classe pradrão do biblioteca PySide2 responsavel pela janela gráfica principal.
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.main = FormMain()
        self.main.setupUi(self)

        # Bloco de eventos ao clicar no botão de controle do formulário
        self.main.btn_close.clicked.connect(self.close)
        self.main.btn_maximize_and_restore.clicked.connect(self.maximize_and_restore)
        self.main.btn_minimize.clicked.connect(self.showMinimized)

        # Bloco de eventos ao clicar no botão de controle do menu principal
        self.main.btn_home.clicked.connect(self.home_menu)
        self.main.btn_help_desk.clicked.connect(self.ticket_menu)
        self.main.btn_chat.clicked.connect(self.chat_menu)
        self.main.btn_settings.clicked.connect(self.settings_menu)
        self.main.btn_help.clicked.connect(self.help_menu)

        self.main.btn_new_ticket.clicked.connect(self.create_ticket)

        def moveWindow(event: QMouseEvent):
            """
            Metodo de evento da ação de mover o formulário
            Parâmetro:
                - event: evento do mouse no formulário
            """
            if event.buttons() == Qt.LeftButton:
                delta = QPoint(event.globalPos() - self.old_pos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.old_pos = event.globalPos()

        # Designar que o campo do formulário ao ser selecionado possa mover o formulário
        self.main.frm_header_content.mouseMoveEvent = moveWindow
        self.main.frm_top_menu.mouseMoveEvent = moveWindow

        # Iniciar o menu Home
        self.home_menu()

    def mousePressEvent(self, event: QMouseEvent):
        """
        Metodo de evento para capturar posição onde o mouse clicou
        Parâmetro:
            - event: evento do mouse no formulário
        """
        self.old_pos = event.globalPos()

    def maximize_and_restore(self):
        """
        Metodo para Maximizar a janela da aplicação restar para o tamnaho normal
        """
        if self.isMaximized():
            self.showNormal()
            maximize = QIcon()
            maximize.addFile(resource_path("..\img\window-maximize.png"), QSize(), QIcon.Normal,
                                           QIcon.Off)
            self.main.btn_maximize_and_restore.setIcon(maximize)
        else:
            self.showMaximized()
            rest_maximize = QIcon()
            rest_maximize.addFile(resource_path("..\img\window-restore.png"), QSize(), QIcon.Normal,
                                                QIcon.Off)
            self.main.btn_maximize_and_restore.setIcon(rest_maximize)

    def home_menu(self):
        """
        Metodo para visualizar as opções do menu inicial
        """
        clear_layout(self.main.vrl_main_menu)
        self.set_form_home_menu(self.main.frm_menu)
        self.main.vrl_main_menu.addWidget(self.frm_home_menu)

    def ticket_menu(self):
        """
        Metodo para visualizar as opções do menu ticket
        """
        clear_layout(self.main.vrl_main_menu)
        self.set_form_ticket_menu(self.main.frm_menu)
        self.main.vrl_main_menu.addWidget(self.frm_ticket_menu)

    def chat_menu(self):
        """
        Metodo para visualizar as opções do menu chat
        """
        clear_layout(self.main.vrl_main_menu)
        self.set_form_chat_menu(self.main.frm_menu)
        self.main.vrl_main_menu.addWidget(self.frm_chat_menu)

    def settings_menu(self):
        """
        Metodo para visualizar as opções do menu settings
        """
        clear_layout(self.main.vrl_main_menu)
        self.set_form_settings_menu(self.main.frm_menu)
        self.main.vrl_main_menu.addWidget(self.frm_settings_menu)

    def help_menu(self):
        """
        Metodo para visualizar as opções do menu help
        """
        clear_layout(self.main.vrl_main_menu)
        self.set_form_help_menu(self.main.frm_menu)
        self.main.vrl_main_menu.addWidget(self.frm_help_menu)

    def create_ticket(self):
        """
        Metodo para visualizar as opções do menu help
        """
        clear_layout(self.main.grl_content)
        self.set_form_create_ticket_content(self.main.frm_content)
        self.main.grl_content.addWidget(self.frm_content_ticket_message)