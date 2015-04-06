# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428093491.419568
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/email_receipt.html'
_template_uri = 'email_receipt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tp = context.get('tp', UNDEFINED)
        productlist = context.get('productlist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n    <div>Thank you for your purchase.</div>\n    <div>Your total comes out to</div>\n    <div>Here are your products:</div>\n    <table>\n')
        for name, price in productlist:
            __M_writer('        <tr>\n        <th>')
            __M_writer(str( name ))
            __M_writer('</th>\n        <th>')
            __M_writer(str( price ))
            __M_writer('</th>\n        </tr>\n')
        __M_writer('        <tr>Your total price is: ')
        __M_writer(str( tp ))
        __M_writer('</tr>\n    </table>\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "email_receipt.html", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/email_receipt.html", "line_map": {"32": 19, "38": 32, "16": 0, "23": 1, "24": 13, "25": 14, "26": 15, "27": 15, "28": 16, "29": 16, "30": 19, "31": 19}, "source_encoding": "ascii"}
__M_END_METADATA
"""
