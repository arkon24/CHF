# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423357143.928055
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/crud.html'
_template_uri = 'crud.html'
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
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<body>\n\n <table class="table table-striped table-bordered">\n     <tr>\n         <th>Create, Read, Edit, or Delete for:</th>\n     </tr>\n     <tr>\n        <td><a href="http://localhost:8000/homepage/users/">Users</a></td>\n     </tr>\n        <td><a href="http://localhost:8000/homepage/events/">Events</a></td>\n     <tr>\n        <td><a href="http://localhost:8000/homepage/items/">Items</a></td>\n     </tr>\n        <td><a href="http://localhost:8000/homepage/participants/">Participants</a></td>\n     <tr>\n         <td><a href="http://localhost:8000/homepage/phones/">Phone Numbers</a></td>\n     </tr>\n         <td><a href="http://localhost:8000/homepage/products/">Products</a></td>\n </table>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/lukewilliam17/test_dmp/homepage/templates/crud.html", "source_encoding": "ascii", "uri": "crud.html", "line_map": {"51": 5, "34": 1, "35": 4, "57": 51, "27": 0, "45": 5}}
__M_END_METADATA
"""
