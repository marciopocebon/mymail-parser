#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

LOGIN = 'LOGIN'        # ������� �����
PASSWORD = 'PASSWORD'  # ������� ������


Credentials = namedtuple('Credentials', [
	'login',
	'password'
])

mymail = Credentials(LOGIN, PASSWORD)
