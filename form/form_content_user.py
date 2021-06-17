# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions.functions import resource_path


class FormUserContent(object):

    def setup_frm_user_content(self, frm_content):
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
                                   "   border-bottom-right-radius: 15px;"
                                   "}")

        self.vrl_frm_content_user = QVBoxLayout(frm_content)
        self.vrl_frm_content_user.setSpacing(0)
        self.vrl_frm_content_user.setObjectName(u"vrl_frm_content_user")
        self.vrl_frm_content_user.setContentsMargins(0, 0, 0, 0)

        self.frm_content_user = QFrame(frm_content)
        self.frm_content_user.setObjectName(u"frm_content_user")
        self.frm_content_user.setMinimumSize(QSize(682, 561))
        self.frm_content_user.setFont(font)
        self.frm_content_user.setFrameShape(QFrame.StyledPanel)
        self.frm_content_user.setFrameShadow(QFrame.Raised)

        self.vrl_content_user = QVBoxLayout(self.frm_content_user)
        self.vrl_content_user.setObjectName(u"vrl_content_user")

        self.frm_content_button_user = QFrame(self.frm_content_user)
        self.frm_content_button_user.setObjectName(u"frm_content_button_user")
        self.frm_content_button_user.setMinimumSize(QSize(661, 41))
        self.frm_content_button_user.setMaximumSize(QSize(16777215, 41))
        self.frm_content_button_user.setFrameShape(QFrame.StyledPanel)
        self.frm_content_button_user.setFrameShadow(QFrame.Raised)

        self.hzl_content_button_user = QHBoxLayout(self.frm_content_button_user)
        self.hzl_content_button_user.setSpacing(10)
        self.hzl_content_button_user.setObjectName(u"hzl_content_button_user")
        self.hzl_content_button_user.setContentsMargins(15, 0, 15, 0)

        self.hls_between_boder_left_and_buttons_user = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_user.addItem(self.hls_between_boder_left_and_buttons_user)

        self.btn_new_user = QPushButton(self.frm_content_button_user)
        self.btn_new_user.setObjectName(u"btn_new_user")
        self.btn_new_user.setEnabled(True)
        self.btn_new_user.setMinimumSize(QSize(75, 23))
        self.btn_new_user.setMaximumSize(QSize(75, 23))
        self.btn_new_user.setStyleSheet(u"QPushButton#btn_new_user {\n"
                                         "	background-color: #2FB7F3;\n"
                                         "	color: white;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton#btn_new_user:hover {\n"
                                         "	background-color:#009CE1;\n"
                                         "}\n"
                                         "QPushButton#btn_new_user:pressed {\n"
                                         "	background-color:#0082BC;\n"
                                         "}\n"
                                         "QPushButton#btn_new_user:disabled {\n"
                                         "	background-color:  #BFBFBF;\n"
                                         "	color: #6a6767;\n"
                                         "}")
        icon = QIcon()
        icon.addFile(resource_path(u"../img/plus-2-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_user.setIcon(icon)
        self.btn_new_user.setIconSize(QSize(10, 10))

        self.hzl_content_button_user.addWidget(self.btn_new_user)

        self.btn_report_user = QPushButton(self.frm_content_button_user)
        self.btn_report_user.setObjectName(u"btn_report_user")
        self.btn_report_user.setEnabled(True)
        self.btn_report_user.setMinimumSize(QSize(75, 23))
        self.btn_report_user.setMaximumSize(QSize(75, 23))
        self.btn_report_user.setStyleSheet(u"QPushButton#btn_report_user {\n"
                                            "	background-color: #2FB7F3;\n"
                                            "	color: white;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton#btn_report_user:hover {\n"
                                            "	background-color:#009CE1;\n"
                                            "}\n"
                                            "QPushButton#btn_report_user:pressed {\n"
                                            "	background-color:#0082BC;\n"
                                            "}\n"
                                            "QPushButton#btn_report_user:disabled {\n"
                                            "	background-color:  #BFBFBF;\n"
                                            "	color: #6a6767;\n"
                                            "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/report.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report_user.setIcon(icon1)
        self.btn_report_user.setIconSize(QSize(16, 16))

        self.hzl_content_button_user.addWidget(self.btn_report_user)

        self.hls_between_button_report_and_logs_user = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_user.addItem(self.hls_between_button_report_and_logs_user)

        self.btn_log_user = QPushButton(self.frm_content_button_user)
        self.btn_log_user.setObjectName(u"btn_log_user")
        self.btn_log_user.setMinimumSize(QSize(75, 23))
        self.btn_log_user.setMaximumSize(QSize(75, 23))
        self.btn_log_user.setStyleSheet(u"QPushButton#btn_log_user {\n"
                                         "	background-color: #A9A9AC;\n"
                                         "	color: white;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton#btn_log_user:hover {\n"
                                         "	background-color:#97979B;\n"
                                         "}\n"
                                         "QPushButton#btn_log_user:pressed {\n"
                                         "	background-color:#8A8A8E;\n"
                                         "}\n"
                                         "QPushButton#btn_log_user:disabled {\n"
                                         "	background-color:  #BFBFBF;\n"
                                         "	color: #6a6767;\n"
                                         "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"../img/log.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_log_user.setIcon(icon2)

        self.hzl_content_button_user.addWidget(self.btn_log_user)

        self.hls_between_button_and_border_right_user = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_user.addItem(self.hls_between_button_and_border_right_user)

        self.vrl_content_user.addWidget(self.frm_content_button_user)

        self.frm_content_fields_user = QFrame(self.frm_content_user)
        self.frm_content_fields_user.setObjectName(u"frm_content_fields_user")
        self.frm_content_fields_user.setMinimumSize(QSize(662, 501))
        self.frm_content_fields_user.setFont(font)
        self.frm_content_fields_user.setStyleSheet(u"QHeaderView::section {\n"
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
        self.frm_content_fields_user.setFrameShape(QFrame.StyledPanel)
        self.frm_content_fields_user.setFrameShadow(QFrame.Raised)

        self.hzl_content_fields_user = QHBoxLayout(self.frm_content_fields_user)
        self.hzl_content_fields_user.setObjectName(u"hzl_content_fields_user")

        self.hls_between__borde_left_and_table_user = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_fields_user.addItem(self.hls_between__borde_left_and_table_user)

        self.tab_user = QTableWidget(self.frm_content_fields_user)
        self.tab_user.setObjectName(u"tab_user")
        self.tab_user.setMinimumSize(QSize(642, 481))
        self.tab_user.setStyleSheet(u"QTableWidget {\n"
                                     "	background: white;\n"
                                     "	border-style: none;\n"
                                     "}\n"
                                     "QTableWidget::item {\n"
                                     "	Border-bottom:1px solid #EEF1F7;\n"
                                     "}\n")
        self.tab_user.setFrameShape(QFrame.NoFrame)
        self.tab_user.setFrameShadow(QFrame.Plain)
        self.tab_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_user.setSelectionMode(QAbstractItemView.NoSelection)
        self.tab_user.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_user.setShowGrid(False)
        self.tab_user.setGridStyle(Qt.NoPen)
        self.tab_user.setSortingEnabled(True)
        self.tab_user.horizontalHeader().setSectionsMovable(True)
        self.tab_user.verticalHeader().setVisible(False)
        self.tab_user.setColumnCount(6)
        id_user = QTableWidgetItem()
        self.tab_user.setHorizontalHeaderItem(0, id_user)
        photo_user = QTableWidgetItem()
        self.tab_user.setHorizontalHeaderItem(1, photo_user)
        name_user = QTableWidgetItem()
        self.tab_user.setHorizontalHeaderItem(2, name_user)
        edit_user = QTableWidgetItem()
        self.tab_user.setHorizontalHeaderItem(3, edit_user)
        delete_user = QTableWidgetItem()
        self.tab_user.setHorizontalHeaderItem(4, delete_user)
        view_user = QTableWidgetItem()
        self.tab_user.setHorizontalHeaderItem(5, view_user)
        self.tab_user.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tab_user.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tab_user.setColumnWidth(0, 70)
        self.tab_user.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tab_user.setColumnWidth(1, 80)
        self.tab_user.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tab_user.setColumnWidth(2, 282)
        self.tab_user.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tab_user.setColumnWidth(3, 70)
        self.tab_user.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tab_user.setColumnWidth(4, 70)
        self.tab_user.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tab_user.setColumnWidth(5, 85)

        self.hzl_content_fields_user.addWidget(self.tab_user)

        self.hls_between_table_and_borde_right_user = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_fields_user.addItem(self.hls_between_table_and_borde_right_user)
        
        self.vrl_content_user.addWidget(self.frm_content_fields_user)

        self.vrl_frm_content_user.addWidget(self.frm_content_user)

        self.retranslate_frm_user_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_user_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Usu\u00e1rio", None))
        self.btn_new_user.setText(QCoreApplication.translate("frm_content", u"Incluir", None))
        self.btn_report_user.setText(QCoreApplication.translate("frm_content", u"Relat\u00f3rio", None))
        self.btn_log_user.setText(QCoreApplication.translate("frm_content", u"Logs", None))
        id_user = self.tab_user.horizontalHeaderItem(0)
        id_user.setText(QCoreApplication.translate("frm_content", u"ID", None))
        name_user = self.tab_user.horizontalHeaderItem(2)
        name_user.setText(QCoreApplication.translate("frm_content", u"Nome", None))
        edit_user = self.tab_user.horizontalHeaderItem(3)
        edit_user.setText(QCoreApplication.translate("frm_content", u"Editar", None))
        delete_user = self.tab_user.horizontalHeaderItem(4)
        delete_user.setText(QCoreApplication.translate("frm_content", u"Deletar", None))
        view_user = self.tab_user.horizontalHeaderItem(5)
        view_user.setText(QCoreApplication.translate("frm_content", u"Visualizar", None))
    # retranslateUi

