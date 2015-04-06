# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425672564.408881
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/account.editpassword.html'
_template_uri = 'account.editpassword.html'
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
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
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
        __M_writer('\n    Please enter new password\n  <form method ="POST">\n   <table>\n    ')
        __M_writer(str( form ))
        __M_writer('\n   </table>\n    <button type="submit" class="btn btn-primary">Submit</button>\n        <a href="/homepage/account/" class=" btn btn-danger">Cancel</a>\n  </form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "53": 3, "54": 7, "55": 7, "40": 13, "27": 0, "61": 55, "46": 3}, "uri": "account.editpassword.html", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/account.editpassword.html"}
__M_END_METADATA
"""
