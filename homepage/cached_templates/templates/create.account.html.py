# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425584732.936018
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/account.html'
_template_uri = 'account.html'
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
        user = context.get('user', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n<h4>Account Information</h4>\n<table id="users_table" class="table table-striped table-bordered">\n    <tr>\n        <th>Username</th>\n        <th>First Name</th>\n        <th>Last Name</th>\n        <th>Email</th>\n        <th>Address</th>\n        <th>State</th>\n        <th>City</th>\n        <th>Zipcode</th>\n        <th>Security Question</th>\n        <th>Actions</th>\n    </tr>\n  <tr>\n    <td>')
        __M_writer(str(user.username))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.first_name))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.last_name))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.email))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.address1))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.state))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.city))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.zip))
        __M_writer(' </td>\n    <td>')
        __M_writer(str(user.security_question))
        __M_writer('</td>\n    <td>\n        <a href = "/homepage/users.edit/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-xs btn-default">Edit</a>\n    </td>\n  </tr>\n</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "account.html", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/account.html", "line_map": {"64": 26, "65": 26, "66": 27, "67": 27, "68": 28, "69": 28, "70": 29, "71": 29, "72": 31, "73": 31, "79": 73, "27": 0, "35": 1, "40": 36, "46": 3, "53": 3, "54": 21, "55": 21, "56": 22, "57": 22, "58": 23, "59": 23, "60": 24, "61": 24, "62": 25, "63": 25}}
__M_END_METADATA
"""
