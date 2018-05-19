import logging

from pylons import app_globals, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from hola.lib.base import BaseController, render

import hola.lib.helpers as h

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/hello.mako')
        # or, return a string
        response.content_type = 'text/plain'
        return 'Hello from index()'

    def environ(self):
        response.content_type = 'text/plain'
        return h.format_environ(request.environ)

    def app_global_test(self):
        app_globals.visits += 1
        return 'Number of visitors so far: %s' % app_globals.visits