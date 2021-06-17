# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormSettingsMenu(object):

    def setup_frm_settings_menu(self, frm_menu):
        if not frm_menu.objectName():
            frm_menu.setObjectName(u"frm_menu")
        frm_menu.resize(200, 563)
        frm_menu.setMinimumSize(QSize(200, 563))
        frm_menu.setMaximumSize(QSize(200, 16777215))
        frm_menu.setStyleSheet(u"QFrame#frm_menu {\n"
                                "	background-color: #DBDBDB;\n"
                                "}")

        self.vrl_settings_menu = QVBoxLayout(frm_menu)
        self.vrl_settings_menu.setSpacing(0)
        self.vrl_settings_menu.setObjectName(u"vrl_settings_menu")
        self.vrl_settings_menu.setContentsMargins(0, 0, 0, 0)

        self.frm_settings_menu = QFrame(frm_menu)
        self.frm_settings_menu.setObjectName(u"frm_settings_menu")
        self.frm_settings_menu.setMinimumSize(QSize(200, 563))
        self.frm_settings_menu.setMaximumSize(QSize(200, 16777215))
        self.frm_settings_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_settings_menu.setFrameShadow(QFrame.Raised)

        self.frl_setting_menu = QFormLayout(self.frm_settings_menu)
        self.frl_setting_menu.setObjectName(u"frl_setting_menu")
        self.frl_setting_menu.setHorizontalSpacing(0)
        self.frl_setting_menu.setVerticalSpacing(0)
        self.frl_setting_menu.setContentsMargins(0, 0, 0, 0)

        self.hls_between_border_left_and_search_in_settings = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.frl_setting_menu.setItem(2, QFormLayout.LabelRole, self.hls_between_border_left_and_search_in_settings)

        self.txt_search_settings = QLineEdit(self.frm_settings_menu)
        self.txt_search_settings.setObjectName(u"txt_search_settings")
        self.txt_search_settings.setMinimumSize(QSize(181, 28))
        self.txt_search_settings.setMaximumSize(QSize(181, 28))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.txt_search_settings.setFont(font)
        self.txt_search_settings.setFocusPolicy(Qt.ClickFocus)
        self.txt_search_settings.setStyleSheet(u"QLineEdit#txt_search_settings{\n"
                                                "	background-color: #F1F1F1;\n"
                                                "	color: #8C8C8C;\n"
                                                "	border: 1px solid #AFAEAE;\n"
                                                "	border-radius: 5px;\n"
                                                "}")
        self.txt_search_settings.setMaxLength(40)

        self.frl_setting_menu.setWidget(2, QFormLayout.FieldRole, self.txt_search_settings)

        self.btn_profile = QPushButton(self.frm_settings_menu)
        self.btn_profile.setObjectName(u"btn_profile")
        self.btn_profile.setMinimumSize(QSize(200, 30))
        self.btn_profile.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.btn_profile.setFont(font1)
        self.btn_profile.setStyleSheet(u"QPushButton#btn_profile {\n"
                                        "	text-align:left;\n"
                                        "	text-decoration: none;\n"
                                        "	margin-left: 20px;\n"
                                        "	border: none;\n"
                                        "	color: #555555;\n"
                                        "}\n"
                                        "QPushButton#btn_profile:hover {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_profile:pressed {\n"
                                        "	color: #00B1FF;\n"
                                        "	text-decoration: none;\n"
                                        "}\n"
                                        "QPushButton#btn_profile:focus {\n"
                                        "    color: #00B1FF;\n"
                                        "	text-decoration: underline;\n"
                                        "}")
        self.btn_profile.setIconSize(QSize(0, 0))

        self.frl_setting_menu.setWidget(5, QFormLayout.SpanningRole, self.btn_profile)

        self.btn_settings = QPushButton(self.frm_settings_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(200, 30))
        self.btn_settings.setMaximumSize(QSize(200, 30))
        self.btn_settings.setFont(font1)
        self.btn_settings.setStyleSheet(u"QPushButton#btn_settings {\n"
                                         "	text-align:left;\n"
                                         "	text-decoration: none;\n"
                                         "	margin-left: 20px;\n"
                                         "	border: none;\n"
                                         "	color: #555555;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:hover {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:pressed {\n"
                                         "	color: #00B1FF;\n"
                                         "	text-decoration: none;\n"
                                         "}\n"
                                         "QPushButton#btn_settings:focus {\n"
                                         "    color: #00B1FF;\n"
                                         "	text-decoration: underline;\n"
                                         "}")
        self.btn_settings.setIconSize(QSize(0, 0))

        self.frl_setting_menu.setWidget(8, QFormLayout.SpanningRole, self.btn_settings)

        self.btn_user = QPushButton(self.frm_settings_menu)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setMinimumSize(QSize(200, 30))
        self.btn_user.setMaximumSize(QSize(200, 30))
        self.btn_user.setFont(font1)
        self.btn_user.setStyleSheet(u"QPushButton#btn_user {\n"
                                     "	text-align:left;\n"
                                     "	text-decoration: none;\n"
                                     "	margin-left: 20px;\n"
                                     "	border: none;\n"
                                     "	color: #555555;\n"
                                     "}\n"
                                     "QPushButton#btn_user:hover {\n"
                                     "	color: #00B1FF;\n"
                                     "	text-decoration: none;\n"
                                     "}\n"
                                     "QPushButton#btn_user:pressed {\n"
                                     "	color: #00B1FF;\n"
                                     "	text-decoration: none;\n"
                                     "}\n"
                                     "QPushButton#btn_user:focus {\n"
                                     "    color: #00B1FF;\n"
                                     "	text-decoration: underline;\n"
                                     "}")
        self.btn_user.setIconSize(QSize(0, 0))

        self.frl_setting_menu.setWidget(11, QFormLayout.SpanningRole, self.btn_user)

        self.btn_group = QPushButton(self.frm_settings_menu)
        self.btn_group.setObjectName(u"btn_group")
        self.btn_group.setMinimumSize(QSize(200, 30))
        self.btn_group.setMaximumSize(QSize(200, 30))
        self.btn_group.setFont(font1)
        self.btn_group.setStyleSheet(u"QPushButton#btn_group {\n"
                                      "	text-align:left;\n"
                                      "	text-decoration: none;\n"
                                      "	margin-left: 20px;\n"
                                      "	border: none;\n"
                                      "	color: #555555;\n"
                                      "}\n"
                                      "QPushButton#btn_group:hover {\n"
                                      "	color: #00B1FF;\n"
                                      "	text-decoration: none;\n"
                                      "}\n"
                                      "QPushButton#btn_group:pressed {\n"
                                      "	color: #00B1FF;\n"
                                      "	text-decoration: none;\n"
                                      "}\n"
                                      "QPushButton#btn_group:focus {\n"
                                      "    color: #00B1FF;\n"
                                      "	text-decoration: underline;\n"
                                      "};")
        self.btn_group.setIconSize(QSize(0, 0))

        self.frl_setting_menu.setWidget(14, QFormLayout.SpanningRole, self.btn_group)

        self.btn_department = QPushButton(self.frm_settings_menu)
        self.btn_department.setObjectName(u"btn_department")
        self.btn_department.setMinimumSize(QSize(200, 30))
        self.btn_department.setMaximumSize(QSize(200, 30))
        self.btn_department.setFont(font1)
        self.btn_department.setStyleSheet(u"QPushButton#btn_department {\n"
                                           "	text-align:left;\n"
                                           "	text-decoration: none;\n"
                                           "	margin-left: 20px;\n"
                                           "	border: none;\n"
                                           "	color: #555555;\n"
                                           "}\n"
                                           "QPushButton#btn_department:hover {\n"
                                           "	color: #00B1FF;\n"
                                           "	text-decoration: none;\n"
                                           "}\n"
                                           "QPushButton#btn_department:pressed {\n"
                                           "	color: #00B1FF;\n"
                                           "	text-decoration: none;\n"
                                           "}\n"
                                           "QPushButton#btn_department:focus {\n"
                                           "    color: #00B1FF;\n"
                                           "	text-decoration: underline;\n"
                                           "};")
        self.btn_department.setIconSize(QSize(0, 0))

        self.frl_setting_menu.setWidget(17, QFormLayout.SpanningRole, self.btn_department)

        self.btn_tags = QPushButton(self.frm_settings_menu)
        self.btn_tags.setObjectName(u"btn_tags")
        self.btn_tags.setMinimumSize(QSize(200, 30))
        self.btn_tags.setMaximumSize(QSize(200, 30))
        self.btn_tags.setFont(font1)
        self.btn_tags.setStyleSheet(u"QPushButton#btn_tags {\n"
                                     "	text-align:left;\n"
                                     "	text-decoration: none;\n"
                                     "	margin-left: 20px;\n"
                                     "	border: none;\n"
                                     "	color: #555555;\n"
                                     "}\n"
                                     "QPushButton#btn_tags:hover {\n"
                                     "	color: #00B1FF;\n"
                                     "	text-decoration: none;\n"
                                     "}\n"
                                     "QPushButton#btn_tags:pressed {\n"
                                     "	color: #00B1FF;\n"
                                     "	text-decoration: none;\n"
                                     "}\n"
                                     "QPushButton#btn_tags:focus {\n"
                                     "    color: #00B1FF;\n"
                                     "	text-decoration: underline;\n"
                                     "};")
        self.btn_tags.setIconSize(QSize(0, 0))

        self.frl_setting_menu.setWidget(20, QFormLayout.SpanningRole, self.btn_tags)

        self.vsl_between_buttom_and_border_in_setting = QSpacerItem(184, 317, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.frl_setting_menu.setItem(23, QFormLayout.FieldRole, self.vsl_between_buttom_and_border_in_setting)

        self.vls_between_border_top_and_search_in_settings = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.frl_setting_menu.setItem(1, QFormLayout.FieldRole, self.vls_between_border_top_and_search_in_settings)

        self.vls_between_search_and_buttom_in_setting = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.frl_setting_menu.setItem(4, QFormLayout.FieldRole, self.vls_between_search_and_buttom_in_setting)

        self.vrl_settings_menu.addWidget(self.frm_settings_menu)

        self.retranslate_settings_menu(frm_menu)

        QMetaObject.connectSlotsByName(frm_menu)

    def retranslate_settings_menu(self, frm_menu):
        frm_menu.setWindowTitle("")
        self.txt_search_settings.setStatusTip(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_settings.setWhatsThis(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_settings.setAccessibleName(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_settings.setAccessibleDescription(QCoreApplication.translate("frm_menu", u"Pesquisar", None))
        self.txt_search_settings.setText("")
        self.txt_search_settings.setPlaceholderText(QCoreApplication.translate("frm_menu", u" Pesquisar", None))
        self.btn_profile.setText(QCoreApplication.translate("frm_menu", u"Perfil", None))
        self.btn_settings.setText(QCoreApplication.translate("frm_menu", u"Configura\u00e7\u00f5es", None))
        self.btn_user.setText(QCoreApplication.translate("frm_menu", u"Usu\u00e1rio", None))
        self.btn_group.setText(QCoreApplication.translate("frm_menu", u"Grupos", None))
        self.btn_department.setText(QCoreApplication.translate("frm_menu", u"Departamento", None))
        self.btn_tags.setText(QCoreApplication.translate("frm_menu", u"Tags", None))

