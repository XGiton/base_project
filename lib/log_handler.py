# -*- coding: utf-8 -*-
"""
Define different log handler here
"""
from config import EMAIL_HOST, EMAIL_ADDR, EMAIL_SUBJECT, EMAIL_PWD, ADMINS
from config.default_celery import celery_app
from logging import Handler, Filter, Formatter, WARNING, ERROR, INFO
from logging.handlers import SMTPHandler, HTTPHandler


class CustomSMTPHandler(SMTPHandler):
    """
    程序报错时, 给管理员发送报错提醒
    """
    def __init__(self, mailhost, fromaddr, toaddrs, subject,
                 credentials=None, secure=None):
        SMTPHandler.__init__(self, mailhost, fromaddr, toaddrs, subject,
                             credentials, secure)

    def emit(self, record):
        """
        Override handler for sending async error emails
        """
        from email.utils import formatdate
        msg = self.format(record)
        msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
            self.fromaddr,
            ",".join(self.toaddrs),
            self.getSubject(record),
            formatdate(),
            msg)
        celery_app.send_task(
            'send_error_email',
            (
                self.mailhost,
                self.mailport,
                self.fromaddr,
                self.toaddrs,
                self.subject,
            ),
            {
                'username': self.username,
                'password': self.password,
                'msg': msg,
                'secure': self.secure,
            },
        )


# create a smtp handler
mailer = CustomSMTPHandler(EMAIL_HOST,
                           EMAIL_ADDR,
                           ADMINS,
                           EMAIL_SUBJECT,
                           (EMAIL_ADDR, EMAIL_PWD))
mailer.setFormatter(Formatter(
    '''
    Message type:    %(levelname)s
    Location:        %(pathname)s:%(lineno)d
    Module:          %(module)s
    Function:        %(funcName)s
    Time:            %(asctime)s
    Message:         %(message)s
    '''
))
mailer.setLevel(WARNING)
