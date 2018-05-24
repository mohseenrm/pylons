# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527135246.208165
_enable_loop = True
_template_filename = '/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/context.html'
_template_uri = '/context.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n    <body>\n        ')

        context.write('<p>Here is an example:</p>')
                
        
        __M_writer(u'\n        <p>\n')
        for key in context.keys():
            __M_writer(u'        The key is <tt>')
            __M_writer(escape(key))
            __M_writer(u'</tt>, the value is ')
            __M_writer(escape(str(context.get(key))))
            __M_writer(u'. <br />\n')
        __M_writer(u'        </p>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 8, "33": 8, "34": 8, "35": 10, "41": 35, "17": 0, "23": 1, "24": 3, "28": 5, "29": 7, "30": 8, "31": 8}, "uri": "/context.html", "filename": "/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/context.html"}
__M_END_METADATA
"""
