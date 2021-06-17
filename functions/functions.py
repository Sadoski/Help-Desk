# -*- coding: utf-8 -*-
"""
Funções padroes da aplicação
"""
import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Função para retornar o caminho  absoluto do item
    Parâmetros:
        - relative_path: nome do item.
    Retorno:
        - Retornar a caminho abosluto do item
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def clear_layout(layout):
    """
    Procedimento para limpar conteudo do layout
    Parâmetro:
        - layout: compo do layout
    """
    def delete_items(layout_):
        """
        Procedimento para deletar conteudo do layout
        Parâmetro:
            - layout: compo do layout
        """
        if layout_ is not None:
            while layout_.count():
                item = layout_.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    delete_items(item.layout())
    delete_items(layout) #chama a função delete_items


def clear_fields_form(form):
    """
     Procedimento para limpar o canteudo de um formulário
     Parâmetro:
        - form: campo formulário
    """
    for i in range(len(form.children())):
        form.children()[i].deleteLater()
'''
class MyLabel(QLabel):
    def paintEvent( self, event ):
        painter = QPainter(self)

        metrics = QFontMetrics(self.font())
        elided  = metrics.elidedText(self.text(), Qt.ElideRight, self.width())

        painter.drawText(self.rect(), self.alignment(), elided)
'''