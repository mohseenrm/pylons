# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527207436.97156
_enable_loop = True
_template_filename = u'/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/base.html'
_template_uri = u'/base.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n    <head>\n        <title>')
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    </head>\n    <body>\n        ')
        __M_writer(escape(self.body()))
        __M_writer(u'\n        <div class="footer">\n            <p>This is a simple page footer</p>\n        </div>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 27, "17": 0, "23": 1, "24": 3, "25": 3, "26": 6, "27": 6}, "uri": "/base.html", "filename": "/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/base.html"}
__M_END_METADATA
"""
