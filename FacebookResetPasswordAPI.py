#!/bin/python
# coding: utf-8

"""
Python util to retrieve Facebook profile from an email address.
Using this code, you can the full name + profile picture from any account using the email address. 
"""

import requests
from bs4 import BeautifulSoup
import re


class FacebookResetPasswordAPI(object):

    """
        FacebookResetPasswordAPI Main Handler
    """

    _instance = None
    _verbose = False

    def __init__(self, arg=None):
        pass

    def __new__(cls, *args, **kwargs):
        """
            __new__ builtin
        """
        if not cls._instance:
            cls._instance = super(FacebookResetPasswordAPI, cls).__new__(
                cls, *args, **kwargs)
            if (args and args[0] and args[0]['verbose']):
                cls._verbose = True
        return cls._instance

    def display_message(self, s):
        if (self._verbose):
            print '[verbose] %s' % s

    def get(self, email):
        s = requests.Session()
        req = s.get('https://www.facebook.com/login/identify?ctx=recover&lwv=110')

        # retrieve token
        pattern = r'"token":"([a-zA-Z0-9_-]+)"'
        token = re.findall(pattern, req.content)[0]
        if not token:
            self.display_message('[!] token not found')
            return []
        self.display_message('Token retrieved: %s' % token)

        # retrieve jsdatr
        pattern = r'"_js_datr","([a-zA-Z0-9_-]+)"'
        jsdatr = re.findall(pattern, req.content)[0]
        if not jsdatr:
            self.display_message('[!] jsdatr not found')
            return []
        self.display_message('jsdatr retrieved: %s' % jsdatr)

        # setting payload
        data = {'lsd': token,
                'email': email,
                'did_submit': 'Search',
                '__user': 0,
                '__a': 1}
        # setting cookie
        cookies = {'_js_datr': jsdatr + ';'}
        # setting headers
        headers = {'referer': 'https://www.facebook.com/login/identify?ctx=recover&lwv=110'}
        # sending the request and retrieving the data
        req = s.post('https://www.facebook.com/ajax/login/help/identify.php?ctx=recover', cookies=cookies, data=data, headers=headers)

        # retrieving link
        pattern = r'ldata=([a-zA-Z0-9-_]+)\\"'
        ldata = re.findall(pattern, req.content)[0]
        if not ldata:
            self.display_message('[!] ldata not found')
            return []

        req = s.get('https://www.facebook.com/recover/initiate?ldata=%s' % ldata)
        soup = BeautifulSoup(req.content)
        full_name = soup.find('div', attrs={'class': 'fsl fwb fcb'})
        profile_picture = soup.find('img', attrs={'class': 'img'})
        return {'full_name': full_name.text, 'profile_picture': profile_picture['src']}