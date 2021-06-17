# -*- coding: utf-8 -*-
"""
Modulo do controle de ações e visualizações da Conteudo para a criação do Ticket
"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from form.form_content_create_ticket import FormCreateTicketContent
from form.form_chat_message_receiver import FormChatMessageReceived
from form.form_chat_message_sent import FormChatMessageSent
from form.form_chat_message_receiver import FormChatMessageReceived


class CreateTicketContent(FormCreateTicketContent):
    resized = Signal()

    def set_form_create_ticket_content(self, frame: QFrame):
        super(CreateTicketContent, self).setup_frm_create_ticket_content(frame)
        self.main.lbl_title.setText("Abrir Ticket")
        #self.insert_message_chat_receiver()
        #self.insert_message_chat_sent()
        self.btn_submit.clicked.connect(self.submit_message)


    def submit_message_re(self):
        received = FormChatMessageReceived()
        text = self.txt_message.toPlainText()
        received.lbl_message_chat_received.setText(text)
        self.vrl_content_message_ticket.removeItem(self.vls_between_message_chat_and_border_bottom)
        self.vrl_content_message_ticket.addWidget(received)
        self.vrl_content_message_ticket.addItem(self.vls_between_message_chat_and_border_bottom)

    def submit_message(self):
        sent = FormChatMessageSent()
        text_ = str(self.txt_message.toPlainText())
        text = ("Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara ")
        print(text_)
        print(text)
        #sent.lbl_message_chat_sent.setTextFormat(0)
        sent.lbl_message_chat_sent.setText((text_))
        sent.lbl_message_chat_sent.adjustSize()


        self.vrl_content_message_ticket.removeItem(self.vls_between_message_chat_and_border_bottom)
        self.vrl_content_message_ticket.addWidget(sent)
        self.vrl_content_message_ticket.addItem(self.vls_between_message_chat_and_border_bottom)

    def insert_message_chat_sent(self):
        sent = FormChatMessageSent()
        #text = "Você é lindo cara Você é lindo cara"
        text = ("Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara Você é lindo cara ")
        sent.lbl_message_chat_sent.setText(text)

        self.vrl_content_message_ticket.removeItem(self.vls_between_message_chat_and_border_bottom)
        self.vrl_content_message_ticket.addWidget(sent)
        self.vrl_content_message_ticket.addItem(self.vls_between_message_chat_and_border_bottom)

    def insert_message_chat_receiver(self):
        receiver = FormChatMessageReceived()
        text = ("Muito Obrigado cara")
        receiver.lbl_message_chat_received.setText(text)
        receiver.lbl_message_chat_received.setWordWrap(True)

        self.vrl_content_message_ticket.removeItem(self.vls_between_message_chat_and_border_bottom)
        self.vrl_content_message_ticket.addWidget(receiver)
        self.vrl_content_message_ticket.addItem(self.vls_between_message_chat_and_border_bottom)


class ScaledLabel(QLabel):
    def resizeEvent(self, event: QResizeEvent):
        # This flag is used for pixmaps, but I thought it might be useful to
        # disable font scaling. Remove the check if you don't like it.
        if not self.hasScaledContents():
            return

        target_rect = self.contentsRect()
        text = self.text()

        # Use binary search to efficiently find the biggest font that will fit.
        max_size = self.height()
        min_size = 1
        font = self.font()
        while 1 < max_size - min_size:
            new_size = (min_size + max_size) // 2
            font.setPointSize(new_size)
            metrics = QFontMetrics(font)

            # Be careful which overload of boundingRect() you call.
            rect = metrics.boundingRect(target_rect, Qt.AlignLeft, text)
            if (rect.width() > target_rect.width() or
                    rect.height() > target_rect.height()):
                max_size = new_size
            else:
                min_size = new_size

        font.setPointSize(min_size)
        self.setFont(font)