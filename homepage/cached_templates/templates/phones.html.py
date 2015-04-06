# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423282576.750856
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/phones.html'
_template_uri = 'phones.html'
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
        phones = context.get('phones', UNDEFINED)
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
        phones = context.get('phones', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n<a href ="/homepage/phones.create/" class="btn btn-warning">Create New Phone</a>\n</div>\n\n<table id="phones_table" class="table table-striped table-bordered">\n    <tr>\n        <th>ID</th>\n        <th>Number</th>\n        <th>Extension</th>\n        <th>Type</th>\n        <th>User</th>\n        <th>Actions</th>\n    </tr>\n')
        for phone in phones:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(phone.id))
            __M_writer('</td>\n    <td>')
            __M_writer(str(phone.number))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(phone.extension))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(phone.type))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(phone.user))
            __M_writer('</td>\n\n    <td>\n        <a href = "/homepage/phones.edit/')
            __M_writer(str( phone.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit</a>\n    </td>\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "phones.html", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/phones.html", "source_encoding": "ascii", "line_map": {"64": 24, "65": 24, "66": 27, "35": 1, "68": 31, "40": 33, "74": 68, "46": 3, "59": 21, "67": 27, "53": 3, "54": 18, "55": 19, "56": 20, "57": 20, "58": 21, "27": 0, "60": 22, "61": 22, "62": 23, "63": 23}}
__M_END_METADATA
"""
