# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425535259.853631
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="content">\n  <h3>This is the home page</h3>\n  <h4>Please use the links on the left to navigate the website</h4>\n\n</div>\n  <div id =\'loginform_container\' align="center">\n    <form id="loginform" method="POST" action="/homepage/index.loginform/">\n      <table>\n        ')
        __M_writer(str( form ))
        __M_writer('\n      </table>\n      <input type ="submit"/>\n    </form>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/index.html", "line_map": {"35": 1, "52": 2, "53": 12, "54": 12, "27": 0, "60": 54, "45": 2}, "source_encoding": "ascii"}
__M_END_METADATA
"""
