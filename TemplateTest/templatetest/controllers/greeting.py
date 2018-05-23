import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from templatetest.lib.base import BaseController

from pylons.templating import render_mako as render

log = logging.getLogger(__name__)

class GreetingController(BaseController):

    def index(self):
        name =  'Mohseen'
        return render(
            '/basic_test.html',
            extra_vars={'name': name}
        )
