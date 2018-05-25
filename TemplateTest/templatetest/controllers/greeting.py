import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from templatetest.lib.base import BaseController

import templatetest.lib.helpers as h

from pylons.templating import render_mako as render

log = logging.getLogger(__name__)

class GreetingController(BaseController):

    def index(self):
        c.greeting = h.literal('<b>Welcome</b>')
        c.name = request.params.get('name', 'Visitor')
        return render('/basic_test.html')

    def context(self):
        return render('/context.html')