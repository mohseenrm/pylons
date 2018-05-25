# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527207436.856455
_enable_loop = True
_template_filename = '/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/basic_test.html'
_template_uri = '/basic_test.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<h1>Greetings</h1>\n\n<p>')
        __M_writer(escape(c.greeting))
        __M_writer(u' ')
        __M_writer(escape(c.name))
        __M_writer(u'!</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Greetings')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 2, "35": 5, "36": 5, "37": 5, "38": 5, "44": 2, "48": 2, "54": 48, "28": 0}, "uri": "/basic_test.html", "filename": "/Users/mohseenmukaddam/Projects/pylons/TemplateTest/templatetest/templates/basic_test.html"}
__M_END_METADATA
"""
