# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425768150.069187
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/account.edit.html'
_template_uri = 'account.edit.html'
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
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
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
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <form method ="POST">\n   <table>\n    ')
        __M_writer(str( form ))
        __M_writer('\n   </table>\n    <button type="submit" class="btn btn-primary">Submit</button>\n')
        if request.user.is_authenticated():
            __M_writer('        <a href="/homepage/account.delete/')
            __M_writer(str( user.id ))
            __M_writer('/" class=" btn btn-danger">Delete</a>\n')
        else:
            __M_writer('        <a href="/homepage/account.delete/')
            __M_writer(str( user.id ))
            __M_writer('/" class=" btn btn-danger">Cancel</a>\n')
        __M_writer('  </form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/lukewilliam17/test_dmp/homepage/templates/account.edit.html", "uri": "account.edit.html", "source_encoding": "ascii", "line_map": {"64": 12, "65": 13, "66": 13, "27": 0, "68": 15, "37": 1, "42": 17, "48": 3, "67": 13, "74": 68, "57": 3, "58": 7, "59": 7, "60": 10, "61": 11, "62": 11, "63": 11}}
__M_END_METADATA
"""
