# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423357051.912545
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<body>\n\n <div class="content">\n      <h3>Contact Info</h3>\n      <p>Call this number!</p>\n      <p class="server-time">888-888-8888</p>\n\n </div>\n\n<div class="form-group">\n    <label for="exampleInputEmail1">Email address</label>\n    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter email">\n  </div>\n\n</body>\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/lukewilliam17/test_dmp/homepage/templates/contact.html", "source_encoding": "ascii", "uri": "contact.html", "line_map": {"34": 1, "35": 4, "52": 5, "40": 24, "58": 52, "27": 0, "46": 5}}
__M_END_METADATA
"""
