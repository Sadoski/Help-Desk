# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions.functions import resource_path


class FormDepartmentContent(object):
        
    def setup_frm_department_content(self, frm_content):
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
        
        self.vrl_frm_content_department = QVBoxLayout(frm_content)
        self.vrl_frm_content_department.setSpacing(0)
        self.vrl_frm_content_department.setObjectName(u"vrl_frm_content_department")
        self.vrl_frm_content_department.setContentsMargins(0, 0, 0, 0)
        
        self.frm_content_department = QFrame(frm_content)
        self.frm_content_department.setObjectName(u"frm_content_department")
        self.frm_content_department.setMinimumSize(QSize(682, 561))
        self.frm_content_department.setFont(font)
        self.frm_content_department.setFrameShape(QFrame.StyledPanel)
        self.frm_content_department.setFrameShadow(QFrame.Raised)
        
        self.vrl_content_department = QVBoxLayout(self.frm_content_department)
        self.vrl_content_department.setObjectName(u"vrl_content_department")
        
        self.frm_content_button_department = QFrame(self.frm_content_department)
        self.frm_content_button_department.setObjectName(u"frm_content_button_department")
        self.frm_content_button_department.setMinimumSize(QSize(661, 41))
        self.frm_content_button_department.setMaximumSize(QSize(16777215, 41))
        self.frm_content_button_department.setFrameShape(QFrame.StyledPanel)
        self.frm_content_button_department.setFrameShadow(QFrame.Raised)
        
        self.hzl_content_button_department = QHBoxLayout(self.frm_content_button_department)
        self.hzl_content_button_department.setSpacing(10)
        self.hzl_content_button_department.setObjectName(u"hzl_content_button_department")
        self.hzl_content_button_department.setContentsMargins(15, 0, 15, 0)
        
        self.hls_between_boder_left_and_buttons_department = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_department.addItem(self.hls_between_boder_left_and_buttons_department)

        self.btn_new_department = QPushButton(self.frm_content_button_department)
        self.btn_new_department.setObjectName(u"btn_new_department")
        self.btn_new_department.setEnabled(True)
        self.btn_new_department.setMinimumSize(QSize(75, 23))
        self.btn_new_department.setMaximumSize(QSize(75, 23))
        self.btn_new_department.setStyleSheet(u"QPushButton#btn_new_department {\n"
                                               "	background-color: #2FB7F3;\n"
                                               "	color: white;\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton#btn_new_department:hover {\n"
                                               "	background-color:#009CE1;\n"
                                               "}\n"
                                               "QPushButton#btn_new_tags:pressed {\n"
                                               "	background-color:#0082BC;\n"
                                               "}\n"
                                               "QPushButton#btn_new_department:disabled {\n"
                                               "	background-color:  #BFBFBF;\n"
                                               "	color: #6a6767;\n"
                                               "}")
        icon = QIcon()
        icon.addFile(resource_path(u"../img/plus-2-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_department.setIcon(icon)
        self.btn_new_department.setIconSize(QSize(10, 10))

        self.hzl_content_button_department.addWidget(self.btn_new_department)

        self.btn_report_department = QPushButton(self.frm_content_button_department)
        self.btn_report_department.setObjectName(u"btn_report_department")
        self.btn_report_department.setEnabled(True)
        self.btn_report_department.setMinimumSize(QSize(75, 23))
        self.btn_report_department.setMaximumSize(QSize(75, 23))
        self.btn_report_department.setStyleSheet(u"QPushButton#btn_report_department {\n"
                                                  "	background-color: #2FB7F3;\n"
                                                  "	color: white;\n"
                                                  "	border-radius: 5px;\n"
                                                  "}\n"
                                                  "QPushButton#btn_report_department:hover {\n"
                                                  "	background-color:#009CE1;\n"
                                                  "}\n"
                                                  "QPushButton#btn_report_department:pressed {\n"
                                                  "	background-color:#0082BC;\n"
                                                  "}\n"
                                                  "QPushButton#btn_report_department:disabled {\n"
                                                  "	background-color:  #BFBFBF;\n"
                                                  "	color: #6a6767;\n"
                                                  "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/report.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report_department.setIcon(icon1)
        self.btn_report_department.setIconSize(QSize(16, 16))

        self.hzl_content_button_department.addWidget(self.btn_report_department)

        self.hls_between_button_report_and_logs_department = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_department.addItem(self.hls_between_button_report_and_logs_department)

        self.btn_log_department = QPushButton(self.frm_content_button_department)
        self.btn_log_department.setObjectName(u"btn_log_department")
        self.btn_log_department.setMinimumSize(QSize(75, 23))
        self.btn_log_department.setMaximumSize(QSize(75, 23))
        self.btn_log_department.setStyleSheet(u"QPushButton#btn_log_department {\n"
                                               "	background-color: #A9A9AC;\n"
                                               "	color: white;\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton#btn_log_department:hover {\n"
                                               "	background-color:#97979B;\n"
                                               "}\n"
                                               "QPushButton#btn_log_department:pressed {\n"
                                               "	background-color:#8A8A8E;\n"
                                               "}\n"
                                               "QPushButton#btn_log_department:disabled {\n"
                                               "	background-color:  #BFBFBF;\n"
                                               "	color: #6a6767;\n"
                                               "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"../img/log.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_log_department.setIcon(icon2)

        self.hzl_content_button_department.addWidget(self.btn_log_department)

        self.hls_between_button_and_border_right_department = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_department.addItem(self.hls_between_button_and_border_right_department)

        self.vrl_content_department.addWidget(self.frm_content_button_department)

        self.frm_content_fields_department = QFrame(self.frm_content_department)
        self.frm_content_fields_department.setObjectName(u"frm_content_fields_department")
        self.frm_content_fields_department.setMinimumSize(QSize(662, 501))
        self.frm_content_fields_department.setFont(font)
        self.frm_content_fields_department.setStyleSheet(u"QHeaderView::section {\n"
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
        self.frm_content_fields_department.setFrameShape(QFrame.StyledPanel)
        self.frm_content_fields_department.setFrameShadow(QFrame.Raised)
        
        self.hzl_content_fields_department = QHBoxLayout(self.frm_content_fields_department)
        self.hzl_content_fields_department.setObjectName(u"hzl_content_fields_department")

        self.hls_between__borde_left_and_table_department = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_fields_department.addItem(self.hls_between__borde_left_and_table_department)

        self.tab_department = QTableWidget(self.frm_content_fields_department)
        self.tab_department.setObjectName(u"tab_department")
        self.tab_department.setMinimumSize(QSize(642, 481))
        self.tab_department.setStyleSheet(u"QTableWidget {\n"
                                           "	background: white;\n"
                                           "	border-style: none;\n"
                                           "}\n"
                                           "QTableWidget::item {\n"
                                           "	Border-bottom:1px solid #EEF1F7;\n"
                                           "}\n")
        self.tab_department.setFrameShape(QFrame.NoFrame)
        self.tab_department.setFrameShadow(QFrame.Plain)
        self.tab_department.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_department.setSelectionMode(QAbstractItemView.NoSelection)
        self.tab_department.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_department.setShowGrid(False)
        self.tab_department.setGridStyle(Qt.NoPen)
        self.tab_department.setSortingEnabled(True)
        self.tab_department.horizontalHeader().setSectionsMovable(True)
        self.tab_department.verticalHeader().setVisible(False)
        self.tab_department.setColumnCount(5)
        id_department = QTableWidgetItem()
        self.tab_department.setHorizontalHeaderItem(0, id_department)
        department = QTableWidgetItem()
        self.tab_department.setHorizontalHeaderItem(1, department)
        edit_department = QTableWidgetItem()
        self.tab_department.setHorizontalHeaderItem(2, edit_department)
        delete_department = QTableWidgetItem()
        self.tab_department.setHorizontalHeaderItem(3, delete_department)
        view_department = QTableWidgetItem()
        self.tab_department.setHorizontalHeaderItem(4, view_department)
        self.tab_department.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tab_department.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tab_department.setColumnWidth(0, 70)
        self.tab_department.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tab_department.setColumnWidth(1, 362)
        self.tab_department.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tab_department.setColumnWidth(2, 70)
        self.tab_department.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tab_department.setColumnWidth(3, 70)
        self.tab_department.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tab_department.setColumnWidth(4, 85)

        self.hzl_content_fields_department.addWidget(self.tab_department)

        self.hls_between_table_and_borde_right_department = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_fields_department.addItem(self.hls_between_table_and_borde_right_department)

        self.vrl_content_department.addWidget(self.frm_content_fields_department)

        self.vrl_frm_content_department.addWidget(self.frm_content_department)

        self.retranslate_frm_department_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_department_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Departamento", None))
        self.btn_new_department.setText(QCoreApplication.translate("frm_content", u"Incluir", None))
        self.btn_report_department.setText(QCoreApplication.translate("frm_content", u"Relat\u00f3rio", None))
        self.btn_log_department.setText(QCoreApplication.translate("frm_content", u"Logs", None))
        id_department = self.tab_department.horizontalHeaderItem(0)
        id_department.setText(QCoreApplication.translate("frm_content", u"ID", None));
        department = self.tab_department.horizontalHeaderItem(1)
        department.setText(QCoreApplication.translate("frm_content", u"Departamento", None));
        edit_department = self.tab_department.horizontalHeaderItem(2)
        edit_department.setText(QCoreApplication.translate("frm_content", u"Editar", None));
        delete_department = self.tab_department.horizontalHeaderItem(3)
        delete_department.setText(QCoreApplication.translate("frm_content", u"Deletar", None));
        view_department = self.tab_department.horizontalHeaderItem(4)
        view_department.setText(QCoreApplication.translate("frm_content", u"Visualizar", None));
    # retranslateUi

