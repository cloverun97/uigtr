"""
WSGI config for uigtr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
#import myproject.wsgi

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uigtr.settings")

application = get_wsgi_application()

#application = myproject.wsgi.application

# Replace myproject with your project’s module name.
