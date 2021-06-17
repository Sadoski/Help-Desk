# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo das Tags
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_tags import FormTagsContent


class TagsContent(FormTagsContent):

    def set_form_tags_content(self, frame: QFrame):
        super(TagsContent, self).setup_frm_tags_content(frame)
        self.main.lbl_title.setText("Tags")
