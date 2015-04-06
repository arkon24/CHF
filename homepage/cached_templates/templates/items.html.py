# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425566441.016789
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n<a href ="/homepage/items.create/" class="btn btn-warning">Create New Item</a>\n</div>\n\n<table id="items_table" class="table table-striped table-bordered">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Value</th>\n        <th>Standard Rental Price</th>\n        <th>User</th>\n        <th>Actions</th>\n    </tr>\n')
        for item in items:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n    <td>')
            __M_writer(str(item.name))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(item.description))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(item.value))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(item.standardRentalPrice))
            __M_writer(' </td>\n    <td>')
            __M_writer(str( item.user ))
            __M_writer('</td>\n\n    <td>\n        <a href = "/homepage/items.edit/')
            __M_writer(str( item.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit</a>\n    </td>\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "items.html", "source_encoding": "ascii", "line_map": {"64": 25, "65": 25, "66": 26, "67": 26, "68": 29, "69": 29, "70": 33, "76": 70, "27": 0, "35": 1, "40": 35, "46": 3, "53": 3, "54": 19, "55": 20, "56": 21, "57": 21, "58": 22, "59": 22, "60": 23, "61": 23, "62": 24, "63": 24}, "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/items.html"}
__M_END_METADATA
"""
