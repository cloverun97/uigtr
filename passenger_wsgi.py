import imp
import os
import sys

import uigtr.wsgi
application = uigtr.wsgi.application

#sys.path.insert(0, os.path.dirname(__file__))

#wsgi = imp.load_source('wsgi', '')
#application = wsgi.application
