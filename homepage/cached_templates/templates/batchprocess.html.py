# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427934785.921426
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/batchprocess.html'
_template_uri = 'batchprocess.html'
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
        thirty = context.get('thirty', UNDEFINED)
        zero = context.get('zero', UNDEFINED)
        sixty = context.get('sixty', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        thirty = context.get('thirty', UNDEFINED)
        zero = context.get('zero', UNDEFINED)
        sixty = context.get('sixty', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<a href="/homepage/batchprocess.email/" class="btn btn-warning">Send Emails</a>\n\n<title>Overdue Rentals</title>\n\n<h3>Items overdue 60 days or more</h3>\n<title>Overdue Items 30</title>\n  <table>\n   <tr>\n      <th>Renter\'s Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\n      <th>Rental Product</th>\n  </tr>\n')
        for Rented_Item in sixty:
            __M_writer('       <tr>\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\n            <p></p>\n       </tr>\n')
        __M_writer("  </table>\n\n\n\n<h3>Items overdue between 30 and 60 days</h3>\n<title>Overdue Items 60</title>\n  <table>\n   <tr>\n      <th>Renter's Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\n      <th>Rental Product</th>\n  </tr>\n")
        for Rented_Item in thirty:
            __M_writer('       <tr>\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\n            <p></p>\n       </tr>\n')
        __M_writer("  </table>\n\n<h3>Items overdue 30 days or less</h3>\n<title>Overdue Items 30</title>\n  <table>\n   <tr>\n      <th>Renter's Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\n      <th>Rental Product</th>\n  </tr>\n")
        for Rented_Item in zero:
            __M_writer('       <tr>\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\n            <p></p>\n       </tr>\n')
        __M_writer('  </table>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "batchprocess.html", "source_encoding": "ascii", "line_map": {"27": 0, "37": 1, "47": 3, "56": 3, "57": 19, "58": 20, "59": 21, "60": 21, "61": 22, "62": 22, "63": 23, "64": 23, "65": 24, "66": 24, "67": 25, "68": 25, "69": 29, "70": 43, "71": 44, "72": 45, "73": 45, "74": 46, "75": 46, "76": 47, "77": 47, "78": 48, "79": 48, "80": 49, "81": 49, "82": 53, "83": 65, "84": 66, "85": 67, "86": 67, "87": 68, "88": 68, "89": 69, "90": 69, "91": 70, "92": 70, "93": 71, "94": 71, "95": 75, "101": 95}, "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/batchprocess.html"}
__M_END_METADATA
"""
