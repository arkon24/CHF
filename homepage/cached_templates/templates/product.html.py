# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427916275.18434
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/product.html'
_template_uri = 'product.html'
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
        products = context.get('products', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<table id="products_table" class="table table-striped table-bordered">\n    <tr>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Price</th>\n    </tr>\n')
        for product in products:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(product.name))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(product.description))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(product.price))
            __M_writer(' </td>\n\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "68": 62, "40": 21, "46": 3, "59": 14, "53": 3, "54": 11, "55": 12, "56": 13, "57": 13, "58": 14, "27": 0, "60": 15, "61": 15, "62": 19}, "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/product.html", "uri": "product.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
