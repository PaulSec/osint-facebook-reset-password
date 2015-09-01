Facebook Reset Password API
================

Quick utility to retrieve full display name and profile picture from a simple e-mail address (if the privacy settings have not been configured properly). 

Usage
======

```python
#!/bin/python
# coding: utf-8

from FacebookResetPasswordAPI import FacebookResetPasswordAPI
res = FacebookResetPasswordAPI({'verbose': True}).get('email@domail.com')
print res  # retrieves the results
```

And the result looks something like: 

```
[verbose] Token retrieved: AVpvxQbb
[verbose] jsdatr retrieved: UPrlVd-aKAWKxxxXAAPwJ7wz
{'profile_picture': 'https://www.facebook.com/profile/pic.php?cuid=AYhEUfs4ayVJXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'full_name': u'Paul XXXXXXXXXX'}
```

Contributing
======

Feel free to contribute or ping me on [Twitter](https://www.twitter.com/paulwebsec) if you find a bug. 
Cheers!