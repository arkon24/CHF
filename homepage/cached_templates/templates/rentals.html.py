# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427917649.515445
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/rentals.html'
_template_uri = 'rentals.html'
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
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<table id="rentals_table" class="table table-striped table-bordered">\n    <tr>\n        <th>Name</th>\n        <th>Photo</th>\n        <th>Times Rented</th>\n        <th>Price Per Day</th>\n        <th>Replacement Price</th>\n        <th>Quantity</th>\n        <th>Action</th>\n    </tr>\n')
        for rental in rentals:
            __M_writer('  <tr>\n\n    <td><a href = "/homepage/rentals.detail/')
            __M_writer(str( rental.id ))
            __M_writer('/">')
            __M_writer(str(rental.name))
            __M_writer('</a></td>\n    <td><center><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( rental.name))
            __M_writer('.jpg/" height="150" /></center></td>\n    <td>')
            __M_writer(str(rental.times_rented))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(rental.price_per_day))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(rental.replacement_price))
            __M_writer(' </td>\n    <td><input id="qty')
            __M_writer(str( rental.id ))
            __M_writer('"type = "number" name = "qty" value ="0" min="1" max="400"/></td>\n    <td><button data-pid="')
            __M_writer(str( rental.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button></td>\n  </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 19, "65": 19, "66": 20, "67": 20, "68": 21, "69": 21, "70": 22, "71": 22, "72": 23, "73": 23, "74": 24, "75": 24, "76": 27, "82": 76, "27": 0, "36": 1, "41": 28, "47": 3, "55": 3, "56": 15, "57": 16, "58": 18, "59": 18, "60": 18, "61": 18, "62": 19, "63": 19}, "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/rentals.html", "uri": "rentals.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
