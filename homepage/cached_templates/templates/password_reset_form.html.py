# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427941237.482465
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/password_reset_form.html'
_template_uri = 'password_reset_form.html'
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
        csrf_token = context.get('csrf_token', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        csrf_token = context.get('csrf_token', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<p>Please specify your email address to receive instructions for resetting it.</p>\n\n<form action="" method="POST">\n    <div style="display:none">\n        <input type="hidden" value=')
        __M_writer(str( csrf_token ))
        __M_writer(' name="csrfmiddlewaretoken">\n    </div>\n     ')
        __M_writer(str( form.email.errors ))
        __M_writer('\n    <p><label for="id_email">E-mail address:</label> {{ form.email }} <input type="submit" value="Reset password" /></p>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 59, "59": 10, "36": 1, "57": 8, "55": 3, "56": 8, "41": 13, "58": 10, "27": 0, "47": 3}, "uri": "password_reset_form.html", "source_encoding": "ascii", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/password_reset_form.html"}
__M_END_METADATA
"""
