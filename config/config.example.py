# -*- coding: utf-8 -*-
"""
Copy this file to config/__init__.py
"""
# -------------------------------------------------
# Server Config
# -------------------------------------------------
ROOT_PATH = ''
DEBUG = True
PORT = 6006
# If production environment, different from DEBUG
PRODUCTION = False


# -------------------------------------------------
# Email Config 用于发送报错邮件给管理员
# -------------------------------------------------
EMAIL_HOST = 'smtp.126.com'
EMAIL_ADDR = 'xgiton@126.com'
EMAIL_SUBJECT = 'Base Project'
EMAIL_PWD = ''
ADMINS = ['xiaozhidong@jaxus.com']
