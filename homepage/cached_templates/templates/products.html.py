# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425670246.039531
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/products.html'
_template_uri = 'products.html'
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
        products = context.get('products', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n<a href ="/homepage/products.create/" class="btn btn-warning">Create New Product</a>\n</div>\n\n<table id="products_table" class="table table-striped table-bordered">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Price</th>\n        <th>Actions</th>\n    </tr>\n')
        for product in products:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(product.id))
            __M_writer('</td>\n    <td>')
            __M_writer(str(product.name))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(product.description))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(product.price))
            __M_writer(' </td>\n    <td>\n        <a href = "/homepage/products.edit/')
            __M_writer(str( product.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit</a>\n    </td>\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/lukewilliam17/test_dmp/homepage/templates/products.html", "uri": "products.html", "line_map": {"64": 24, "65": 24, "66": 28, "35": 1, "40": 30, "46": 3, "59": 20, "72": 66, "53": 3, "54": 17, "55": 18, "56": 19, "57": 19, "58": 20, "27": 0, "60": 21, "61": 21, "62": 22, "63": 22}, "source_encoding": "ascii"}
__M_END_METADATA
"""
