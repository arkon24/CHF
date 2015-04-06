# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428092590.315609
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/checkout.html'
_template_uri = 'checkout.html'
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
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if user.is_authenticated() :
            __M_writer('\n    <form method="POST">\n   <table>\n    ')
            __M_writer(str( form ))
            __M_writer('\n   </table>\n    <br>\n    <button type="submit" class="btn btn-primary">Purchase</button>\n\n  </form>\n\n\n')
        else:
            __M_writer('       <div id="login">\n            <strong>You will need to login first in order to checkout, thank you.</strong>\n       </div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "36": 1, "46": 3, "67": 61, "54": 3, "55": 5, "56": 6, "57": 9, "58": 9, "59": 17, "60": 18, "61": 22}, "source_encoding": "ascii", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/checkout.html", "uri": "checkout.html"}
__M_END_METADATA
"""
