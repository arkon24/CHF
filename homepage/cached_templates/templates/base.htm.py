# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427998818.111823
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>homepage</title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n      <!-- Latest compiled and minified CSS -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n\n    <!-- Optional theme -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">\n\n    <!-- Latest compiled and minified JavaScript -->\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n<header>\n  Colonial Heritage Foundation\n  </div>\n</header>\n\n  <nav class="navbar navbar-inverse">\n    <p class="navbar-text"></p>\n\n    <div name ="links" class=" nav nav-pills nav-justified">\n        <div class ="pull-right">\n')
        if request.user.is_authenticated():
            __M_writer('\n            <li><button id="show_logout_dialog" class ="btn btn-danger">Logout</button>\n            <button id="show_cart_dialog" class ="btn btn-success">Shopping Cart</button>\n')
        else:
            __M_writer('            <li><button id="show_login_dialog" class ="btn btn-success">Login</button>\n            <a href ="/homepage/account.create/" class="btn btn-warning">Create New Account</a></li>\n')
        __M_writer('        </div>\n    </div>\n</nav>\n\n    <div class="row">\n        <div class="col-md-2" border :2px solid margin="2px">\n            <center> <p></p><a href="http://localhost:8000/homepage/index2/">Home Page</a></p>\n            <p><a href="http://localhost:8000/homepage/product_catalog/">Product Catalog</a></p>\n            <p><a href="http://localhost:8000/homepage/product/">Product Details</a></p>\n            <p><a href="http://localhost:8000/homepage/contact/">Contact</a></p>\n            <p></p><a href="http://localhost:8000/homepage/about/">About</a></p>\n            <p></p><a href="http://localhost:8000/homepage/crud/">Admin Pages</a></p>\n')
        if request.user.is_authenticated():
            __M_writer('            <p><a href="http://localhost:8000/homepage/account/">Account</a></p>\n')
        __M_writer('           <p><a href="http://localhost:8000/homepage/batchprocess/">Overdue Items</a></p>\n           <p><a href="http://localhost:8000/homepage/rentals/">Rental Catalog</a></p>\n           <p><a href="http://localhost:8000/homepage/events/">Events</a></p>\n            </center>\n\n\n        </div>\n        <div class="col-md-8">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div>\n    </div>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                Site content goes here in sub-templates.\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/lukewilliam17/test_dmp/homepage/templates/base.htm", "uri": "base.htm", "line_map": {"64": 76, "70": 76, "76": 70, "16": 4, "18": 0, "28": 2, "29": 4, "30": 5, "34": 5, "35": 14, "36": 24, "37": 24, "38": 26, "39": 26, "40": 30, "41": 30, "42": 30, "43": 45, "44": 46, "45": 49, "46": 50, "47": 53, "48": 65, "49": 66, "50": 68, "55": 78, "56": 83, "57": 83, "58": 83}, "source_encoding": "ascii"}
__M_END_METADATA
"""
