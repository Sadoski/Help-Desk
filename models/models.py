# -*- coding: utf-8 -*-
"""
Modulo específico da estrutura das tabelas do banco de dados para sua manipulação
"""
import uuid
from datetime import datetime
from sqlalchemy import BINARY, BLOB, Boolean, Column, Date, DateTime, DECIMAL, ForeignKey, Integer, Numeric, String, \
                       Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy.types as types
from sqlalchemy.dialects.mysql import BIT


BASE = declarative_base()
mysql_engine = 'InnoDB',
mariadb_engine = 'InnoDB',
mysql_charset = 'utf8mb4',
mariadb_charset = 'utf8',


class DateTimeUTC(types.TypeDecorator):
    impl = datetime
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not value.tzinfo:
                raise TypeError("tzinfo is required")
            value = value.astimezone(datetime.timezone.utc).replace(
                tzinfo=None
            )
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        return value


class ChoiceType(types.TypeDecorator):

    impl = types.String

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.items() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class User(BASE):

    """
        Classe da estrutura da tabela "user" do banco de dados
        Herança:
            - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                    utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
        Parâmetro:
            - __tablename__: nome da tabela no banco de dados do tipo texto
            - id_user: index da usuario, representando a coluna, do tipo inteiro, chave primaria,
                           autoincrementado, nunca nulo
            - name_user: nome completo do usuário, representando a coluna, do tipo texto, de tamanho 75
            - email: endereço de e-mail, representando a coluna, do tipo texto, de tamanho 255
            - avatar = binário da imagem do usuário, representando a coluna, do tipo texto
            - role = função do usuário, representando a coluna, do tipo texto, de tamanho 255
            - login: nome de login, representando a coluna, do tipo texto, de tamanho 10
            - password: senha do login, representando a coluna, do tipo texto, de tamnaho 255
            - password_expires: data de expiração da senha, representando a coluna, do tipo texto, do tipo data
            - last_seen : data e hora do ultimo visualização, representando a coluna, do tipo data e hora
            - situation: situação do registo (0 - Inativo, 1 - Ativo), representando a coluna, do tipo inteiro,
                         com valor default 1
            - user_created_id: index do usuário que criou o registro, representando a coluna, do tipo inteiro,
                               chave estrangeira
            - created: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
            - modification: data e hora de modificação, representando a coluna, do tipo data e hora
        """

    __tablename__ = 'user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_unicode_ci'}
    id_user = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(75), nullable=False)
    email = Column(String(255), unique=True)
    avatar = Column(BLOB)
    role = Column(String(255))
    about = Column(Text)
    telephone = Column(String(11))
    user = Column(String(10), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    password_expires = Column(DateTime)
    last_seen = Column(DateTime)
    situation = Column(BINARY, nullable=False, default=1)
    user_created_id = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_user_who_created_user'), index=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    modification = Column(DateTime, onupdate=datetime.utcnow)


class Department(BASE):
    __tablename__ = 'department'
    id_department = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    department = Column(String(200), nullable=False)


class Status(BASE):
    __tablename__ = 'status'
    id_status = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    status = Column(String(200), nullable=False)


class Ticket(BASE):
    Open = 1
    In_Analysis = 2
    On_Hold = 3
    Resolved = 4
    ReOpened = 5
    Closed = 6
    Duplicate = 7

    STATUS_CHOICES = {
        "Open": "Aberto",
        "In_Analysis": "Em Análise",
        "On_Hold": "Em Espera",
        "Resolved": "Resolvido",
        "ReOpened": "Reaberto",
        "Closed": "Fechado",
        "Duplicate": "Duplicado",
    }

    PRIORITY_CHOICES = {
        "Critical": "Crítico",
        "High": "Alto",
        "Normal": "Normal",
        "Low": "Baixo",
        "Very Low": "Muito Baixo"
    }

    __tablename__ = 'ticket'
    id_ticket = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(200), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    modification = Column(DateTime, onupdate=datetime.utcnow)
    closed = Column(DateTime)
    status = Column(ChoiceType(STATUS_CHOICES), default="Open")
    priority = Column(ChoiceType(PRIORITY_CHOICES), default=3, blank=3)
    removed = Column(Boolean, default=False)
    merged_to = Column(Integer, ForeignKey('ticket.id_ticket', onupdate="CASCADE", ondelete="CASCADE",
                                            name='fk_id_ticket_duplicate_on_ticket'), index=True)
    user_created_id = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                                 name='fk_id_user_who_created_ticket'), index=True)
    user_following_id = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                                   name='fk_id_user_who_following_ticket'), index=True)


class Comments(BASE):

    __tablename__ = 'comments'
    id_comments = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ticket_id = Column(Integer, ForeignKey('ticket.id_ticket', onupdate="CASCADE", ondelete="CASCADE",
                                            name='fk_id_ticket_in_comments'), index=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    removed = Column(Boolean, default=False)
    user = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                      name='fk_id_user_who_created_comments'), index=True)
    comment = Column(Text, nullable=False)


class FilesAttachments(BASE):

    __tablename__ = 'files_attachments'
    id_files_attachments = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ticket_id = Column(Integer, ForeignKey('ticket.id_ticket', onupdate="CASCADE", ondelete="CASCADE",
                                            name='fk_id_ticket_in_comments'), index=True)
    name = Column(Text, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                      name='fk_id_user_who_created_file'), index=True)
    size = Column(Integer, nullable=False)
    contents = Column(BLOB, nullable=False)


class Tags(BASE):

    __tablename__ = 'tags'
    id_tag = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    tag = Column(String(30), nullable=False)
    user_created_id = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                                 name='fk_id_user_who_created_tag'), index=True)


class ChatMessage(BASE):
    __tablename__ = 'chat_message'
    id_chat_message = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_created_id = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                                 name='fk_id_user_who_created_chat'), index=True)
    recipient = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="RESTRICT",
                                            name='fk_id_user_who_created_recipient'), index=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    read_date = Column(DateTime)
    room = Column(String(150))
    body = Column(Text, nullable=False)
    broadcast = Column(Boolean, default=False)


class SavedSearch(BASE):

    user_id = Column(Integer, ForeignKey('user.id_user', onupdate="CASCADE", ondelete="CASCADE",
                                          name='fk_id_user_in_saved_search'), index=True)
    title = Column(String(100))
    query = Column(String(200))

"""
def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        params = {k: v for k, v in kwargs.items() if not isinstance(v, ClauseElement)}
        params.update(defaults or {})
        instance = model(**params)
        try:
            session.add(instance)
            session.commit()
        except Exception:  # The actual exception depends on the specific database so we catch all exceptions. This is similar to the official documentation: https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True
            
 Python 3.9+           
def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(Model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance
    else:
        kwargs |= defaults or {}
        instance = model(**params)
        try:
            session.add(instance)
            session.commit()
        except Exception:  # The actual exception depends on the specific database so we catch all exceptions. This is similar to the official documentation: https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True            
"""