# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions.functions import resource_path


class FormUserContent(object):

    def setup_frm_user_content(self, frm_content):
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
                                   "   border-bottom-right-radius: 15px;"
                                   "}")

        self.vrl_frm_content_user = QVBoxLayout(frm_content)
        self.vrl_frm_content_user.setSpacing(0)
        self.vrl_frm_content_user.setObjectName(u"vrl_frm_content_user")
        self.vrl_frm_content_user.setContentsMargins(0, 0, 0, 0)

        self.frm_content_user = QFrame(frm_content)
        self.frm_content_user.setObjectName(u"frm_content_user")
        self.frm_content_user.setMinimumSize(QSize(682, 561))
        font1 = QFont()
        font1.setPointSize(10)
        self.frm_content_user.setFont(font1)
        self.frm_content_user.setFrameShape(QFrame.StyledPanel)
        self.frm_content_user.setFrameShadow(QFrame.Raised)

        self.vrl_content_user = QVBoxLayout(self.frm_content_user)
        self.vrl_content_user.setObjectName(u"vrl_content_user")

        self.vls_between_border_and_button_actions_user = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.vrl_content_user.addItem(self.vls_between_border_and_button_actions_user)

        self.frm_user_actions_button = QFrame(self.frm_content_user)
        self.frm_user_actions_button.setObjectName(u"frm_user_actions_button")
        self.frm_user_actions_button.setMaximumSize(QSize(16777215, 51))
        font2 = QFont()
        font2.setPointSize(11)
        self.frm_user_actions_button.setFont(font2)

        self.hzl_botoes = QHBoxLayout(self.frm_user_actions_button)
        self.hzl_botoes.setObjectName(u"hzl_botoes")
        self.hzl_botoes.setContentsMargins(-1, 6, -1, -1)

        self.hls_between_border_and_navigation_user = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_botoes.addItem(self.hls_between_border_and_navigation_user)

        self.btn_navigation_first = QPushButton(self.frm_user_actions_button)
        self.btn_navigation_first.setObjectName(u"btn_navigation_first")
        self.btn_navigation_first.setEnabled(False)
        self.btn_navigation_first.setMinimumSize(QSize(36, 36))
        self.btn_navigation_first.setMaximumSize(QSize(36, 36))
        self.btn_navigation_first.setFocusPolicy(Qt.NoFocus)
        self.btn_navigation_first.setStyleSheet(u"QPushButton#btn_navigation_first{\n"
                                                  "	border-radius: 5px;\n"
                                                  "}\n"
                                                  "QPushButton#btn_navigation_first:hover{\n"
                                                  "	border: 1px solid rgba(33,33,33,.2);\n"
                                                  "	background: rgba(33,33,33,.1);\n"
                                                  "}\n"
                                                  "QPushButton#btn_navigation_first:pressed {\n"
                                                  "	border: 1px solid rgba(33,33,33,.5);\n"
                                                  "	background: rgba(33,33,33,.2);\n"
                                                  "}")
        icon = QIcon()
        icon.addFile(resource_path(u"../img/nextAll.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_navigation_first.setIcon(icon)
        self.btn_navigation_first.setIconSize(QSize(36, 36))
        self.btn_navigation_first.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_navigation_first)

        self.btn_navigation_previous = QPushButton(self.frm_user_actions_button)
        self.btn_navigation_previous.setObjectName(u"btn_navigation_previous")
        self.btn_navigation_previous.setEnabled(False)
        self.btn_navigation_previous.setMinimumSize(QSize(36, 36))
        self.btn_navigation_previous.setMaximumSize(QSize(36, 36))
        self.btn_navigation_previous.setFocusPolicy(Qt.NoFocus)
        self.btn_navigation_previous.setStyleSheet(u"QPushButton#btn_navigation_previous{\n"
                                                    "	border-radius: 5px;\n"
                                                    "}\n"
                                                    "QPushButton#btn_navigation_previousr:hover{\n"
                                                    "	border: 1px solid rgba(33,33,33,.2);\n"
                                                    "	background: rgba(33,33,33,.1);\n"
                                                    "}\n"
                                                    "QPushButton#btn_navigation_previous:pressed {\n"
                                                    "	border: 1px solid rgba(33,33,33,.5);\n"
                                                    "	background: rgba(33,33,33,.2);\n"
                                                    "}")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"../img/next.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_navigation_previous.setIcon(icon1)
        self.btn_navigation_previous.setIconSize(QSize(36, 36))
        self.btn_navigation_previous.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_navigation_previous)

        self.btn_navigation_next = QPushButton(self.frm_user_actions_button)
        self.btn_navigation_next.setObjectName(u"btn_navigation_next")
        self.btn_navigation_next.setEnabled(False)
        self.btn_navigation_next.setMinimumSize(QSize(36, 36))
        self.btn_navigation_next.setMaximumSize(QSize(36, 36))
        self.btn_navigation_next.setFocusPolicy(Qt.NoFocus)
        self.btn_navigation_next.setStyleSheet(u"QPushButton#btn_navigation_next{\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QPushButton#btn_navigation_next:hover{\n"
                                                "	border: 1px solid rgba(33,33,33,.2);\n"
                                                "	background: rgba(33,33,33,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_navigation_next:pressed {\n"
                                                "	border: 1px solid rgba(33,33,33,.5);\n"
                                                "	background: rgba(33,33,33,.2);\n"
                                                "}")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"../img/previous.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_navigation_next.setIcon(icon2)
        self.btn_navigation_next.setIconSize(QSize(36, 36))
        self.btn_navigation_next.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_navigation_next)

        self.btn_navigation_last = QPushButton(self.frm_user_actions_button)
        self.btn_navigation_last.setObjectName(u"btn_navigation_last")
        self.btn_navigation_last.setEnabled(False)
        self.btn_navigation_last.setMinimumSize(QSize(36, 36))
        self.btn_navigation_last.setMaximumSize(QSize(36, 36))
        self.btn_navigation_last.setFocusPolicy(Qt.NoFocus)
        self.btn_navigation_last.setStyleSheet(u"QPushButton#btn_navigation_last{\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QPushButton#btn_navigation_last:hover{\n"
                                                "	border: 1px solid rgba(33,33,33,.2);\n"
                                                "	background: rgba(33,33,33,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_navigation_last:pressed {\n"
                                                "	border: 1px solid rgba(33,33,33,.5);\n"
                                                "	background: rgba(33,33,33,.2);\n"
                                                "}")
        icon3 = QIcon()
        icon3.addFile(resource_path(u"../img/PreviousAll.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_navigation_last.setIcon(icon3)
        self.btn_navigation_last.setIconSize(QSize(36, 36))
        self.btn_navigation_last.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_navigation_last)

        self.hls_between_middle_of_action_navigations_user = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_botoes.addItem(self.hls_between_middle_of_action_navigations_user)

        self.btn_search_register = QPushButton(self.frm_user_actions_button)
        self.btn_search_register.setObjectName(u"btn_search_register")
        self.btn_search_register.setMinimumSize(QSize(36, 36))
        self.btn_search_register.setMaximumSize(QSize(36, 36))
        self.btn_search_register.setFocusPolicy(Qt.NoFocus)
        self.btn_search_register.setStyleSheet(u"QPushButton#btn_search_register{\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QPushButton#btn_search_register:hover{\n"
                                                "	border: 1px solid rgba(33,33,33,.2);\n"
                                                "	background: rgba(33,33,33,.1);\n"
                                                "}\n"
                                                "QPushButton#btn_search_register:pressed {\n"
                                                "	border: 1px solid rgba(33,33,33,.5);\n"
                                                "	background: rgba(33,33,33,.2);\n"
                                                "}")
        icon4 = QIcon()
        icon4.addFile(resource_path(u"../img/edit_find_replace.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search_register.setIcon(icon4)
        self.btn_search_register.setIconSize(QSize(36, 30))
        self.btn_search_register.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_search_register)

        self.btn_print = QPushButton(self.frm_user_actions_button)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(36, 36))
        self.btn_print.setMaximumSize(QSize(36, 36))
        self.btn_print.setFocusPolicy(Qt.NoFocus)
        self.btn_print.setStyleSheet(u"QPushButton#btn_print{\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#btn_print:hover{\n"
                                      "	border: 1px solid rgba(33,33,33,.2);\n"
                                      "	background: rgba(33,33,33,.1);\n"
                                      "}\n"
                                      "QPushButton#btn_print:pressed {\n"
                                      "	border: 1px solid rgba(33,33,33,.5);\n"
                                      "	background: rgba(33,33,33,.2);\n"
                                      "}")
        icon5 = QIcon()
        icon5.addFile(resource_path(u"../img/print.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print.setIcon(icon5)
        self.btn_print.setIconSize(QSize(36, 36))
        self.btn_print.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_print)

        self.btn_copy = QPushButton(self.frm_user_actions_button)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setMinimumSize(QSize(36, 36))
        self.btn_copy.setMaximumSize(QSize(36, 36))
        self.btn_copy.setFocusPolicy(Qt.NoFocus)
        self.btn_copy.setStyleSheet(u"QPushButton#btn_copy{\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton#btn_copy:hover{\n"
                                     "	border: 1px solid rgba(33,33,33,.2);\n"
                                     "	background: rgba(33,33,33,.1);\n"
                                     "}\n"
                                     "QPushButton#btn_copy:pressed {\n"
                                     "	border: 1px solid rgba(33,33,33,.5);\n"
                                     "	background: rgba(33,33,33,.2);\n"
                                     "}")
        icon6 = QIcon()
        icon6.addFile(resource_path(u"../img/copy.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copy.setIcon(icon6)
        self.btn_copy.setIconSize(QSize(36, 36))
        self.btn_copy.setFlat(True)

        self.hzl_botoes.addWidget(self.btn_copy)

        self.hls_between_middle_of_action_register_user = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_botoes.addItem(self.hls_between_middle_of_action_register_user)

        self.btn_new = QPushButton(self.frm_user_actions_button)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setMinimumSize(QSize(36, 36))
        self.btn_new.setMaximumSize(QSize(36, 36))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.btn_new.setFont(font3)
        self.btn_new.setFocusPolicy(Qt.NoFocus)
        self.btn_new.setStyleSheet(u"QPushButton#btn_new{\n"
                                    "	background-color: #0080ff ;\n"
                                    "	color: #fff;\n"
                                    "	border-radius: 5px;\n"
                                    "}\n"
                                    "QPushButton#btn_new:hover{\n"
                                    "	background-color:  #0073e6;\n"
                                    "}\n"
                                    "QPushButton#btn_new:pressed {\n"
                                    "	background-color: #0059b3;\n"
                                    "}\n"
                                    "QPushButton#btn_new:disabled {\n"
                                    "	background-color:  #a6a6a6;\n"
                                    "	color: #6a6767;\n"
                                    "}")
        icon7 = QIcon()
        icon7.addFile(resource_path(u"../img/new.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new.setIcon(icon7)
        self.btn_new.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.frm_user_actions_button)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)
        self.btn_save.setMinimumSize(QSize(36, 36))
        self.btn_save.setMaximumSize(QSize(36, 36))
        self.btn_save.setFont(font2)
        self.btn_save.setFocusPolicy(Qt.NoFocus)
        self.btn_save.setStyleSheet(u"QPushButton#btn_save {\n"
                                     "	background-color: #0080ff ;\n"
                                     "	color: #fff;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton#btn_save:hover{\n"
                                     "	background-color:  #0073e6;\n"
                                     "}\n"
                                     "QPushButton#btn_save:pressed {\n"
                                     "	background-color: #0059b3;\n"
                                     "}\n"
                                     "QPushButton#btn_save:disabled {\n"
                                     "	background-color:  #a6a6a6;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")
        icon8 = QIcon()
        icon8.addFile(resource_path(u"../img/save.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon8)
        self.btn_save.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_save)

        self.btn_edit = QPushButton(self.frm_user_actions_button)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setEnabled(False)
        self.btn_edit.setMinimumSize(QSize(36, 36))
        self.btn_edit.setMaximumSize(QSize(36, 36))
        self.btn_edit.setFont(font3)
        self.btn_edit.setFocusPolicy(Qt.NoFocus)
        self.btn_edit.setStyleSheet(u"QPushButton#btn_edit{\n"
                                     "	background-color: #0080ff ;\n"
                                     "	color: #fff;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton#btn_edit:hover{\n"
                                     "	background-color:  #0073e6;\n"
                                     "}\n"
                                     "QPushButton#btn_edit:pressed {\n"
                                     "	background-color: #0059b3;\n"
                                     "}\n"
                                     "QPushButton#btn_edit:disabled {\n"
                                     "	background-color:  #a6a6a6;\n"
                                     "	color: #6a6767;\n"
                                     "}")
        icon9 = QIcon()
        icon9.addFile(resource_path(u"../img/edit.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon9)
        self.btn_edit.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_edit)

        self.btn_cancel = QPushButton(self.frm_user_actions_button)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setEnabled(False)
        self.btn_cancel.setMinimumSize(QSize(36, 36))
        self.btn_cancel.setMaximumSize(QSize(36, 36))
        self.btn_cancel.setFont(font2)
        self.btn_cancel.setFocusPolicy(Qt.NoFocus)
        self.btn_cancel.setStyleSheet(u"QPushButton#btn_cancel{\n"
                                       "	background-color: #0080ff ;\n"
                                       "	color: #fff;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton#btn_cancel:hover{\n"
                                       "	background-color:  #0073e6;\n"
                                       "}\n"
                                       "QPushButton#btn_cancel:pressed {\n"
                                       "	background-color: #0059b3;\n"
                                       "}\n"
                                       "QPushButton#btn_cancel:disabled {\n"
                                       "	background-color:  #a6a6a6;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "}")
        icon10 = QIcon()
        icon10.addFile(resource_path(u"../img/cancel.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon10)
        self.btn_cancel.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_cancel)

        self.btn_delete = QPushButton(self.frm_user_actions_button)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setEnabled(False)
        self.btn_delete.setMinimumSize(QSize(36, 36))
        self.btn_delete.setMaximumSize(QSize(36, 36))
        self.btn_delete.setFont(font2)
        self.btn_delete.setFocusPolicy(Qt.NoFocus)
        self.btn_delete.setStyleSheet(u"QPushButton#btn_delete{\n"
                                       "	background-color: #0080ff ;\n"
                                       "	color: #fff;\n"
                                       "	border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton#btn_delete:hover{\n"
                                       "	background-color:  #0073e6;\n"
                                       "}\n"
                                       "QPushButton#btn_delete:pressed {\n"
                                       "	background-color: #0059b3;\n"
                                       "}\n"
                                       "QPushButton#btn_delete:disabled {\n"
                                       "	background-color:  #a6a6a6;\n"
                                       "	color: #6a6767;\n"
                                       "	border: 1px solid gray;\n"
                                       "}")
        icon11 = QIcon()
        icon11.addFile(resource_path(u"../img/delete.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon11)
        self.btn_delete.setIconSize(QSize(36, 36))

        self.hzl_botoes.addWidget(self.btn_delete)

        self.hls_between_button_action_and_border_user = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hzl_botoes.addItem(self.hls_between_button_action_and_border_user)

        self.vrl_content_user.addWidget(self.frm_user_actions_button)

        self.vls_between_button_actions_and_fields_user = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.vrl_content_user.addItem(self.vls_between_button_actions_and_fields_user)

        self.frm_content_fields_user = QFrame(self.frm_content_user)
        self.frm_content_fields_user.setObjectName(u"frm_content_fields_user")
        self.frm_content_fields_user.setMinimumSize(QSize(601, 461))
        self.frm_content_fields_user.setFrameShape(QFrame.StyledPanel)
        self.frm_content_fields_user.setFrameShadow(QFrame.Raised)

        self.grl_content_fields_user = QGridLayout(self.frm_content_fields_user)
        self.grl_content_fields_user.setObjectName(u"grl_content_fields_user")

        self.frm_field_user_right = QFrame(self.frm_content_fields_user)
        self.frm_field_user_right.setObjectName(u"frm_field_user_right")
        self.frm_field_user_right.setMinimumSize(QSize(318, 215))
        self.frm_field_user_right.setFrameShape(QFrame.StyledPanel)
        self.frm_field_user_right.setFrameShadow(QFrame.Raised)

        self.vrl_field_user_right = QVBoxLayout(self.frm_field_user_right)
        self.vrl_field_user_right.setSpacing(0)
        self.vrl_field_user_right.setObjectName(u"vrl_field_user_right")
        self.vrl_field_user_right.setContentsMargins(0, 0, 0, 0)

        self.lbl_email = QLabel(self.frm_field_user_right)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setMinimumSize(QSize(47, 16))
        self.lbl_email.setMaximumSize(QSize(47, 16))
        self.lbl_email.setFont(font1)
        self.lbl_email.setStyleSheet(u"QLabel {\n"
                                      "	color: #605D5D;\n"
                                      "}")

        self.vrl_field_user_right.addWidget(self.lbl_email)

        self.txt_email = QLineEdit(self.frm_field_user_right)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setMinimumSize(QSize(281, 20))
        self.txt_email.setFont(font)
        self.txt_email.setStyleSheet(u"QLineEdit#txt_email {\n"
                                      "	background-color: white;\n"
                                      "	color: #8C8C8C;\n"
                                      "	border: 1px solid #AFAEAE;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QLineEdit#txt_email:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_email:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")

        self.vrl_field_user_right.addWidget(self.txt_email)

        self.lbl_telephone = QLabel(self.frm_field_user_right)
        self.lbl_telephone.setObjectName(u"lbl_telephone")
        self.lbl_telephone.setMinimumSize(QSize(60, 16))
        self.lbl_telephone.setMaximumSize(QSize(60, 16))
        self.lbl_telephone.setFont(font1)
        self.lbl_telephone.setStyleSheet(u"QLabel {\n"
                                          "	color: #605D5D;\n"
                                          "}")

        self.vrl_field_user_right.addWidget(self.lbl_telephone)

        self.txt_telephone = QLineEdit(self.frm_field_user_right)
        self.txt_telephone.setObjectName(u"txt_telephone")
        self.txt_telephone.setMinimumSize(QSize(281, 20))
        self.txt_telephone.setFont(font)
        self.txt_telephone.setStyleSheet(u"QLineEdit#txt_telephone {\n"
                                          "	background-color: white;\n"
                                          "	color: #8C8C8C;\n"
                                          "	border: 1px solid #AFAEAE;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "QLineEdit#txt_telephone:focus{\n"
                                          "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                          "}\n"
                                          "QLineEdit#txt_telephone:disabled {\n"
                                          "	background-color:  #dcdcdc;\n"
                                          "	color: #6a6767;\n"
                                          "	border: 1px solid gray;\n"
                                          "}")

        self.vrl_field_user_right.addWidget(self.txt_telephone)

        self.lbl_password = QLabel(self.frm_field_user_right)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setMinimumSize(QSize(70, 16))
        self.lbl_password.setMaximumSize(QSize(70, 16))
        self.lbl_password.setFont(font1)
        self.lbl_password.setStyleSheet(u"QLabel {\n"
                                         "	color: #605D5D;\n"
                                         "}")

        self.vrl_field_user_right.addWidget(self.lbl_password)

        self.txt_password = QLineEdit(self.frm_field_user_right)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setMinimumSize(QSize(281, 20))
        font4 = QFont()
        font4.setFamily(u"Arial")
        self.txt_password.setFont(font4)
        self.txt_password.setStyleSheet(u"QLineEdit#txt_password {\n"
                                         "	background-color: white;\n"
                                         "	color: #8C8C8C;\n"
                                         "	border: 1px solid #AFAEAE;\n"
                                         "	border-radius: 5px;\n"
                                         "}\n"
                                         "QLineEdit#txt_password:focus{\n"
                                         "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                         "}\n"
                                         "QLineEdit#txt_password:disabled {\n"
                                         "	background-color:  #dcdcdc;\n"
                                         "	color: #6a6767;\n"
                                         "	border: 1px solid gray;\n"
                                         "}")
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.vrl_field_user_right.addWidget(self.txt_password)

        self.lbl_date_expires_password = QLabel(self.frm_field_user_right)
        self.lbl_date_expires_password.setObjectName(u"lbl_date_expires_password")
        self.lbl_date_expires_password.setMinimumSize(QSize(130, 16))
        self.lbl_date_expires_password.setMaximumSize(QSize(130, 16))
        self.lbl_date_expires_password.setFont(font1)
        self.lbl_date_expires_password.setStyleSheet(u"QLabel {\n"
                                                      "	color: #605D5D;\n"
                                                      "}")

        self.vrl_field_user_right.addWidget(self.lbl_date_expires_password)

        self.txt_date_expires_password = QLineEdit(self.frm_field_user_right)
        self.txt_date_expires_password.setObjectName(u"txt_date_expires_password")
        self.txt_date_expires_password.setMinimumSize(QSize(150, 20))
        self.txt_date_expires_password.setMaximumSize(QSize(150, 16777215))
        self.txt_date_expires_password.setFont(font4)
        self.txt_date_expires_password.setStyleSheet(u"QLineEdit#txt_date_expires_password{\n"
                                                      "	background-color: white;\n"
                                                      "	color: #8C8C8C;\n"
                                                      "	border: 1px solid #AFAEAE;\n"
                                                      "	border-radius: 5px;\n"
                                                      "}\n"
                                                      "QLineEdit#txt_date_expires_password:focus{\n"
                                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                      "}\n"
                                                      "QLineEdit#txt_date_expires_password:disabled {\n"
                                                      "	background-color:  #dcdcdc;\n"
                                                      "	color: #6a6767;\n"
                                                      "	border: 1px solid gray;\n"
                                                      "}")

        self.vrl_field_user_right.addWidget(self.txt_date_expires_password)

        self.lbl_cbx_situation = QLabel(self.frm_field_user_right)
        self.lbl_cbx_situation.setObjectName(u"lbl_cbx_situation")
        self.lbl_cbx_situation.setMinimumSize(QSize(70, 16))
        self.lbl_cbx_situation.setMaximumSize(QSize(70, 16))
        self.lbl_cbx_situation.setFont(font1)
        self.lbl_cbx_situation.setStyleSheet(u"QLabel {\n"
                                              "	color: #605D5D;\n"
                                              "}")

        self.vrl_field_user_right.addWidget(self.lbl_cbx_situation)

        self.cbx_situation = QComboBox(self.frm_field_user_right)
        self.cbx_situation.setObjectName(u"cbx_situation")
        self.cbx_situation.setMinimumSize(QSize(150, 20))
        self.cbx_situation.setMaximumSize(QSize(150, 16777215))
        self.cbx_situation.setFont(font)
        self.cbx_situation.setStyleSheet(u"QComboBox#cbx_situation {\n"
                                          "	background-color: #eeeeee;\n"
                                          "	color: #6a6767;\n"
                                          "	border: 1px solid gray;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "QComboBox#cbx_situation:focus{\n"
                                          "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                          "}\n"
                                          "QComboBox#cbx_situation:disabled {\n"
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

        self.vrl_field_user_right.addWidget(self.cbx_situation)

        self.grl_content_fields_user.addWidget(self.frm_field_user_right, 1, 2, 1, 1)

        self.vls_between_button_and_border_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_content_fields_user.addItem(self.vls_between_button_and_border_bottom, 5, 2, 1, 1)

        self.lbl_avatar = QLabel(self.frm_content_fields_user)
        self.lbl_avatar.setObjectName(u"lbl_avatar")
        self.lbl_avatar.setMinimumSize(QSize(281, 191))
        self.lbl_avatar.setMaximumSize(QSize(318, 214))
        self.lbl_avatar.setStyleSheet(u"QLabel#lbl_avatar {\n"
                                       "	border-width: 2px; \n"
                                       "	border-style: solid; \n"
                                       "	border-color: #CACACA;\n"
                                       "}")

        self.grl_content_fields_user.addWidget(self.lbl_avatar, 3, 2, 1, 1)

        self.frm_fields_user_left = QFrame(self.frm_content_fields_user)
        self.frm_fields_user_left.setObjectName(u"frm_fields_user_left")
        self.frm_fields_user_left.setMinimumSize(QSize(318, 215))
        self.frm_fields_user_left.setFrameShape(QFrame.StyledPanel)
        self.frm_fields_user_left.setFrameShadow(QFrame.Raised)

        self.vrl_fields_user_left = QVBoxLayout(self.frm_fields_user_left)
        self.vrl_fields_user_left.setSpacing(0)
        self.vrl_fields_user_left.setObjectName(u"vrl_fields_user_left")
        self.vrl_fields_user_left.setContentsMargins(0, 0, 0, 0)

        self.lbl_name = QLabel(self.frm_fields_user_left)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setMinimumSize(QSize(47, 16))
        self.lbl_name.setMaximumSize(QSize(47, 16))
        self.lbl_name.setFont(font1)
        self.lbl_name.setStyleSheet(u"QLabel {\n"
                                     "	color: #605D5D;\n"
                                     "}")

        self.vrl_fields_user_left.addWidget(self.lbl_name)

        self.txt_name = QLineEdit(self.frm_fields_user_left)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setMinimumSize(QSize(281, 20))
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet(u"QLineEdit#txt_name {\n"
                                     "	background-color: white;\n"
                                     "	color: #8C8C8C;\n"
                                     "	border: 1px solid #AFAEAE;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QLineEdit#txt_name:focus{\n"
                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                     "}\n"
                                     "QLineEdit#txt_name:disabled {\n"
                                     "	background-color:  #dcdcdc;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")

        self.vrl_fields_user_left.addWidget(self.txt_name)

        self.lbl_role = QLabel(self.frm_fields_user_left)
        self.lbl_role.setObjectName(u"lbl_role")
        self.lbl_role.setMinimumSize(QSize(47, 16))
        self.lbl_role.setMaximumSize(QSize(47, 16))
        self.lbl_role.setFont(font1)
        self.lbl_role.setStyleSheet(u"QLabel {\n"
                                     "	color: #605D5D;\n"
                                     "}")

        self.vrl_fields_user_left.addWidget(self.lbl_role)

        self.txt_role = QLineEdit(self.frm_fields_user_left)
        self.txt_role.setObjectName(u"txt_role")
        self.txt_role.setMinimumSize(QSize(281, 20))
        self.txt_role.setFont(font)
        self.txt_role.setStyleSheet(u"QLineEdit#txt_role{\n"
                                     "	background-color: white;\n"
                                     "	color: #8C8C8C;\n"
                                     "	border: 1px solid #AFAEAE;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QLineEdit#txt_role:focus{\n"
                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                     "}\n"
                                     "QLineEdit#txt_role:disabled {\n"
                                     "	background-color:  #dcdcdc;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")

        self.vrl_fields_user_left.addWidget(self.txt_role)

        self.lbl_user = QLabel(self.frm_fields_user_left)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setMinimumSize(QSize(70, 16))
        self.lbl_user.setMaximumSize(QSize(70, 16))
        self.lbl_user.setFont(font1)
        self.lbl_user.setStyleSheet(u"QLabel {\n"
                                     "	color: #605D5D;\n"
                                     "}")

        self.vrl_fields_user_left.addWidget(self.lbl_user)

        self.txt_user = QLineEdit(self.frm_fields_user_left)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setMinimumSize(QSize(281, 20))
        self.txt_user.setFont(font4)
        self.txt_user.setStyleSheet(u"QLineEdit#txt_user {\n"
                                     "	background-color: white;\n"
                                     "	color: #8C8C8C;\n"
                                     "	border: 1px solid #AFAEAE;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QLineEdit#txt_user:focus{\n"
                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                     "}\n"
                                     "QLineEdit#txt_user:disabled {\n"
                                     "	background-color:  #dcdcdc;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")

        self.vrl_fields_user_left.addWidget(self.txt_user)

        self.lbl_re_type_password = QLabel(self.frm_fields_user_left)
        self.lbl_re_type_password.setObjectName(u"lbl_re_type_password")
        self.lbl_re_type_password.setMinimumSize(QSize(111, 16))
        self.lbl_re_type_password.setMaximumSize(QSize(111, 16))
        self.lbl_re_type_password.setFont(font1)
        self.lbl_re_type_password.setStyleSheet(u"QLabel {\n"
                                                 "	color: #605D5D;\n"
                                                 "}")

        self.vrl_fields_user_left.addWidget(self.lbl_re_type_password)

        self.txt_re_type_password = QLineEdit(self.frm_fields_user_left)
        self.txt_re_type_password.setObjectName(u"txt_re_type_password")
        self.txt_re_type_password.setMinimumSize(QSize(281, 20))
        self.txt_re_type_password.setFont(font4)
        self.txt_re_type_password.setStyleSheet(u"QLineEdit#txt_re_type_password {\n"
                                                 "	background-color: white;\n"
                                                 "	color: #8C8C8C;\n"
                                                 "	border: 1px solid #AFAEAE;\n"
                                                 "	border-radius: 5px;\n"
                                                 "}\n"
                                                 "QLineEdit#txt_re_type_password:focus{\n"
                                                 "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                 "}\n"
                                                 "QLineEdit#txt_re_type_password:disabled {\n"
                                                 "	background-color:  #dcdcdc;\n"
                                                 "	color: #6a6767;\n"
                                                 "	border: 1px solid gray;\n"
                                                 "}")
        self.txt_re_type_password.setEchoMode(QLineEdit.Password)

        self.vrl_fields_user_left.addWidget(self.txt_re_type_password)

        self.lbl_type_user = QLabel(self.frm_fields_user_left)
        self.lbl_type_user.setObjectName(u"lbl_type_user")
        self.lbl_type_user.setMinimumSize(QSize(100, 16))
        self.lbl_type_user.setMaximumSize(QSize(100, 16))
        self.lbl_type_user.setFont(font1)
        self.lbl_type_user.setStyleSheet(u"QLabel {\n"
                                          "	color: #605D5D;\n"
                                          "}")

        self.vrl_fields_user_left.addWidget(self.lbl_type_user)

        self.cbx_type_user = QComboBox(self.frm_fields_user_left)
        self.cbx_type_user.setObjectName(u"cbx_type_user")
        self.cbx_type_user.setMinimumSize(QSize(150, 20))
        self.cbx_type_user.setMaximumSize(QSize(150, 16777215))
        self.cbx_type_user.setFont(font)
        self.cbx_type_user.setStyleSheet(u"QComboBox#cbx_type_user {\n"
                                          "	background-color: #eeeeee;\n"
                                          "	color: #6a6767;\n"
                                          "	border: 1px solid gray;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "QComboBox#cbx_type_user:focus{\n"
                                          "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                          "}\n"
                                          "QComboBox#cbx_type_user:disabled {\n"
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

        self.vrl_fields_user_left.addWidget(self.cbx_type_user)

        self.grl_content_fields_user.addWidget(self.frm_fields_user_left, 1, 1, 1, 1)

        self.hls_between_fields_right_and_border_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_fields_user.addItem(self.hls_between_fields_right_and_border_right, 1, 3, 1, 1)

        self.hls_between_border_and_fields_leth = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_fields_user.addItem(self.hls_between_border_and_fields_leth, 1, 0, 1, 1)

        self.btn_select_image_profile = QPushButton(self.frm_content_fields_user)
        self.btn_select_image_profile.setObjectName(u"btn_select_image_profile")
        self.btn_select_image_profile.setMinimumSize(QSize(151, 23))
        self.btn_select_image_profile.setMaximumSize(QSize(318, 23))
        self.btn_select_image_profile.setStyleSheet(u"QPushButton#btn_select_image_profile {\n"
                                                     "	background-color: #B2AFAF;\n"
                                                     "	color: white;\n"
                                                     "	border-radius: 5px;\n"
                                                     "}\n"
                                                     "QPushButton#btn_select_image_profile:hover {\n"
                                                     "	background-color:#9B9B9B;\n"
                                                     "}\n"
                                                     "QPushButton#btn_select_image_profile:pressed {\n"
                                                     "	background-color:#888888;\n"
                                                     "}")

        self.grl_content_fields_user.addWidget(self.btn_select_image_profile, 4, 2, 1, 1)

        self.vls_between_fields_and_photo_user = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.grl_content_fields_user.addItem(self.vls_between_fields_and_photo_user, 2, 2, 1, 1)

        self.vrl_content_user.addWidget(self.frm_content_fields_user)

        self.vrl_frm_content_user.addWidget(self.frm_content_user)

        QWidget.setTabOrder(self.txt_name, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_role)
        QWidget.setTabOrder(self.txt_role, self.txt_telephone)
        QWidget.setTabOrder(self.txt_telephone, self.txt_user)
        QWidget.setTabOrder(self.txt_user, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.txt_re_type_password)
        QWidget.setTabOrder(self.txt_re_type_password, self.txt_date_expires_password)
        QWidget.setTabOrder(self.txt_date_expires_password, self.cbx_type_user)
        QWidget.setTabOrder(self.cbx_type_user, self.cbx_situation)
        QWidget.setTabOrder(self.cbx_situation, self.btn_select_image_profile)

        self.retranslate_frm_user_content(frm_content)

        QMetaObject.connectSlotsByName(frm_content)

    def retranslate_frm_user_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Usu\u00e1rio", None))
        self.btn_navigation_first.setToolTip(QCoreApplication.translate("frm_content", u"Primeiro Registro", None))
        self.btn_navigation_first.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para ir ao primeiro registro</p></body></html>", None))
        self.btn_navigation_first.setText("")
        self.btn_navigation_first.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+Alt+Left", None))
        self.btn_navigation_previous.setToolTip(QCoreApplication.translate("frm_content", u"Registro Anterior", None))
        self.btn_navigation_previous.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para ir ao registro anterior</p></body></html>", None))
        self.btn_navigation_previous.setText("")
        self.btn_navigation_previous.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+Left", None))
        self.btn_navigation_next.setToolTip(QCoreApplication.translate("frm_content", u"Pr\u00f3xima Registro", None))
        self.btn_navigation_next.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para ir ao pr\u00f3ximo registro</p></body></html>", None))
        self.btn_navigation_next.setText("")
        self.btn_navigation_next.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+Right", None))
        self.btn_navigation_last.setToolTip(QCoreApplication.translate("frm_content", u"\u00daltima Registro", None))
        self.btn_navigation_last.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para ir ao ultimo registro</p></body></html>", None))
        self.btn_navigation_last.setText("")
        self.btn_navigation_last.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+Alt+Right", None))
        self.btn_search_register.setToolTip(QCoreApplication.translate("frm_content", u"Pesquisar", None))
        self.btn_search_register.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para pesquisar os registros de empresa</p></body></html>", None))
        self.btn_search_register.setText("")
        self.btn_search_register.setShortcut(QCoreApplication.translate("frm_content", u"F12", None))
        self.btn_print.setToolTip(QCoreApplication.translate("frm_content", u"Imprimir", None))
        self.btn_print.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para imprimir registro de empresa</p></body></html>", None))
        self.btn_print.setText("")
        self.btn_print.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+P", None))
        self.btn_copy.setToolTip(QCoreApplication.translate("frm_content", u"Duplicar", None))
        self.btn_copy.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para duplicar registro</p></body></html>", None))
        self.btn_copy.setText("")
        self.btn_new.setToolTip(QCoreApplication.translate("frm_content", u"Novo", None))
        self.btn_new.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para cadastrar uma novo registro de empresa</p></body></html>", None))
        self.btn_new.setText("")
        self.btn_new.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+N", None))
        self.btn_save.setToolTip(QCoreApplication.translate("frm_content", u"Salvar", None))
        self.btn_save.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para salvar o registro de empresa</p></body></html>", None))
        self.btn_save.setText("")
        self.btn_save.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+S", None))
        self.btn_edit.setToolTip(QCoreApplication.translate("frm_content", u"Editar", None))
        self.btn_edit.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para editar o registro de empresa</p></body></html>", None))
        self.btn_edit.setText("")
        self.btn_edit.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+E", None))
        self.btn_cancel.setToolTip(QCoreApplication.translate("frm_content", u"Cancelar", None))
        self.btn_cancel.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o para cancelar a opera\u00e7\u00e3o</p></body></html>", None))
        self.btn_cancel.setText("")
        self.btn_cancel.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+F", None))
        self.btn_delete.setToolTip(QCoreApplication.translate("frm_content", u"Deletar", None))
        self.btn_delete.setWhatsThis(QCoreApplication.translate("frm_content", u"<html><head/><body><p>Bot\u00e3o de deletar o registro de empresa</p></body></html>", None))
        self.btn_delete.setText("")
        self.btn_delete.setShortcut(QCoreApplication.translate("frm_content", u"Ctrl+D", None))
        self.lbl_email.setText(QCoreApplication.translate("frm_content", u"E-mail", None))
        self.lbl_telephone.setText(QCoreApplication.translate("frm_content", u"Telefone", None))
        self.lbl_password.setText(QCoreApplication.translate("frm_content", u"Senha", None))
        self.lbl_date_expires_password.setText(QCoreApplication.translate("frm_content", u"Data Expira\u00e7\u00e3o Senha", None))
        self.lbl_cbx_situation.setText(QCoreApplication.translate("frm_content", u"Situa\u00e7\u00e3o", None))
        self.lbl_avatar.setText("")
        self.lbl_name.setText(QCoreApplication.translate("frm_content", u"Nome", None))
        self.lbl_role.setText(QCoreApplication.translate("frm_content", u"Cargo", None))
        self.lbl_user.setText(QCoreApplication.translate("frm_content", u"Usu\u00e1rio", None))
        self.lbl_re_type_password.setText(QCoreApplication.translate("frm_content", u"Re-Digite a Senha ", None))
        self.lbl_type_user.setText(QCoreApplication.translate("frm_content", u"Tipo do Usu\u00e1rio", None))
        self.btn_select_image_profile.setText(QCoreApplication.translate("frm_content", u"Selecionar Imagem de Perfil", None))
    # retranslateUi

