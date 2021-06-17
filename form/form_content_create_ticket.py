# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions.functions import resource_path


class FormCreateTicketContent(object):

    def setup_frm_create_ticket_content(self, frm_content):
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
                                   "	border-bottom-right-radius: 15px;\n"
                                   "}")

        self.vrl_frm_conten_ticket_message = QVBoxLayout(frm_content)
        self.vrl_frm_conten_ticket_message.setSpacing(0)
        self.vrl_frm_conten_ticket_message.setObjectName(u"vrl_frm_conten_ticket_message")
        self.vrl_frm_conten_ticket_message.setContentsMargins(0, 0, 0, 0)

        self.frm_content_ticket_message = QFrame(frm_content)
        self.frm_content_ticket_message.setObjectName(u"frm_content_ticket_message")
        self.frm_content_ticket_message.setMinimumSize(QSize(682, 561))
        font1 = QFont()
        font1.setPointSize(10)
        self.frm_content_ticket_message.setFont(font1)
        self.frm_content_ticket_message.setFrameShape(QFrame.StyledPanel)
        self.frm_content_ticket_message.setFrameShadow(QFrame.Raised)

        self.vrl_content_ticket_message = QVBoxLayout(self.frm_content_ticket_message)
        self.vrl_content_ticket_message.setObjectName(u"vrl_content_ticket_message")

        self.frm_ticket_tags = QFrame(self.frm_content_ticket_message)
        self.frm_ticket_tags.setObjectName(u"frm_ticket_tags")
        self.frm_ticket_tags.setMinimumSize(QSize(662, 51))
        self.frm_ticket_tags.setMaximumSize(QSize(16777215, 51))
        font2 = QFont()
        font2.setPointSize(11)
        self.frm_ticket_tags.setFont(font2)

        self.vrl_ticket_tags = QVBoxLayout(self.frm_ticket_tags)
        self.vrl_ticket_tags.setObjectName(u"vrl_ticket_tags")
        self.vrl_ticket_tags.setContentsMargins(0, 0, 0, 0)

        self.sra_ticket_tags = QScrollArea(self.frm_ticket_tags)
        self.sra_ticket_tags.setObjectName(u"sra_ticket_tags")
        self.sra_ticket_tags.setMinimumSize(QSize(651, 51))
        #self.sra_ticket_tags.setMaximumSize(QSize(651, 51))
        self.sra_ticket_tags.setStyleSheet(u"QScrollArea QWidget {   \n"
                                            "    background-color:#F5F5F5;\n"
                                            "}\n"
                                            "QScrollArea  {\n"
                                            "	border: none;\n"
                                            "}\n")
        self.sra_ticket_tags.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.sra_ticket_tags.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sra_ticket_tags.setWidgetResizable(True)

        self.srw_content_ticket_tags = QWidget()
        self.srw_content_ticket_tags.setObjectName(u"srw_content_ticket_tags")
        self.srw_content_ticket_tags.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.srw_content_ticket_tags.setGeometry(QRect(0, 0, 651, 51))

        self.hzl_content_ticket_tags = QHBoxLayout(self.srw_content_ticket_tags)
        self.hzl_content_ticket_tags.setSpacing(9)
        self.hzl_content_ticket_tags.setObjectName(u"hzl_content_ticket_tags")
        self.hzl_content_ticket_tags.setContentsMargins(0, 0, 0, 0)

        self.hls_between_boder_left_and_buttons_ticket_tags = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hzl_content_ticket_tags.addItem(self.hls_between_boder_left_and_buttons_ticket_tags)

        self.btn_add_tag_ticket = QPushButton(self.srw_content_ticket_tags)
        self.btn_add_tag_ticket.setObjectName(u"btn_add_tag_ticket")
        self.btn_add_tag_ticket.setMinimumSize(QSize(85, 25))
        self.btn_add_tag_ticket.setMaximumSize(QSize(85, 25))
        self.btn_add_tag_ticket.setFocusPolicy(Qt.NoFocus)
        self.btn_add_tag_ticket.setStyleSheet(u"QPushButton#btn_add_tag_ticket {\n"
                                               "	background: #2E6AFF;\n"
                                               "	color: white;\n"
                                               "	border: 3px solid #2E6AFF;\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton#btn_add_tag_ticket:hover {\n"
                                               "	background-color:#2B62EA;\n"
                                               "	border-color: #2B62EA;\n"
                                               "}\n"
                                               "QPushButton#btn_add_tag_ticket:pressed {\n"
                                               "	background-color:#295AD5;\n"
                                               "	border-color: #295AD5;\n"
                                               "}\n")
        icon = QIcon()
        icon.addFile(resource_path(u"../img/plus-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_tag_ticket.setIcon(icon)
        self.btn_add_tag_ticket.setIconSize(QSize(10, 10))

        self.hzl_content_ticket_tags.addWidget(self.btn_add_tag_ticket)

        self.btn_filter = QToolButton(self.srw_content_ticket_tags)
        self.btn_filter.setObjectName(u"btn_filter")
        self.btn_filter.setMinimumSize(QSize(85, 25))
        self.btn_filter.setMaximumSize(QSize(85, 25))
        self.btn_filter.setFocusPolicy(Qt.NoFocus)
        self.btn_filter.setStyleSheet(u"QToolButton#btn_filter {\n"
                                       "	background: #7E26FE;\n"
                                       "	color: white;\n"
                                       "	border: 3px solid #7E26FE;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QToolButton#btn_filter:hover {\n"
                                       "	background-color:#7725EE;\n"
                                       "	border-color: #7725EE;\n"
                                       "}\n"
                                       "QToolButton#btn_filter:pressed {\n"
                                       "	background-color:#6721CD;\n"
                                       "	border-color: #6721CD;\n"
                                       "}\n")

        self.hzl_content_ticket_tags.addWidget(self.btn_filter)

        self.hls_between_border_right_and_buttons_ticket_tags = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_content_ticket_tags.addItem(self.hls_between_border_right_and_buttons_ticket_tags)

        self.sra_ticket_tags.setWidget(self.srw_content_ticket_tags)

        self.vrl_ticket_tags.addWidget(self.sra_ticket_tags)

        self.vrl_content_ticket_message.addWidget(self.frm_ticket_tags)

        self.frm_content_fields_ticket_message = QFrame(self.frm_content_ticket_message)
        self.frm_content_fields_ticket_message.setObjectName(u"frm_content_fields_ticket_message")
        self.frm_content_fields_ticket_message.setMinimumSize(QSize(601, 461))
        self.frm_content_fields_ticket_message.setFrameShape(QFrame.StyledPanel)
        self.frm_content_fields_ticket_message.setFrameShadow(QFrame.Raised)

        self.vrl_content_fields_ticket_message = QVBoxLayout(self.frm_content_fields_ticket_message)
        self.vrl_content_fields_ticket_message.setObjectName(u"vrl_content_fields_ticket_message")

        self.frm_content_information_ticket = QFrame(self.frm_content_fields_ticket_message)
        self.frm_content_information_ticket.setObjectName(u"frm_content_information_ticket")
        self.frm_content_information_ticket.setMinimumSize(QSize(642, 95))
        self.frm_content_information_ticket.setMaximumSize(QSize(16777215, 95))
        self.frm_content_information_ticket.setFrameShape(QFrame.StyledPanel)
        self.frm_content_information_ticket.setFrameShadow(QFrame.Raised)

        self.grl_content_information_ticket = QGridLayout(self.frm_content_information_ticket)
        self.grl_content_information_ticket.setSpacing(0)
        self.grl_content_information_ticket.setObjectName(u"grl_content_information_ticket")
        self.grl_content_information_ticket.setContentsMargins(0, 0, 0, 0)

        self.lbl_title = QLabel(self.frm_content_information_ticket)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 16))
        self.lbl_title.setMaximumSize(QSize(16777215, 16))
        self.lbl_title.setFont(font1)
        self.lbl_title.setStyleSheet(u"QLabel {\n"
                                      "	color: #605D5D;\n"
                                      "}")

        self.grl_content_information_ticket.addWidget(self.lbl_title, 0, 0, 1, 2)

        self.txt_title = QLineEdit(self.frm_content_information_ticket)
        self.txt_title.setObjectName(u"txt_title")
        self.txt_title.setMinimumSize(QSize(611, 20))
        self.txt_title.setMaximumSize(QSize(850, 16777215))
        self.txt_title.setFont(font1)
        self.txt_title.setStyleSheet(u"QLineEdit#txt_title {\n"
                                      "	background-color: white;\n"
                                      "	color: #8C8C8C;\n"
                                      "	border: 1px solid #AFAEAE;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QLineEdit#txt_title:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_title:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")

        self.grl_content_information_ticket.addWidget(self.txt_title, 1, 0, 1, 7)

        self.lbl_department = QLabel(self.frm_content_information_ticket)
        self.lbl_department.setObjectName(u"lbl_department")
        self.lbl_department.setMinimumSize(QSize(100, 16))
        self.lbl_department.setMaximumSize(QSize(100, 16))
        self.lbl_department.setFont(font1)
        self.lbl_department.setStyleSheet(u"QLabel {\n"
                                           "	color: #605D5D;\n"
                                           "}")

        self.grl_content_information_ticket.addWidget(self.lbl_department, 2, 1, 1, 1)

        self.lbl_priority = QLabel(self.frm_content_information_ticket)
        self.lbl_priority.setObjectName(u"lbl_priority")
        self.lbl_priority.setMinimumSize(QSize(100, 16))
        self.lbl_priority.setMaximumSize(QSize(100, 16))
        self.lbl_priority.setFont(font1)
        self.lbl_priority.setStyleSheet(u"QLabel {\n"
                                         "	color: #605D5D;\n"
                                         "}")

        self.grl_content_information_ticket.addWidget(self.lbl_priority, 2, 3, 1, 1)

        self.lbl_status = QLabel(self.frm_content_information_ticket)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setMinimumSize(QSize(100, 16))
        self.lbl_status.setMaximumSize(QSize(100, 16))
        self.lbl_status.setFont(font1)
        self.lbl_status.setStyleSheet(u"QLabel {\n"
                                       "	color: #605D5D;\n"
                                       "}")

        self.grl_content_information_ticket.addWidget(self.lbl_status, 2, 5, 1, 1)

        self.cbx_department = QComboBox(self.frm_content_information_ticket)
        self.cbx_department.setObjectName(u"cbx_department")
        self.cbx_department.setMinimumSize(QSize(150, 20))
        self.cbx_department.setMaximumSize(QSize(250, 16777215))
        self.cbx_department.setFont(font)
        self.cbx_department.setStyleSheet(u"QComboBox#cbx_department{\n"
                                           "	background-color: #eeeeee;\n"
                                           "	color: #6a6767;\n"
                                           "	border: 1px solid gray;\n"
                                           "	border-radius: 5px;\n"
                                           "}\n"
                                           "QComboBox#cbx_department:focus{\n"
                                           "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                           "}\n"
                                           "QComboBox#cbx_department:disabled {\n"
                                           "	background-color:  #dcdcdc;\n"
                                           "	color: #6a6767;\n"
                                           "	border: 1px solid gray;\n"
                                           "}\n"
                                           "QHeaderView::section QComboBox {\n"
                                           "    background-color: #585A5C;\n"
                                           "    color: #F0F0F0;\n"
                                           "	border-radius: 5px;\n"
                                           "}\n"
                                           "QComboBox::drop-down {\n"
                                           "	outline:0px;\n"
                                           "    border:0px;\n"
                                           "}\n"
                                           "QComboBox::down-arrow{\n"
                                           "	subcontrol-position: bottom center;\n"
                                           "    subcontrol-origin: margin;\n"
                                           "	background-color: gray ;\n"
                                           "	border-radius: 5px;\n"
                                           "	border: solid #eeeeee;\n"
                                           "	border-width:2px 3px 8px 3px;\n"
                                           "}\n")

        self.grl_content_information_ticket.addWidget(self.cbx_department, 3, 1, 1, 1)

        self.hls_between_buttons_department_and_priority_ticket_message = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.grl_content_information_ticket.addItem(self.hls_between_buttons_department_and_priority_ticket_message, 3, 2, 1, 1)

        self.cbx_priority = QComboBox(self.frm_content_information_ticket)
        self.cbx_priority.setObjectName(u"cbx_priority")
        self.cbx_priority.setMinimumSize(QSize(150, 20))
        self.cbx_priority.setMaximumSize(QSize(250, 16777215))
        self.cbx_priority.setFont(font)
        self.cbx_priority.setStyleSheet(u"QComboBox#cbx_priority {\n"
                                         "	background-color: #eeeeee;\n"
                                         "	color: #6a6767;\n"
                                         "	border: 1px solid gray;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QComboBox#cbx_priority:focus{\n"
                                         "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                         "}\n"
                                         "QComboBox#cbx_priority:disabled {\n"
                                         "	background-color:  #dcdcdc;\n"
                                         "	color: #6a6767;\n"
                                         "	border: 1px solid gray;\n"
                                         "}\n"
                                          "QHeaderView::section QComboBox {\n"
                                         "    background-color: #585A5C;\n"
                                         "    color: #F0F0F0;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QComboBox::drop-down {\n"
                                         "	outline:0px;\n"
                                         "    border:0px;\n"
                                         "}\n"
                                         "QComboBox::down-arrow{\n"
                                         "	subcontrol-position: bottom center;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "	background-color: gray ;\n"
                                         "	border-radius: 5px;\n"
                                         "	border: solid #eeeeee;\n"
                                         "	border-width:2px 3px 8px 3px;\n"
                                         "}\n")

        self.grl_content_information_ticket.addWidget(self.cbx_priority, 3, 3, 1, 1)

        self.hls_between_buttons_priority_and_status_ticket_message = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.grl_content_information_ticket.addItem(self.hls_between_buttons_priority_and_status_ticket_message, 3, 4, 1, 1)

        self.cbx_status = QComboBox(self.frm_content_information_ticket)
        self.cbx_status.setObjectName(u"cbx_status")
        self.cbx_status.setMinimumSize(QSize(150, 20))
        self.cbx_status.setMaximumSize(QSize(250, 16777215))
        self.cbx_status.setFont(font)
        self.cbx_status.setStyleSheet(u"QComboBox#cbx_status {\n"
                                       "	background-color: #eeeeee;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QComboBox#cbx_status:focus{\n"
                                       "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                       "}\n"
                                       "QComboBox#cbx_status:disabled {\n"
                                       "	background-color:  #dcdcdc;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "}\n"
                                       "QHeaderView::section QComboBox {\n"
                                       "    background-color: #585A5C;\n"
                                       "    color: #F0F0F0;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QComboBox::drop-down {\n"
                                       "	outline:0px;\n"
                                       "    border:0px;\n"
                                       "}\n"
                                       "QComboBox::down-arrow{\n"
                                       "	subcontrol-position: bottom center;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "	background-color: gray ;\n"
                                       "	border-radius: 5px;\n"
                                       "	border: solid #eeeeee;\n"
                                       "	border-width:2px 3px 8px 3px;\n"
                                       "}\n")

        self.grl_content_information_ticket.addWidget(self.cbx_status, 3, 5, 1, 1)

        self.hls_between_buttom_status_and_border_ticket_message = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_information_ticket.addItem(self.hls_between_buttom_status_and_border_ticket_message, 2, 6, 2, 1)

        self.vrl_content_fields_ticket_message.addWidget(self.frm_content_information_ticket)

        self.sra_message_ticket = QScrollArea(self.frm_content_fields_ticket_message)
        self.sra_message_ticket.setObjectName(u"sra_message_ticket")
        self.sra_message_ticket.setMinimumSize(QSize(641, 271))
        self.sra_message_ticket.setStyleSheet(u"QScrollArea QWidget {   \n"
                                               "    background: white;\n"
                                               "}\n"
                                               "QScrollArea  {\n"
                                               "	border: none;\n"
                                               "}\n")
        self.sra_message_ticket.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sra_message_ticket.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sra_message_ticket.setWidgetResizable(True)

        self.srw_content_message_ticket = QWidget()
        self.srw_content_message_ticket.setObjectName(u"srw_content_message_ticket")
        self.srw_content_message_ticket.setGeometry(QRect(0, 0, 642, 271))

        self.vrl_content_message_ticket = QVBoxLayout(self.srw_content_message_ticket)
        self.vrl_content_message_ticket.setSpacing(0)
        self.vrl_content_message_ticket.setObjectName(u"vrl_content_message_ticket")
        self.vrl_content_message_ticket.setContentsMargins(0, 0, 0, 0)

        self.vls_between_message_chat_and_border_bottom = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.sra_message_ticket.setWidget(self.srw_content_message_ticket)

        self.vrl_content_fields_ticket_message.addWidget(self.sra_message_ticket)

        self.frm_content_message_writing_field = QFrame(self.frm_content_fields_ticket_message)
        self.frm_content_message_writing_field.setObjectName(u"frm_content_message_writing_field")
        self.frm_content_message_writing_field.setMinimumSize(QSize(641, 91))
        self.frm_content_message_writing_field.setFrameShape(QFrame.StyledPanel)
        self.frm_content_message_writing_field.setFrameShadow(QFrame.Raised)

        self.grl_content_message_writing_field = QGridLayout(self.frm_content_message_writing_field)
        self.grl_content_message_writing_field.setObjectName(u"grl_content_message_writing_field")

        self.txt_message = QTextEdit(self.frm_content_message_writing_field)
        self.txt_message.setObjectName(u"txt_message")
        self.txt_message.setMinimumSize(QSize(580, 75))
        self.txt_message.setStyleSheet(u"QTextEdit#txt_message {\n"
                                        "	background-color: white;\n"
                                        "	color: #8C8C8C;\n"
                                        "	border: 1px solid #AFAEAE;\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QTextEdit#txt_message:focus{\n"
                                        "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                        "}\n"
                                        "QTextEdit#txt_message:disabled {\n"
                                        "	background-color:  #dcdcdc;\n"
                                        "	color: #6a6767;\n"
                                        "	border: 1px solid gray;\n"
                                        "}")

        self.grl_content_message_writing_field.addWidget(self.txt_message, 0, 0, 2, 1)

        self.btn_submit = QPushButton(self.frm_content_message_writing_field)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(36, 36))
        self.btn_submit.setMaximumSize(QSize(36, 36))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        self.btn_submit.setFont(font4)
        self.btn_submit.setFocusPolicy(Qt.NoFocus)
        self.btn_submit.setStyleSheet(u"QPushButton#btn_submit {\n"
                                       "	background-color: #0080ff ;\n"
                                       "	color: #fff;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton#btn_submit:hover{\n"
                                       "	background-color:  #0073e6;\n"
                                       "}\n"
                                       "QPushButton#btn_submit:pressed {\n"
                                       "	background-color: #0059b3;\n"
                                       "}\n"
                                       "QPushButton#btn_submit:disabled {\n"
                                       "	background-color:  #a6a6a6;\n"
                                       "	color: #6a6767;\n"
                                       "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/paper-plane-48.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_submit.setIcon(icon1)
        self.btn_submit.setIconSize(QSize(20, 20))

        self.grl_content_message_writing_field.addWidget(self.btn_submit, 0, 1, 1, 1)

        self.btn_attachments = QPushButton(self.frm_content_message_writing_field)
        self.btn_attachments.setObjectName(u"btn_attachments")
        self.btn_attachments.setMinimumSize(QSize(36, 36))
        self.btn_attachments.setMaximumSize(QSize(36, 36))
        self.btn_attachments.setFont(font4)
        self.btn_attachments.setFocusPolicy(Qt.NoFocus)
        self.btn_attachments.setStyleSheet(u"QPushButton#btn_attachments {\n"
                                            "	background-color: #0080ff ;\n"
                                            "	color: #fff;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton#btn_attachments:hover{\n"
                                            "	background-color:  #0073e6;\n"
                                            "}\n"
                                            "QPushButton#btn_attachments:pressed {\n"
                                            "	background-color: #0059b3;\n"
                                            "}\n"
                                            "QPushButton#btn_attachments:disabled {\n"
                                            "	background-color:  #a6a6a6;\n"
                                            "	color: #6a6767;\n"
                                            "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"../img/attachment.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_attachments.setIcon(icon2)
        self.btn_attachments.setIconSize(QSize(20, 20))

        self.grl_content_message_writing_field.addWidget(self.btn_attachments, 1, 1, 1, 1)

        self.vrl_content_fields_ticket_message.addWidget(self.frm_content_message_writing_field)

        self.vrl_content_ticket_message.addWidget(self.frm_content_fields_ticket_message)

        self.vrl_frm_conten_ticket_message.addWidget(self.frm_content_ticket_message)

        self.retranslate_frm_create_ticket_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_create_ticket_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Abrir Ticket", None))
        self.btn_add_tag_ticket.setText(QCoreApplication.translate("frm_content", u"  Add Tag", None))
        self.btn_add_tag_ticket.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+T", None))
        self.btn_filter.setText(QCoreApplication.translate("frm_content", u"Aberto", None))
        self.lbl_title.setText(QCoreApplication.translate("frm_content", u"Titulo", None))
        self.lbl_department.setText(QCoreApplication.translate("frm_content", u"Departamento", None))
        self.lbl_priority.setText(QCoreApplication.translate("frm_content", u"Prioridade", None))
        self.lbl_status.setText(QCoreApplication.translate("frm_content", u"Status", None))
        self.btn_submit.setToolTip(QCoreApplication.translate("frm_content", u"Enviar", None))
        self.btn_submit.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para enviar a mensagem</p></body></html>", None))
        self.btn_submit.setText("")
        self.btn_submit.setShortcut(QCoreApplication.translate("frm_content", u"Enter", None))
        self.btn_attachments.setToolTip(QCoreApplication.translate("frm_content", u"Anexos", None))
        self.btn_attachments.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para anexar um arquivo</p></body></html>", None))
        self.btn_attachments.setText("")
        self.btn_attachments.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+Shift+A", None))
    # retranslateUi

