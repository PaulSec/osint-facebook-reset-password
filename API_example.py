#!/bin/python
# coding: utf-8

from FacebookResetPasswordAPI import FacebookResetPasswordAPI
res = FacebookResetPasswordAPI({'verbose': True}).get('email@domain.com')
print res  # retrieves the results
