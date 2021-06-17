# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions.functions import resource_path


class FormTicketsContent(object):

    def setup_frm_tickets_content(self, frm_content):
        if not frm_content.objectName():
            frm_content.setObjectName(u"frm_content")
        frm_content.resize(683, 565)
        frm_content.setMinimumSize(QSize(682, 561))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        frm_content.setFont(font)
        frm_content.setStyleSheet(u"QFrame#frm_content{\n"
                                   "	background-color:#F5F5F5;\n"
                                   "	border-bottom-right-radius: 15px;\n"
                                   "}")

        self.vrl_frm_content_tickets = QVBoxLayout(frm_content)
        self.vrl_frm_content_tickets.setSpacing(0)
        self.vrl_frm_content_tickets.setObjectName(u"vrl_frm_content_tickets")
        self.vrl_frm_content_tickets.setContentsMargins(0, 0, 0, 0)

        self.frm_content_tickets = QFrame(frm_content)
        self.frm_content_tickets.setObjectName(u"frm_content_tickets")
        self.frm_content_tickets.setMinimumSize(QSize(682, 561))
        self.frm_content_tickets.setFont(font)
        self.frm_content_tickets.setFrameShape(QFrame.StyledPanel)
        self.frm_content_tickets.setFrameShadow(QFrame.Raised)

        self.vrl_content_tickets = QVBoxLayout(self.frm_content_tickets)
        self.vrl_content_tickets.setObjectName(u"vrl_content_tickets")

        self.frm_content_button_tickets = QFrame(self.frm_content_tickets)
        self.frm_content_button_tickets.setObjectName(u"frm_content_button_tickets")
        self.frm_content_button_tickets.setMinimumSize(QSize(661, 41))
        self.frm_content_button_tickets.setMaximumSize(QSize(16777215, 41))
        self.frm_content_button_tickets.setFrameShape(QFrame.StyledPanel)
        self.frm_content_button_tickets.setFrameShadow(QFrame.Raised)

        self.hzl_content_button_tickets = QHBoxLayout(self.frm_content_button_tickets)
        self.hzl_content_button_tickets.setSpacing(10)
        self.hzl_content_button_tickets.setObjectName(u"hzl_content_button_tickets")
        self.hzl_content_button_tickets.setContentsMargins(15, 0, 15, 0)

        self.hls_between_boder_left_and_buttons_tickets = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hzl_content_button_tickets.addItem(self.hls_between_boder_left_and_buttons_tickets)

        self.btn_add_tickets = QPushButton(self.frm_content_button_tickets)
        self.btn_add_tickets.setObjectName(u"btn_add_tickets")
        self.btn_add_tickets.setEnabled(True)
        self.btn_add_tickets.setMinimumSize(QSize(75, 23))
        self.btn_add_tickets.setMaximumSize(QSize(75, 23))
        self.btn_add_tickets.setStyleSheet(u"QPushButton#btn_add_tickets {\n"
                                            "	background-color: #2FB7F3;\n"
                                            "	color: white;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton#btn_add_tickets:hover {\n"
                                            "	background-color:#009CE1;\n"
                                            "}\n"
                                            "QPushButton#btn_add_tickets:pressed {\n"
                                            "	background-color:#0082BC;\n"
                                            "}\n"
                                            "QPushButton#btn_add_tickets:disabled {\n"
                                            "	background-color:  #BFBFBF;\n"
                                            "	color: #6a6767;\n"
                                            "}")
        icon = QIcon()
        icon.addFile(resource_path(u"../img/plus-2-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_tickets.setIcon(icon)
        self.btn_add_tickets.setIconSize(QSize(10, 10))

        self.hzl_content_button_tickets.addWidget(self.btn_add_tickets)

        self.btn_report_tickets = QPushButton(self.frm_content_button_tickets)
        self.btn_report_tickets.setObjectName(u"btn_report_tickets")
        self.btn_report_tickets.setEnabled(True)
        self.btn_report_tickets.setMinimumSize(QSize(75, 23))
        self.btn_report_tickets.setMaximumSize(QSize(75, 23))
        self.btn_report_tickets.setStyleSheet(u"QPushButton#btn_report_tickets {\n"
                                               "	background-color: #2FB7F3;\n"
                                               "	color: white;\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton#btn_report_tickets:hover {\n"
                                               "	background-color:#009CE1;\n"
                                               "}\n"
                                               "QPushButton#btn_report_tickets:pressed {\n"
                                               "	background-color:#0082BC;\n"
                                               "}\n"
                                               "QPushButton#btn_report_tickets:disabled {\n"
                                               "	background-color:  #BFBFBF;\n"
                                               "	color: #6a6767;\n"
                                               "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/report.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report_tickets.setIcon(icon1)
        self.btn_report_tickets.setIconSize(QSize(16, 16))

        self.hzl_content_button_tickets.addWidget(self.btn_report_tickets)

        self.hls_between_button_report_and_logs_tickets = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_tickets.addItem(self.hls_between_button_report_and_logs_tickets)

        self.btn_log_tickets = QPushButton(self.frm_content_button_tickets)
        self.btn_log_tickets.setObjectName(u"btn_log_tickets")
        self.btn_log_tickets.setMinimumSize(QSize(75, 23))
        self.btn_log_tickets.setMaximumSize(QSize(75, 23))
        self.btn_log_tickets.setStyleSheet(u"QPushButton#btn_log_tickets {\n"
                                            "	background-color: #A9A9AC;\n"
                                            "	color: white;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton#btn_log_tickets:hover {\n"
                                            "	background-color:#97979B;\n"
                                            "}\n"
                                            "QPushButton#btn_log_tickets:pressed {\n"
                                            "	background-color:#8A8A8E;\n"
                                            "}\n"
                                            "QPushButton#btn_log_tickets:disabled {\n"
                                            "	background-color:  #BFBFBF;\n"
                                            "	color: #6a6767;\n"
                                            "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"../img/log.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_log_tickets.setIcon(icon2)

        self.hzl_content_button_tickets.addWidget(self.btn_log_tickets)

        self.hls_between_button_and_border_right_tickets = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hzl_content_button_tickets.addItem(self.hls_between_button_and_border_right_tickets)

        self.vrl_content_tickets.addWidget(self.frm_content_button_tickets)

        self.frm_content_fields_tickets = QFrame(self.frm_content_tickets)
        self.frm_content_fields_tickets.setObjectName(u"frm_content_fields_tickets")
        self.frm_content_fields_tickets.setMinimumSize(QSize(662, 501))
        self.frm_content_fields_tickets.setFont(font)
        self.frm_content_fields_tickets.setStyleSheet(u"QHeaderView::section {\n"
                                                       "	background-color: white;\n"
                                                       "	color: gray;\n"
                                                       "	padding: 2px;\n"
                                                       "	font-size: 10pt;\n"
                                                       "	font-weight: bold;\n"
                                                       "	border-style: none;\n"
                                                       "	text-transform: uppercase\n"
                                                       "}\n"
                                                       "QHeaderView::section:horizontal {\n"
                                                       "    border-top: 1px solid #DFDFDF;\n"
                                                       "	border-bottom:1px solid #DFDFDF;\n"
                                                       "}")
        self.frm_content_fields_tickets.setFrameShape(QFrame.StyledPanel)
        self.frm_content_fields_tickets.setFrameShadow(QFrame.Raised)

        self.hzl_content_fields_tickets = QHBoxLayout(self.frm_content_fields_tickets)
        self.hzl_content_fields_tickets.setObjectName(u"hzl_content_fields_tickets")

        self.hls_between__borde_left_and_table_tickets = QSpacerItem(4, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hzl_content_fields_tickets.addItem(self.hls_between__borde_left_and_table_tickets)

        self.tab_tickets = QTableWidget(self.frm_content_fields_tickets)
        self.tab_tickets.setObjectName(u"tab_tickets")
        self.tab_tickets.setMinimumSize(QSize(642, 481))
        self.tab_tickets.setStyleSheet(u"QTableWidget {\n"
                                        "	background: white;\n"
                                        "	border-style: none;\n"
                                        "}\n"
                                        "QTableWidget::item {\n"
                                        "	Border-bottom:1px solid #EEF1F7;\n"
                                        "}\n")
        self.tab_tickets.setFrameShape(QFrame.NoFrame)
        self.tab_tickets.setFrameShadow(QFrame.Plain)
        self.tab_tickets.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_tickets.setSelectionMode(QAbstractItemView.NoSelection)
        self.tab_tickets.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_tickets.setShowGrid(False)
        self.tab_tickets.setGridStyle(Qt.NoPen)
        self.tab_tickets.setWordWrap(False)
        self.tab_tickets.horizontalHeader().setHighlightSections(False)
        # self.tab_tickets.horizontalHeader().setStretchLastSection(True)
        self.tab_tickets.verticalHeader().setVisible(False)
        self.tab_tickets.setColumnCount(11)
        id_ticket = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(0, id_ticket)
        user_created = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(1, user_created)
        title_ticket = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(2, title_ticket)
        department = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(3, department)
        user_following = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(4, user_following)
        priority = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(5, priority)
        status = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(6, status)
        reply_to = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(7, reply_to)
        edit_ticket = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(8, edit_ticket)
        delete_ticket = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(9, delete_ticket)
        view_ticket = QTableWidgetItem()
        self.tab_tickets.setHorizontalHeaderItem(10, view_ticket)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(0, 70)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(1, 300)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tab_tickets.setColumnWidth(2, 300)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(3, 157)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(4, 300)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(5, 100)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(6, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(6, 90)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(7, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(7, 80)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(8, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(8, 70)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(9, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(9, 70)
        self.tab_tickets.horizontalHeader().setSectionResizeMode(10, QHeaderView.Fixed)
        self.tab_tickets.setColumnWidth(10, 85)

        self.hzl_content_fields_tickets.addWidget(self.tab_tickets)

        self.hls_between_table_and_borde_right_tickets = QSpacerItem(4, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hzl_content_fields_tickets.addItem(self.hls_between_table_and_borde_right_tickets)

        self.vrl_content_tickets.addWidget(self.frm_content_fields_tickets)

        self.vrl_frm_content_tickets.addWidget(self.frm_content_tickets)

        self.retranslate_frm_tickets_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_tickets_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Tickets", None))
        self.btn_add_tickets.setText(QCoreApplication.translate("frm_content", u"Incluir", None))
        self.btn_report_tickets.setText(QCoreApplication.translate("frm_content", u"Relat\u00f3rio", None))
        self.btn_log_tickets.setText(QCoreApplication.translate("frm_content", u"Logs", None))
        id_ticket = self.tab_tickets.horizontalHeaderItem(0)
        id_ticket.setText(QCoreApplication.translate("frm_content", u"ID", None))
        user_created = self.tab_tickets.horizontalHeaderItem(1)
        user_created.setText(QCoreApplication.translate("frm_content", u"Criado Por", None))
        title_ticket = self.tab_tickets.horizontalHeaderItem(2)
        title_ticket.setText(QCoreApplication.translate("frm_content", u"Titulo", None))
        department = self.tab_tickets.horizontalHeaderItem(3)
        department.setText(QCoreApplication.translate("frm_content", u"Departamento", None))
        user_following = self.tab_tickets.horizontalHeaderItem(4)
        user_following.setText(QCoreApplication.translate("frm_content", u"Acompanhado Por", None))
        priority = self.tab_tickets.horizontalHeaderItem(5)
        priority.setText(QCoreApplication.translate("frm_content", u"Prioridade", None))
        status = self.tab_tickets.horizontalHeaderItem(6)
        status.setText(QCoreApplication.translate("frm_content", u"Status", None))
        reply_to = self.tab_tickets.horizontalHeaderItem(7)
        reply_to.setText(QCoreApplication.translate("frm_content", u"Responder", None))
        edit_ticket = self.tab_tickets.horizontalHeaderItem(8)
        edit_ticket.setText(QCoreApplication.translate("frm_content", u"Editar", None))
        delete_ticket = self.tab_tickets.horizontalHeaderItem(9)
        delete_ticket.setText(QCoreApplication.translate("frm_content", u"Deletar", None))
        view_ticket = self.tab_tickets.horizontalHeaderItem(10)
        view_ticket.setText(QCoreApplication.translate("frm_content", u"Visualizar", None))
    # retranslateUi

