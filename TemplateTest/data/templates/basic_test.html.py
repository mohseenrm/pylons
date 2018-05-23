# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527119626.544855
_enable_loop = True
_template_filename = '/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/basic_test.html'
_template_uri = '/basic_test.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n    <title>Basic Template Test</title>\n</head>\n<body>\n    <h1>Greetings</h1>\n    <p>Hello ')
        __M_writer(escape(name))
        __M_writer(u'!</p>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 7, "17": 0, "31": 25, "25": 7, "23": 1}, "uri": "/basic_test.html", "filename": "/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/basic_test.html"}
__M_END_METADATA
"""
