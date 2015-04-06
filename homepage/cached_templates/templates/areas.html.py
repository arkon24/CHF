# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427918537.592989
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/areas.html'
_template_uri = 'areas.html'
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
        areas = context.get('areas', UNDEFINED)
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
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n</div>\n\n<table id="items_table" class="table table-striped table-bordered">\n    <tr>\n        <th>Area Name</th>\n        <th>Description</th>\n        <th>Coordinator</th>\n        <th>Supervisor</th>\n        <th>Event Name</th>\n    </tr>\n')
        for area in areas:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(area.aname))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(area.description))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(area.coordinator))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(area.supervisor))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(area.event ))
            __M_writer('</td>\n\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 22, "65": 22, "66": 26, "35": 1, "40": 28, "46": 3, "59": 19, "72": 66, "53": 3, "54": 16, "55": 17, "56": 18, "57": 18, "58": 19, "27": 0, "60": 20, "61": 20, "62": 21, "63": 21}, "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/areas.html", "uri": "areas.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
