# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormProfileContent(object):

    def setup_frm_profile_content(self, frm_content):
        if not frm_content.objectName():
            frm_content.setObjectName(u"frm_content")
        frm_content.resize(682, 561)
        frm_content.setMinimumSize(QSize(682, 561))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        frm_content.setFont(font)
        frm_content.setStyleSheet(u"QFrame#frm_content{\n"
                                   "	background-color: #F5F5F5;\n"
                                   "   border-bottom-right-radius: 15px;"
                                   "}")

        self.vrl_frm_content_profile = QVBoxLayout(frm_content)
        self.vrl_frm_content_profile.setSpacing(0)
        self.vrl_frm_content_profile.setObjectName(u"vrl_frm_content_profile")
        self.vrl_frm_content_profile.setContentsMargins(0, 0, 0, 0)

        self.frm_content_profile = QFrame(frm_content)
        self.frm_content_profile.setObjectName(u"frm_content_profile")
        self.frm_content_profile.setMinimumSize(QSize(682, 561))
        font1 = QFont()
        font1.setPointSize(10)
        self.frm_content_profile.setFont(font1)
        self.frm_content_profile.setFrameShape(QFrame.StyledPanel)
        self.frm_content_profile.setFrameShadow(QFrame.Raised)

        self.grl_content_profile = QGridLayout(self.frm_content_profile)
        self.grl_content_profile.setObjectName(u"grl_content_profile")

        self.hls_between_border_and_header_profile = QSpacerItem(46, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.grl_content_profile.addItem(self.hls_between_border_and_header_profile, 2, 0, 1, 1)

        self.vls_between_border_and_content_fields_profile = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grl_content_profile.addItem(self.vls_between_border_and_content_fields_profile, 4, 1, 1, 1)

        self.tab_setting_user = QTabWidget(self.frm_content_profile)
        self.tab_setting_user.setObjectName(u"tab_setting_user")
        self.tab_setting_user.setMinimumSize(QSize(542, 435))
        self.tab_setting_user.setMaximumSize(QSize(542, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.tab_setting_user.setFont(font2)
        self.tab_setting_user.setStyleSheet(u"QTabWidget {\n"
                                             "	border: none;\n"
                                             "}\n"
                                             "QTabWidget QWidget{\n"
                                             "	background-color: #EEEEEE;\n"
                                             "}\n"
                                             "QTabBar::tab {\n"
                                             "	background-color:  #dcdcdc;\n"
                                             "    padding: 8 64 5 20;\n"
                                             "    color:  gray;\n"
                                             "	border-top-left-radius: 10px;\n"
                                             "	border-top-right-radius: 10px;\n"
                                             "	border-left: 1px solid lightgray;\n"
                                             "	border-right: 1px solid lightgray;\n"
                                             "}\n"
                                             "QTabBar::tab:hover {\n"
                                             "     background: #dcdcdc;\n"
                                             "}\n"
                                             "QTabBar::tab:selected {\n"
                                             "    background:  gray;\n"
                                             "    color: white;\n"
                                             "}")
        self.tab_setting_user.setDocumentMode(True)

        self.tab_information_user = QWidget()
        self.tab_information_user.setObjectName(u"tab_information_user")

        self.lbl_about = QLabel(self.tab_information_user)
        self.lbl_about.setObjectName(u"lbl_about")
        self.lbl_about.setGeometry(QRect(130, 230, 47, 16))
        self.lbl_about.setFont(font1)
        self.lbl_about.setStyleSheet(u"QLabel {\n"
                                      "	color: #605D5D;\n"
                                      "}")

        self.txt_role = QLineEdit(self.tab_information_user)
        self.txt_role.setObjectName(u"txt_role")
        self.txt_role.setGeometry(QRect(130, 140, 281, 20))
        self.txt_role.setFont(font1)
        self.txt_role.setStyleSheet(u"QLineEdit#txt_role {\n"
                                     "	background-color: white;\n"
                                     "	color: #8C8C8C;\n"
                                     "	border: 1px solid #AFAEAE;\n"
                                     "	border-radius: 5px;\n"
                                     "}"
                                     "QLineEdit#txt_role:focus{\n"
                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                     "}\n"
                                     "QLineEdit#txt_role:disabled {\n"
                                     "	background-color:  #dcdcdc;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")

        self.txt_about = QTextEdit(self.tab_information_user)
        self.txt_about.setObjectName(u"txt_about")
        self.txt_about.setGeometry(QRect(130, 250, 281, 81))
        self.txt_about.setFont(font1)
        self.txt_about.setStyleSheet(u"QTextEdit#txt_about {\n"
                                      "	background-color: white;\n"
                                      "	color: #8C8C8C;\n"
                                      "	border: 1px solid #AFAEAE;\n"
                                      "	border-radius: 5px;\n"
                                      "}"
                                      "QTextEdit#txt_about:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QTextEdit#txt_about:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")

        self.lbl_email = QLabel(self.tab_information_user)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(130, 70, 47, 16))
        self.lbl_email.setFont(font1)
        self.lbl_email.setStyleSheet(u"QLabel {\n"
                                      "	color: #605D5D;\n"
                                      "}")

        self.lbl_role = QLabel(self.tab_information_user)
        self.lbl_role.setObjectName(u"lbl_role")
        self.lbl_role.setGeometry(QRect(130, 120, 47, 16))
        self.lbl_role.setFont(font1)
        self.lbl_role.setStyleSheet(u"QLabel {\n"
                                     "	color: #605D5D;\n"
                                     "}")

        self.txt_telephone = QLineEdit(self.tab_information_user)
        self.txt_telephone.setObjectName(u"txt_telephone")
        self.txt_telephone.setGeometry(QRect(130, 190, 281, 20))
        self.txt_telephone.setFont(font1)
        self.txt_telephone.setStyleSheet(u"QLineEdit#txt_telephone {\n"
                                          "	background-color: white;\n"
                                          "	color: #8C8C8C;\n"
                                          "	border: 1px solid #AFAEAE;\n"
                                          "	border-radius: 5px;\n"
                                          "}"
                                          "QLineEdit#txt_telephone:focus{\n"
                                          "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                          "}\n"
                                          "QLineEdit#txt_telephone:disabled {\n"
                                          "	background-color:  #dcdcdc;\n"
                                          "	color: #6a6767;\n"
                                          "	border: 1px solid gray;\n"
                                          "}")

        self.lbl_telephone = QLabel(self.tab_information_user)
        self.lbl_telephone.setObjectName(u"lbl_telephone")
        self.lbl_telephone.setGeometry(QRect(130, 170, 60, 16))
        self.lbl_telephone.setFont(font1)
        self.lbl_telephone.setStyleSheet(u"QLabel {\n"
                                          "	color: #605D5D;\n"
                                          "}")

        self.txt_name = QLineEdit(self.tab_information_user)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setGeometry(QRect(130, 40, 281, 20))
        self.txt_name.setFont(font1)
        self.txt_name.setStyleSheet(u"QLineEdit#txt_name {\n"
                                     "	background-color: white;\n"
                                     "	color: #8C8C8C;\n"
                                     "	border: 1px solid #AFAEAE;\n"
                                     "	border-radius: 5px;\n"
                                     "}"
                                     "QLineEdit#txt_name:focus{\n"
                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                     "}\n"
                                     "QLineEdit#txt_name:disabled {\n"
                                     "	background-color:  #dcdcdc;\n"
                                     "	color: #6a6767;\n"
                                     "	border: 1px solid gray;\n"
                                     "}")

        self.lbl_name = QLabel(self.tab_information_user)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(130, 20, 47, 16))
        self.lbl_name.setFont(font1)
        self.lbl_name.setStyleSheet(u"QLabel {\n"
                                     "	color: #605D5D;\n"
                                     "}")

        self.txt_email = QLineEdit(self.tab_information_user)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(130, 90, 281, 20))
        self.txt_email.setFont(font1)
        self.txt_email.setStyleSheet(u"QLineEdit#txt_email {\n"
                                      "	background-color: white;\n"
                                      "	color: #8C8C8C;\n"
                                      "	border: 1px solid #AFAEAE;\n"
                                      "	border-radius: 5px;\n"
                                      "}"
                                      "QLineEdit#txt_email:focus{\n"
                                      "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                      "}\n"
                                      "QLineEdit#txt_email:disabled {\n"
                                      "	background-color:  #dcdcdc;\n"
                                      "	color: #6a6767;\n"
                                      "	border: 1px solid gray;\n"
                                      "}")

        self.btn_save_profile = QPushButton(self.tab_information_user)
        self.btn_save_profile.setObjectName(u"btn_save_profile")
        self.btn_save_profile.setGeometry(QRect(340, 340, 70, 31))
        self.btn_save_profile.setMinimumSize(QSize(70, 31))
        self.btn_save_profile.setMaximumSize(QSize(70, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_save_profile.setFont(font3)
        self.btn_save_profile.setStyleSheet(u"QPushButton#btn_save_profile {\n"
                                             "	background-color: #2FB7F3;\n"
                                             "	color: white;\n"
                                             "	border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton#btn_save_profile:hover {\n"
                                             "	background-color:#009CE1;\n"
                                             "}\n"
                                             "QPushButton#btn_save_profile:pressed {\n"
                                             "	background-color:#0082BC;\n"
                                             "}")
        self.btn_save_profile.setIconSize(QSize(10, 10))

        self.tab_setting_user.addTab(self.tab_information_user, "")

        self.tab_change_avatar = QWidget()
        self.tab_change_avatar.setObjectName(u"tab_change_avatar")

        self.lbl_avatar = QLabel(self.tab_change_avatar)
        self.lbl_avatar.setObjectName(u"lbl_avatar")
        self.lbl_avatar.setGeometry(QRect(130, 30, 281, 191))
        self.lbl_avatar.setStyleSheet(u"QLabel#lbl_avatar {\n"
                                       "	border-width: 2px; \n"
                                       "	border-style: solid; \n"
                                       "	border-color: #CACACA;\n"
                                       "}")

        self.btn_select_image_profile = QPushButton(self.tab_change_avatar)
        self.btn_select_image_profile.setObjectName(u"btn_select_image_profile")
        self.btn_select_image_profile.setGeometry(QRect(260, 224, 151, 23))
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

        self.btn_save_avatar = QPushButton(self.tab_change_avatar)
        self.btn_save_avatar.setObjectName(u"btn_save_avatar")
        self.btn_save_avatar.setGeometry(QRect(340, 270, 70, 31))
        self.btn_save_avatar.setMinimumSize(QSize(70, 31))
        self.btn_save_avatar.setMaximumSize(QSize(70, 31))
        self.btn_save_avatar.setFont(font3)
        self.btn_save_avatar.setStyleSheet(u"QPushButton#btn_save_avatar {\n"
                                            "	background-color: #2FB7F3;\n"
                                            "	color: white;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton#btn_save_avatar:hover {\n"
                                            "	background-color:#009CE1;\n"
                                            "}\n"
                                            "QPushButton#btn_save_avatar:pressed {\n"
                                            "	background-color:#0082BC;\n"
                                            "}")
        self.btn_save_avatar.setIconSize(QSize(10, 10))

        self.tab_setting_user.addTab(self.tab_change_avatar, "")

        self.tab_change_password = QWidget()
        self.tab_change_password.setObjectName(u"tab_change_password")

        self.txt_current_password = QLineEdit(self.tab_change_password)
        self.txt_current_password.setObjectName(u"txt_current_password")
        self.txt_current_password.setGeometry(QRect(130, 40, 281, 20))
        self.txt_current_password.setStyleSheet(u"QLineEdit#txt_current_password {\n"
                                                 "	background-color: white;\n"
                                                 "	color: #8C8C8C;\n"
                                                 "	border: 1px solid #AFAEAE;\n"
                                                 "	border-radius: 5px;\n"
                                                 "}"
                                                 "QLineEdit#txt_current_password:focus{\n"
                                                 "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                 "}\n"
                                                 "QLineEdit#txt_current_password:disabled {\n"
                                                 "	background-color:  #dcdcdc;\n"
                                                 "	color: #6a6767;\n"
                                                 "	border: 1px solid gray;\n"
                                                 "}")
        self.txt_current_password.setEchoMode(QLineEdit.Password)

        self.lbl_re_type_new_password = QLabel(self.tab_change_password)
        self.lbl_re_type_new_password.setObjectName(u"lbl_re_type_new_password")
        self.lbl_re_type_new_password.setGeometry(QRect(130, 120, 140, 16))
        self.lbl_re_type_new_password.setFont(font1)
        self.lbl_re_type_new_password.setStyleSheet(u"QLabel {\n"
                                                     "	color: #605D5D;\n"
                                                     "}")

        self.txt_re_type_new_password = QLineEdit(self.tab_change_password)
        self.txt_re_type_new_password.setObjectName(u"txt_re_type_new_password")
        self.txt_re_type_new_password.setGeometry(QRect(130, 140, 281, 20))
        self.txt_re_type_new_password.setStyleSheet(u"QLineEdit#txt_re_type_new_password {\n"
                                                     "	background-color: white;\n"
                                                     "	color: #8C8C8C;\n"
                                                     "	border: 1px solid #AFAEAE;\n"
                                                     "	border-radius: 5px;\n"
                                                     "}"
                                                     "QLineEdit#txt_re_type_new_password:focus{\n"
                                                     "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                                     "}\n"
                                                     "QLineEdit#txt_re_type_new_password:disabled {\n"
                                                     "	background-color:  #dcdcdc;\n"
                                                     "	color: #6a6767;\n"
                                                     "	border: 1px solid gray;\n"
                                                     "}")
        self.txt_re_type_new_password.setEchoMode(QLineEdit.Password)

        self.lbl_new_password = QLabel(self.tab_change_password)
        self.lbl_new_password.setObjectName(u"lbl_new_password")
        self.lbl_new_password.setGeometry(QRect(130, 70, 70, 16))
        self.lbl_new_password.setFont(font1)
        self.lbl_new_password.setStyleSheet(u"QLabel {\n"
                                             "	color: #605D5D;\n"
                                             "}")

        self.txt_new_password = QLineEdit(self.tab_change_password)
        self.txt_new_password.setObjectName(u"txt_new_password")
        self.txt_new_password.setGeometry(QRect(130, 90, 281, 20))
        self.txt_new_password.setStyleSheet(u"QLineEdit#txt_new_password {\n"
                                             "	background-color: white;\n"
                                             "	color: #8C8C8C;\n"
                                             "	border: 1px solid #AFAEAE;\n"
                                             "	border-radius: 5px;\n"
                                             "}"
                                             "QLineEdit#txt_new_password:focus{\n"
                                             "	border: 2px solid rgba(81, 203, 238, 1);\n"
                                             "}\n"
                                             "QLineEdit#txt_new_password:disabled {\n"
                                             "	background-color:  #dcdcdc;\n"
                                             "	color: #6a6767;\n"
                                             "	border: 1px solid gray;\n"
                                             "}")
        self.txt_new_password.setEchoMode(QLineEdit.Password)

        self.lbl_current_password = QLabel(self.tab_change_password)
        self.lbl_current_password.setObjectName(u"lbl_current_password")
        self.lbl_current_password.setGeometry(QRect(130, 20, 70, 16))
        self.lbl_current_password.setFont(font1)
        self.lbl_current_password.setStyleSheet(u"QLabel {\n"
                                                 "	color: #605D5D;\n"
                                                 "}")

        self.btn_save_password = QPushButton(self.tab_change_password)
        self.btn_save_password.setObjectName(u"btn_save_password")
        self.btn_save_password.setGeometry(QRect(340, 180, 70, 31))
        self.btn_save_password.setMinimumSize(QSize(70, 31))
        self.btn_save_password.setMaximumSize(QSize(70, 31))
        self.btn_save_password.setFont(font3)
        self.btn_save_password.setStyleSheet(u"QPushButton#btn_save_password {\n"
                                              "	background-color: #2FB7F3;\n"
                                              "	color: white;\n"
                                              "	border-radius: 5px;\n"
                                              "}\n"
                                              "QPushButton#btn_save_password:hover {\n"
                                              "	background-color:#009CE1;\n"
                                              "}\n"
                                              "QPushButton#btn_save_password:pressed {\n"
                                              "	background-color:#0082BC;\n"
                                              "}")
        self.btn_save_password.setIconSize(QSize(10, 10))

        self.tab_setting_user.addTab(self.tab_change_password, "")

        self.grl_content_profile.addWidget(self.tab_setting_user, 3, 1, 1, 1)

        self.frm_header_profile = QFrame(self.frm_content_profile)
        self.frm_header_profile.setObjectName(u"frm_header_profile")
        self.frm_header_profile.setMinimumSize(QSize(541, 111))
        self.frm_header_profile.setMaximumSize(QSize(16777215, 111))
        self.frm_header_profile.setFrameShape(QFrame.StyledPanel)
        self.frm_header_profile.setFrameShadow(QFrame.Raised)

        self.lbl_email_user = QLabel(self.frm_header_profile)
        self.lbl_email_user.setObjectName(u"lbl_email_user")
        self.lbl_email_user.setGeometry(QRect(220, 59, 315, 16))
        self.lbl_email_user.setMinimumSize(QSize(315, 16))
        self.lbl_email_user.setMaximumSize(QSize(315, 16))
        self.lbl_email_user.setFont(font1)
        self.lbl_email_user.setStyleSheet(u"QLabel#lbl_email_user {\n"
                                           "	color: #605D5D;\n"
                                           "}")

        self.lbl_type_user = QLabel(self.frm_header_profile)
        self.lbl_type_user.setObjectName(u"lbl_type_user")
        self.lbl_type_user.setGeometry(QRect(220, 80, 315, 16))
        self.lbl_type_user.setMinimumSize(QSize(315, 16))
        self.lbl_type_user.setMaximumSize(QSize(315, 16))
        self.lbl_type_user.setFont(font1)
        self.lbl_type_user.setStyleSheet(u"QLabel#lbl_type_user {\n"
                                          "	color: #605D5D;\n"
                                          "}")

        self.lbl_photo_profile = QLabel(self.frm_header_profile)
        self.lbl_photo_profile.setObjectName(u"lbl_photo_profile")
        self.lbl_photo_profile.setGeometry(QRect(40, -2, 111, 111))
        self.lbl_photo_profile.setMinimumSize(QSize(111, 111))
        self.lbl_photo_profile.setMaximumSize(QSize(111, 111))
        self.lbl_photo_profile.setStyleSheet(u"QLabel#lbl_photo_profile {\n"
                                              "	background: transparent;\n"
                                              "	border-radius: 55px;\n"
                                              "}")
        img = QImage()
        img.load(u"D:/Anps010/Documents/Projetos/Help Desk/img/profile_user.jpg", "JPG")
        self.lbl_photo_profile.resize(img.width(), img.height())
        pixmap = QPixmap(img.width(), img.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        clipPath = QPainterPath()
        clipPath.addRoundedRect(QRectF(img.rect()), img.width() // 2, img.width() // 2)
        painter.setClipPath(clipPath)
        painter.drawPixmap(0, 0, QPixmap(img))
        painter.end()
        self.lbl_photo_profile.setPixmap(pixmap)
        self.lbl_photo_profile.setScaledContents(True)
        self.lbl_photo_profile.setAlignment(Qt.AlignCenter)
        self.lbl_photo_profile.setMargin(3)

        self.lbl_name_user = QLabel(self.frm_header_profile)
        self.lbl_name_user.setObjectName(u"lbl_name_user")
        self.lbl_name_user.setGeometry(QRect(220, 20, 315, 31))
        self.lbl_name_user.setMinimumSize(QSize(315, 31))
        self.lbl_name_user.setMaximumSize(QSize(315, 31))
        font4 = QFont()
        font4.setPointSize(20)
        self.lbl_name_user.setFont(font4)
        self.lbl_name_user.setStyleSheet(u"QLabel#lbl_name_user {\n"
                                          "	color: #605D5D;\n"
                                          "}")

        self.grl_content_profile.addWidget(self.frm_header_profile, 1, 1, 2, 1)

        self.hls_between_header_and_border_profile = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_profile.addItem(self.hls_between_header_and_border_profile, 1, 2, 1, 1)

        self.hls_between_border_content_field_profile = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_profile.addItem(self.hls_between_border_content_field_profile, 3, 0, 1, 1)

        self.hls_between_content_field_and_border_profile = QSpacerItem(53, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grl_content_profile.addItem(self.hls_between_content_field_and_border_profile, 3, 2, 1, 1)

        self.vls_between_border_and_header_profile = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.grl_content_profile.addItem(self.vls_between_border_and_header_profile, 0, 1, 1, 1)

        self.vrl_frm_content_profile.addWidget(self.frm_content_profile)

        QWidget.setTabOrder(self.tab_setting_user, self.txt_name)
        QWidget.setTabOrder(self.txt_name, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_role)
        QWidget.setTabOrder(self.txt_role, self.txt_telephone)
        QWidget.setTabOrder(self.txt_telephone, self.txt_about)
        QWidget.setTabOrder(self.txt_about, self.btn_select_image_profile)
        QWidget.setTabOrder(self.btn_select_image_profile, self.btn_save_avatar)
        QWidget.setTabOrder(self.btn_save_avatar, self.txt_current_password)
        QWidget.setTabOrder(self.txt_current_password, self.txt_new_password)
        QWidget.setTabOrder(self.txt_new_password, self.txt_re_type_new_password)
        QWidget.setTabOrder(self.txt_re_type_new_password, self.btn_save_password)
        QWidget.setTabOrder(self.btn_save_password, self.btn_save_profile)

        self.retranslate_frm_profile_content(frm_content)

        self.tab_setting_user.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_content)
    # setupUi

    def retranslate_frm_profile_content(self, frm_content):
        frm_content.setWindowTitle(QCoreApplication.translate("frm_content", u"Perfil", None))
        self.lbl_about.setText(QCoreApplication.translate("frm_content", u"Sobre", None))
        self.lbl_email.setText(QCoreApplication.translate("frm_content", u"E-mail", None))
        self.lbl_role.setText(QCoreApplication.translate("frm_content", u"Cargo", None))
        self.lbl_telephone.setText(QCoreApplication.translate("frm_content", u"Telefone", None))
        self.lbl_name.setText(QCoreApplication.translate("frm_content", u"Nome", None))
        self.btn_save_profile.setText(QCoreApplication.translate("frm_content", u"Salve", None))
        self.tab_setting_user.setTabText(self.tab_setting_user.indexOf(self.tab_information_user), QCoreApplication.translate("frm_content", u"Informa\u00e7\u00f5es Pessoais", None))
        self.lbl_avatar.setText("")
        self.btn_select_image_profile.setText(QCoreApplication.translate("frm_content", u"Selecionar Imagem de Perfil", None))
        self.btn_save_avatar.setText(QCoreApplication.translate("frm_content", u"Salve", None))
        self.tab_setting_user.setTabText(self.tab_setting_user.indexOf(self.tab_change_avatar), QCoreApplication.translate("frm_content", u"Alterar Avatar", None))
        self.lbl_re_type_new_password.setText(QCoreApplication.translate("frm_content", u"Re-Digite a Nova Senha ", None))
        self.lbl_new_password.setText(QCoreApplication.translate("frm_content", u"Nova Senha ", None))
        self.lbl_current_password.setText(QCoreApplication.translate("frm_content", u"Senha Atual", None))
        self.btn_save_password.setText(QCoreApplication.translate("frm_content", u"Salve", None))
        self.tab_setting_user.setTabText(self.tab_setting_user.indexOf(self.tab_change_password), QCoreApplication.translate("frm_content", u"Alterar Senha", None))
        self.lbl_email_user.setText(QCoreApplication.translate("frm_content", u"jefferson_sadoski@hotmail.com", None))
        self.lbl_type_user.setText(QCoreApplication.translate("frm_content", u"Administrador", None))
        self.lbl_photo_profile.setText("")
        self.lbl_name_user.setText(QCoreApplication.translate("frm_content", u"Jefferson Apa. Sadoski", None))
    # retranslateUi

