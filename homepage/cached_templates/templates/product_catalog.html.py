# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425765256.152946
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/product_catalog.html'
_template_uri = 'product_catalog.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        for Product in catalog_items:
            __M_writer('    <div class="item_container text-center text-muted">\n        <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Product.name))
            __M_writer('.jpg/"/>\n        <a href="/homepage/index2/">\n        <div>')
            __M_writer(str( Product.name ))
            __M_writer('</div>\n        </a>\n        <div>')
            __M_writer(str( Product.price ))
            __M_writer('</div>\n        <input id="qty')
            __M_writer(str( Product.id ))
            __M_writer('"type = "number" name = "qty" value ="0" min="1" max="400"/>\n        <div class="text-right"><button data-pid="')
            __M_writer(str( Product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\n        </div>\n    </div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 10, "65": 10, "66": 11, "27": 0, "36": 1, "69": 12, "68": 12, "41": 17, "76": 70, "70": 16, "47": 2, "67": 11, "55": 2, "56": 4, "57": 5, "58": 6, "59": 6, "60": 6, "61": 6, "62": 8, "63": 8}, "uri": "product_catalog.html", "source_encoding": "ascii", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/product_catalog.html"}
__M_END_METADATA
"""
