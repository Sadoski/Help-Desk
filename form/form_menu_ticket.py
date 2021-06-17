# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormTicketMenu(object):

    def setup_frm_ticket_menu(self, frm_menu):
        if not frm_menu.objectName():
            frm_menu.setObjectName(u"frm_menu")
        frm_menu.resize(200, 563)
        frm_menu.setMinimumSize(QSize(200, 563))
        frm_menu.setMaximumSize(QSize(200, 16777215))
        frm_menu.setStyleSheet(u"QFrame#frm_menu {\n"
                                "	background-color: #DBDBDB;\n"
                                "}")

        self.vrl_ticket_menu = QVBoxLayout(frm_menu)
        self.vrl_ticket_menu.setSpacing(0)
        self.vrl_ticket_menu.setObjectName(u"vrl_ticket_menu")
        self.vrl_ticket_menu.setContentsMargins(0, 0, 0, 0)

        self.frm_ticket_menu = QFrame(frm_menu)
        self.frm_ticket_menu.setObjectName(u"frm_ticket_menu")
        self.frm_ticket_menu.setMinimumSize(QSize(200, 563))
        self.frm_ticket_menu.setMaximumSize(QSize(200, 16777215))
        self.frm_ticket_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_ticket_menu.setFrameShadow(QFrame.Raised)

        self.btn_training = QPushButton(self.frm_ticket_menu)
        self.btn_training.setObjectName(u"btn_training")
        self.btn_training.setGeometry(QRect(0, 439, 200, 30))
        self.btn_training.setMinimumSize(QSize(200, 30))
        self.btn_training.setMaximumSize(QSize(200, 30))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_training.setFont(font)
        self.btn_training.setStyleSheet(u"QPushButton#btn_training {\n"
                                         "	text-align:left;\n"
                                         "	text-decoration: none;\n"
                                         "	margin-left: 20px;\n"
                                          "	border: none;\n"
                                         "	color: #555555;\n"
                                         "}\n"
                                          "QPushButton#btn_training:hover {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                          "QPushButton#btn_training:pressed {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                          "QPushButton#btn_training:focus {\n"
                                         "    color: #00B1FF;\n"
                                         "	text-decoration: underline;\n"
                                         "}")
        self.btn_training.setIconSize(QSize(0, 0))

        self.txt_search = QLineEdit(self.frm_ticket_menu)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setGeometry(QRect(9, 10, 181, 28))
        self.txt_search.setMinimumSize(QSize(181, 28))
        self.txt_search.setMaximumSize(QSize(181, 28))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.txt_search.setFont(font1)
        self.txt_search.setFocusPolicy(Qt.ClickFocus)
        self.txt_search.setStyleSheet(u"QLineEdit#txt_search {\n"
                                       "	background-color: #F1F1F1;\n"
                                       "	color: #8C8C8C;\n"
                                       "	border: 1px solid #AFAEAE;\n"
                                       "	border-radius: 5px;\n"
                                       "}")
        self.txt_search.setMaxLength(40)

        self.btn_my_tickets = QPushButton(self.frm_ticket_menu)
        self.btn_my_tickets.setObjectName(u"btn_my_tickets")
        self.btn_my_tickets.setGeometry(QRect(0, 99, 200, 30))
        self.btn_my_tickets.setMinimumSize(QSize(200, 30))
        self.btn_my_tickets.setMaximumSize(QSize(200, 30))
        self.btn_my_tickets.setFont(font)
        self.btn_my_tickets.setStyleSheet(u"QPushButton#btn_my_tickets {\n"
                                           "	text-align:left;\n"
                                           "	text-decoration: none;\n"
                                           "	margin-left: 20px;\n"
                                           "	border: none;\n"
                                           "	color: #555555;\n"
                                           "}\n"
                                           "QPushButton#btn_my_tickets:hover {\n"
                                           "	color: #00B1FF;\n"
                                           "	text-decoration: none;\n"
                                           "}\n"
                                           "QPushButton#btn_my_tickets:pressed {\n"
                                           "	color: #00B1FF;\n"
                                           "	text-decoration: none;\n"
                                           "}\n"
                                           "QPushButton#btn_my_tickets:focus {\n"
                                           "    color: #00B1FF;\n"
                                           "	text-decoration: underline;\n"
                                           "}")
        self.btn_my_tickets.setIconSize(QSize(0, 0))

        self.btn_solved = QPushButton(self.frm_ticket_menu)
        self.btn_solved.setObjectName(u"btn_solved")
        self.btn_solved.setGeometry(QRect(0, 299, 200, 30))
        self.btn_solved.setMinimumSize(QSize(200, 30))
        self.btn_solved.setMaximumSize(QSize(200, 30))
        self.btn_solved.setFont(font)
        self.btn_solved.setStyleSheet(u"QPushButton#btn_solved {\n"
                                       "	text-align:left;\n"
                                       "	text-decoration: none;\n"
                                       "	margin-left: 20px;\n"
                                       "	border: none;\n"
                                       "	color: #555555;\n"
                                       "}\n"
                                       "QPushButton#btn_solved:hover {\n"
                                       "	color: #00B1FF;\n"
                                       "	text-decoration: none;\n"
                                       "}\n"
                                       "QPushButton#btn_solved:pressed {\n"
                                       "	color: #00B1FF;\n"
                                       "	text-decoration: none;\n"
                                       "}\n"
                                       "QPushButton#btn_solved:focus {\n"
                                       "    color: #00B1FF;\n"
                                       "	text-decoration: underline;\n"
                                       "}")
        self.btn_solved.setIconSize(QSize(0, 0))

        self.btn_recent = QPushButton(self.frm_ticket_menu)
        self.btn_recent.setObjectName(u"btn_recent")
        self.btn_recent.setGeometry(QRect(0, 129, 200, 30))
        self.btn_recent.setMinimumSize(QSize(200, 30))
        self.btn_recent.setMaximumSize(QSize(200, 30))
        self.btn_recent.setFont(font)
        self.btn_recent.setStyleSheet(u"QPushButton#btn_recent {\n"
                                       "	text-align:left;\n"
                                       "	text-decoration: none;\n"
                                       "	margin-left: 20px;\n"
                                       "	border: none;\n"
                                       "	color: #555555;\n"
                                       "}\n"
                                       "QPushButton#btn_recent:hover {\n"
                                       "	color: #00B1FF;\n"
                                       "	text-decoration: none;\n"
                                       "}\n"
                                       "QPushButton#btn_recent:pressed {\n"
                                       "	color: #00B1FF;\n"
                                       "	text-decoration: none;\n"
                                       "}\n"
                                       "QPushButton#btn_recent:focus {\n"
                                       "    color: #00B1FF;\n"
                                       "	text-decoration: underline;\n"
                                       "}")
        self.btn_recent.setIconSize(QSize(0, 0))

        self.lbl_status = QLabel(self.frm_ticket_menu)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setGeometry(QRect(20, 179, 71, 16))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.lbl_status.setFont(font2)
        self.lbl_status.setStyleSheet(u"QLabel#lbl_status {\n"
                                       "	color: #909090;\n"
                                       "}")

        self.btn_closed = QPushButton(self.frm_ticket_menu)
        self.btn_closed.setObjectName(u"btn_closed")
        self.btn_closed.setGeometry(QRect(0, 329, 200, 30))
        self.btn_closed.setMinimumSize(QSize(200, 30))
        self.btn_closed.setMaximumSize(QSize(200, 30))
        self.btn_closed.setFont(font)
        self.btn_closed.setStyleSheet(u"QPushButton#btn_closed {\n"
                                       "	text-align:left;\n"
                                       "	text-decoration: none;\n"
                                       "	margin-left: 20px;\n"
                                       "	border: none;\n"
                                       "	color: #555555;\n"
                                       "}\n"
                                       "QPushButton#btn_closed:hover {\n"
                                       "	color: #00B1FF;\n"
                                       "	text-decoration: none;\n"
                                       "}\n"
                                       "QPushButton#btn_closed:pressed {\n"
                                       "	color: #00B1FF;\n"
                                       "	text-decoration: none;\n"
                                       "}\n"
                                       "QPushButton#btn_closed:focus {\n"
                                       "    color: #00B1FF;\n"
                                       "	text-decoration: underline;\n"
                                       "}")
        self.btn_closed.setIconSize(QSize(0, 0))

        self.btn_all_ticket = QPushButton(self.frm_ticket_menu)
        self.btn_all_ticket.setObjectName(u"btn_all_ticket")
        self.btn_all_ticket.setGeometry(QRect(0, 70, 200, 30))
        self.btn_all_ticket.setMinimumSize(QSize(200, 30))
        self.btn_all_ticket.setMaximumSize(QSize(200, 30))
        self.btn_all_ticket.setFont(font)
        self.btn_all_ticket.setStyleSheet(u"QPushButton#btn_all_ticket {\n"
                                           "	text-align:left;\n"
                                           "	text-decoration: none;\n"
                                           "	margin-left: 20px;\n"
                                           "	border: none;\n"
                                           "	color: #555555;\n"
                                           "}\n"
                                           "QPushButton#btn_all_ticket:hover {\n"
                                           "	color: #00B1FF;\n"
                                           "	text-decoration: none;\n"
                                           "}\n"
                                           "QPushButton#btn_all_ticket:pressed {\n"
                                           "	color: #00B1FF;\n"
                                           "	text-decoration: none;\n"
                                           "}\n"
                                           "QPushButton#btn_all_ticket:focus {\n"
                                           "    color: #00B1FF;\n"
                                           "	text-decoration: underline;\n"
                                           "}")
        self.btn_all_ticket.setIconSize(QSize(0, 0))

        self.lbl_category = QLabel(self.frm_ticket_menu)
        self.lbl_category.setObjectName(u"lbl_category")
        self.lbl_category.setGeometry(QRect(20, 379, 71, 16))
        self.lbl_category.setFont(font2)
        self.lbl_category.setStyleSheet(u"QLabel#lbl_category {\n"
                                         "	color: #909090;\n"
                                         "}")

        self.btn_open = QPushButton(self.frm_ticket_menu)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(0, 209, 200, 30))
        self.btn_open.setMinimumSize(QSize(200, 30))
        self.btn_open.setMaximumSize(QSize(200, 30))
        self.btn_open.setFont(font)
        self.btn_open.setStyleSheet(u"QPushButton#btn_open{\n"
                                     "	text-align:left;\n"
                                     "	text-decoration: none;\n"
                                     "	margin-left: 20px;\n"
                                     "	border: none;\n"
                                     "	color: #555555;\n"
                                     "}\n"
                                     "QPushButton#btn_open:hover {\n"
                                     "	color: #00B1FF;\n"
                                     "	text-decoration: none;\n"
                                     "}\n"
                                     "QPushButton#btn_open:pressed {\n"
                                     "	color: #00B1FF;\n"
                                     "	text-decoration: none;\n"
                                     "}\n"
                                     "QPushButton#btn_open:focus {\n"
                                     "    color: #00B1FF;\n"
                                     "	text-decoration: underline;\n"
                                     "}")
        self.btn_open.setIconSize(QSize(0, 0))

        self.btn_on_hold = QPushButton(self.frm_ticket_menu)
        self.btn_on_hold.setObjectName(u"btn_on_hold")
        self.btn_on_hold.setGeometry(QRect(0, 269, 200, 30))
        self.btn_on_hold.setMinimumSize(QSize(200, 30))
        self.btn_on_hold.setMaximumSize(QSize(200, 30))
        self.btn_on_hold.setFont(font)
        self.btn_on_hold.setStyleSheet(u"QPushButton#btn_on_hold {\n"
                                        "	text-align:left;\n"
                                        "	text-decoration: none;\n"
                                        "	margin-left: 20px;\n"
                                        "	border: none;\n"
                                        "	color: #555555;\n"
                                        "}\n"
                                        "QPushButton#btn_on_hold:hover {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_on_hold:pressed {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_on_hold:focus {\n"
                                        "    color: #00B1FF;\n"
                                        "	text-decoration: underline;\n"
                                        "}")
        self.btn_on_hold.setIconSize(QSize(0, 0))

        self.btn_support = QPushButton(self.frm_ticket_menu)
        self.btn_support.setObjectName(u"btn_support")
        self.btn_support.setGeometry(QRect(0, 409, 200, 30))
        self.btn_support.setMinimumSize(QSize(200, 30))
        self.btn_support.setMaximumSize(QSize(200, 30))
        self.btn_support.setFont(font)
        self.btn_support.setStyleSheet(u"QPushButton#btn_support {\n"
                                        "	text-align:left;\n"
                                        "	text-decoration: none;\n"
                                        "	margin-left: 20px;\n"
                                        "	border: none;\n"
                                        "	color: #555555;\n"
                                        "}\n"
                                        "QPushButton#btn_support:hover {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_support:pressed {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_support:focus {\n"
                                        "    color: #00B1FF;\n"
                                        "	text-decoration: underline;\n"
                                        "}")
        self.btn_support.setIconSize(QSize(0, 0))

        self.btn_pending = QPushButton(self.frm_ticket_menu)
        self.btn_pending.setObjectName(u"btn_pending")
        self.btn_pending.setGeometry(QRect(0, 239, 200, 30))
        self.btn_pending.setMinimumSize(QSize(200, 30))
        self.btn_pending.setMaximumSize(QSize(200, 30))
        self.btn_pending.setFont(font)
        self.btn_pending.setStyleSheet(u"QPushButton#btn_pending {\n"
                                        "	text-align:left;\n"
                                        "	text-decoration: none;\n"
                                        "	margin-left: 20px;\n"
                                        "	border: none;\n"
                                        "	color: #555555;\n"
                                        "}\n"
                                        "QPushButton#btn_pending:hover {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_pending:pressed {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_pending:focus {\n"
                                        "    color: #00B1FF;\n"
                                        "	text-decoration: underline;\n"
                                        "}")
        self.btn_pending.setIconSize(QSize(0, 0))

        self.vrl_ticket_menu.addWidget(self.frm_ticket_menu)

        self.retranslate_ticket_menu(frm_menu)

        QMetaObject.connectSlotsByName(frm_menu)

    def retranslate_ticket_menu(self, frm_menu):
        frm_menu.setWindowTitle("")
        self.btn_training.setText(QCoreApplication.translate("frm_menu", u"Treinamento", None))
        self.txt_search.setStatusTip(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setWhatsThis(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setAccessibleName(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setAccessibleDescription(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search.setText("")
        self.txt_search.setPlaceholderText(QCoreApplication.translate("frm_menu", u" Pesquisar", None))
        self.btn_my_tickets.setText(QCoreApplication.translate("frm_menu", u"Meus Tickets", None))
        self.btn_solved.setText(QCoreApplication.translate("frm_menu", u"Resolvido", None))
        self.btn_recent.setText(QCoreApplication.translate("frm_menu", u"Recentes", None))
        self.lbl_status.setText(QCoreApplication.translate("frm_menu", u"STATUS", None))
        self.btn_closed.setText(QCoreApplication.translate("frm_menu", u"Fechado", None))
        self.btn_all_ticket.setText(QCoreApplication.translate("frm_menu", u"Todos Tickets", None))
        self.lbl_category.setText(QCoreApplication.translate("frm_menu", u"CATEGORIA", None))
        self.btn_open.setText(QCoreApplication.translate("frm_menu", u"Aberto", None))
        self.btn_on_hold.setText(QCoreApplication.translate("frm_menu", u"Em Espera", None))
        self.btn_support.setText(QCoreApplication.translate("frm_menu", u"Suporte", None))
        self.btn_pending.setText(QCoreApplication.translate("frm_menu", u"Pedente", None))

