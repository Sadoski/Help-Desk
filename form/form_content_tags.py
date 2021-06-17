# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions.functions import resource_path


class FormTagsContent(object):

    def setup_frm_tags_content(self, frm_content):
        if not frm_content.objectName():
            frm_content.setObjectName(u"frm_content")
        frm_content.resize(682, 565)
        frm_content.setMinimumSize(QSize(682, 561))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        frm_content.setFont(font)
        frm_content.setStyleSheet(u"QFrame#frm_content{\n"
                                   "	background-color:#F5F5F5;\n"
                                   "    border-bottom-right-radius: 15px;"
                                   "}")

        self.vrl_frm_content_tags = QVBoxLayout(frm_content)
        self.vrl_frm_content_tags.setSpacing(0)
        self.vrl_frm_content_tags.setObjectName(u"vrl_frm_content_tags")
        self.vrl_frm_content_tags.setContentsMargins(0, 0, 0, 0)

        self.frm_content_tags = QFrame(frm_content)
        self.frm_content_tags.setObjectName(u"frm_content_tags")
        self.frm_content_tags.setMinimumSize(QSize(682, 561))
        self.frm_content_tags.setFont(font)
        self.frm_content_tags.setFrameShape(QFrame.StyledPanel)
        self.frm_content_tags.setFrameShadow(QFrame.Raised)

        self.vrl_content_tags = QVBoxLayout(self.frm_content_tags)
        self.vrl_content_tags.setObjectName(u"vrl_content_tags")

        self.frm_content_button_tags = QFrame(self.frm_content_tags)
        self.frm_content_button_tags.setObjectName(u"frm_content_button_tags")
        self.frm_content_button_tags.setMinimumSize(QSize(661, 41))
        self.frm_content_button_tags.setMaximumSize(QSize(16777215, 41))
        self.frm_content_button_tags.setFrameShape(QFrame.StyledPanel)
        self.frm_content_button_tags.setFrameShadow(QFrame.Raised)

        self.hzl_content_button_tags = QHBoxLayout(self.frm_content_button_tags)
        self.hzl_content_button_tags.setSpacing(10)
        self.hzl_content_button_tags.setObjectName(u"hzl_content_button_tags")
        self.hzl_content_button_tags.setContentsMargins(15, 0, 15, 0)

        self.hls_between_boder_left_and_buttons_tags = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_tags.addItem(self.hls_between_boder_left_and_buttons_tags)

        self.btn_new_tags = QPushButton(self.frm_content_button_tags)
        self.btn_new_tags.setObjectName(u"btn_new_tags")
        self.btn_new_tags.setEnabled(True)
        self.btn_new_tags.setMinimumSize(QSize(75, 23))
        self.btn_new_tags.setMaximumSize(QSize(75, 23))
        self.btn_new_tags.setStyleSheet(u"QPushButton#btn_new_tags {\n"
                                         "	background-color: #2FB7F3;\n"
                                         "	color: white;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton#btn_new_tags:hover {\n"
                                         "	background-color:#009CE1;\n"
                                         "}\n"
                                         "QPushButton#btn_new_tags:pressed {\n"
                                         "	background-color:#0082BC;\n"
                                         "}\n"
                                         "QPushButton#btn_new_tags:disabled {\n"
                                         "	background-color:  #BFBFBF;\n"
                                         "	color: #6a6767;\n"
                                         "}")
        icon = QIcon()
        icon.addFile(resource_path(u"../img/plus-2-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_tags.setIcon(icon)
        self.btn_new_tags.setIconSize(QSize(10, 10))

        self.hzl_content_button_tags.addWidget(self.btn_new_tags)

        self.btn_report_tags = QPushButton(self.frm_content_button_tags)
        self.btn_report_tags.setObjectName(u"btn_report_tags")
        self.btn_report_tags.setEnabled(True)
        self.btn_report_tags.setMinimumSize(QSize(75, 23))
        self.btn_report_tags.setMaximumSize(QSize(75, 23))
        self.btn_report_tags.setStyleSheet(u"QPushButton#btn_report_tags {\n"
                                            "	background-color: #2FB7F3;\n"
                                            "	color: white;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton#btn_report_tags:hover {\n"
                                            "	background-color:#009CE1;\n"
                                            "}\n"
                                            "QPushButton#btn_report_tags:pressed {\n"
                                            "	background-color:#0082BC;\n"
                                            "}\n"
                                            "QPushButton#btn_report_tags:disabled {\n"
                                            "	background-color:  #BFBFBF;\n"
                                            "	color: #6a6767;\n"
                                            "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/report.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report_tags.setIcon(icon1)
        self.btn_report_tags.setIconSize(QSize(16, 16))

        self.hzl_content_button_tags.addWidget(self.btn_report_tags)

        self.hls_between_button_report_and_logs_tags = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_tags.addItem(self.hls_between_button_report_and_logs_tags)

        self.btn_log_tags = QPushButton(self.frm_content_button_tags)
        self.btn_log_tags.setObjectName(u"btn_log_tags")
        self.btn_log_tags.setMinimumSize(QSize(75, 23))
        self.btn_log_tags.setMaximumSize(QSize(75, 23))
        self.btn_log_tags.setStyleSheet(u"QPushButton#btn_log_tags {\n"
                                         "	background-color: #A9A9AC;\n"
                                         "	color: white;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton#btn_log_tags:hover {\n"
                                         "	background-color:#97979B;\n"
                                         "}\n"
                                         "QPushButton#btn_log_tags:pressed {\n"
                                         "	background-color:#8A8A8E;\n"
                                         "}\n"
                                         "QPushButton#btn_log_tags:disabled {\n"
                                         "	background-color:  #BFBFBF;\n"
                                         "	color: #6a6767;\n"
                                         "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"../img/log.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_log_tags.setIcon(icon2)

        self.hzl_content_button_tags.addWidget(self.btn_log_tags)

        self.hls_between_button_and_border_right_tags = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_button_tags.addItem(self.hls_between_button_and_border_right_tags)

        self.vrl_content_tags.addWidget(self.frm_content_button_tags)

        self.frm_content_fields_tags = QFrame(self.frm_content_tags)
        self.frm_content_fields_tags.setObjectName(u"frm_content_fields_tags")
        self.frm_content_fields_tags.setMinimumSize(QSize(662, 501))
        self.frm_content_fields_tags.setFont(font)
        self.frm_content_fields_tags.setStyleSheet(u"QHeaderView::section {\n"
                                                    "   background-color: white;\n"
                                                    "	color: gray;\n"
                                                    "	padding: 2px;\n"
                                                    "   font-size: 10pt;\n"
                                                    "	font-weight: bold;\n"
                                                    "   border-style: none;\n"
                                                    "   text-transform: uppercase"
                                                    "}\n"
                                                    "QHeaderView:section:horizontal {\n"
                                                    "   border-top: 1px solid #DFDFDF;\n"
                                                    "	border-bottom:1px solid #DFDFDF;\n"
                                                    "}\n")
        self.frm_content_fields_tags.setFrameShape(QFrame.StyledPanel)
        self.frm_content_fields_tags.setFrameShadow(QFrame.Raised)

        self.hzl_content_fields_tags = QHBoxLayout(self.frm_content_fields_tags)
        self.hzl_content_fields_tags.setObjectName(u"hzl_content_fields_tags")

        self.hls_between__borde_left_and_table_tags = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_fields_tags.addItem(self.hls_between__borde_left_and_table_tags)

        self.tab_tags = QTableWidget(self.frm_content_fields_tags)
        self.tab_tags.setObjectName(u"tab_tags")
        self.tab_tags.setMinimumSize(QSize(642, 481))
        self.tab_tags.setStyleSheet(u"QTableWidget{\n"
                                    "	background: white;\n"
                                    "	border-style: none;\n"
                                    "}\n"
                                    "QTableWidget:item {\n"
                                    "	Border-bottom:1px solid #EEF1F7;\n"
                                    "}\n")
        self.tab_tags.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tab_tags.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_tags.setAlternatingRowColors(False)
        self.tab_tags.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_tags.setShowGrid(False)
        self.tab_tags.setGridStyle(Qt.NoPen)
        self.tab_tags.setSortingEnabled(True)
        self.tab_tags.horizontalHeader().setSectionsMovable(True)
        self.tab_tags.verticalHeader().setVisible(False)
        self.tab_tags.setColumnCount(5)
        id_tags = QTableWidgetItem()
        self.tab_tags.setHorizontalHeaderItem(0, id_tags)
        tags = QTableWidgetItem()
        self.tab_tags.setHorizontalHeaderItem(1, tags)
        edit_tags = QTableWidgetItem()
        self.tab_tags.setHorizontalHeaderItem(2, edit_tags)
        delete_tags = QTableWidgetItem()
        self.tab_tags.setHorizontalHeaderItem(3, delete_tags)
        view_tags = QTableWidgetItem()
        self.tab_tags.setHorizontalHeaderItem(4, view_tags)
        self.tab_tags.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tab_tags.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tab_tags.setColumnWidth(0, 70)
        self.tab_tags.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tab_tags.setColumnWidth(1, 362)
        self.tab_tags.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tab_tags.setColumnWidth(2, 70)
        self.tab_tags.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tab_tags.setColumnWidth(3, 70)
        self.tab_tags.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tab_tags.setColumnWidth(4, 85)

        self.hzl_content_fields_tags.addWidget(self.tab_tags)

        self.hls_between_table_and_borde_right_tags = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_fields_tags.addItem(self.hls_between_table_and_borde_right_tags)

        self.vrl_content_tags.addWidget(self.frm_content_fields_tags)

        self.vrl_frm_content_tags.addWidget(self.frm_content_tags)

        self.retranslate_frm_tags_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_tags_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Tags", None))
        self.btn_new_tags.setText(QCoreApplication.translate("frm_content", u"Incluir", None))
        self.btn_report_tags.setText(QCoreApplication.translate("frm_content", u"Relat\u00f3rio", None))
        self.btn_log_tags.setText(QCoreApplication.translate("frm_content", u"Logs", None))
        id_tag = self.tab_tags.horizontalHeaderItem(0)
        id_tag.setText(QCoreApplication.translate("frm_content", u"ID", None))
        name_tag = self.tab_tags.horizontalHeaderItem(1)
        name_tag.setText(QCoreApplication.translate("frm_content", u"Tag", None))
        edit_tag = self.tab_tags.horizontalHeaderItem(2)
        edit_tag.setText(QCoreApplication.translate("frm_content", u"Editar", None))
        delete_tag = self.tab_tags.horizontalHeaderItem(3)
        delete_tag.setText(QCoreApplication.translate("frm_content", u"Deletar", None))
        view_tag = self.tab_tags.horizontalHeaderItem(4)
        view_tag.setText(QCoreApplication.translate("frm_content", u"Visualizar", None))
