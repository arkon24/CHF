# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423254573.867562
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/participants.html'
_template_uri = 'participants.html'
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
        participants = context.get('participants', UNDEFINED)
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
        participants = context.get('participants', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n<a href ="/homepage/participants.create/" class="btn btn-warning">Create New Participant</a>\n</div>\n\n<table id="participants_table" class="table table-striped table-bordered">\n    <tr>\n        <th>ID</th>\n        <th>Username</th>\n        <th>First Name</th>\n        <th>Last Name</th>\n        <th>Email</th>\n        <th>Address</th>\n        <th>State</th>\n        <th>City</th>\n        <th>Zipcode</th>\n        <th>Security Question</th>\n        <th>Biographical Sketch</th>\n        <th>Contact Relationship</th>\n        <th>Role</th>\n        <th>Actions</th>\n    </tr>\n')
        for participant in participants:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(participant.id))
            __M_writer('</td>\n    <td>')
            __M_writer(str(participant.username))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.first_name))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.last_name))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.email))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.address1))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.state))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.city))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.zip))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.security_question))
            __M_writer('</td>\n    <td>')
            __M_writer(str(participant.biographicalSketch))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.contactRelationship))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(participant.role))
            __M_writer(' </td>\n\n    <td>\n        <a href = "/homepage/participants.edit/')
            __M_writer(str( participant.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit</a>\n    </td>\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/lukewilliam17/test_dmp/homepage/templates/participants.html", "uri": "participants.html", "line_map": {"64": 32, "65": 32, "66": 33, "67": 33, "68": 34, "69": 34, "70": 35, "71": 35, "72": 36, "73": 36, "74": 37, "75": 37, "76": 38, "77": 38, "78": 39, "79": 39, "80": 40, "81": 40, "82": 43, "83": 43, "84": 47, "90": 84, "27": 0, "35": 1, "40": 49, "46": 3, "53": 3, "54": 26, "55": 27, "56": 28, "57": 28, "58": 29, "59": 29, "60": 30, "61": 30, "62": 31, "63": 31}, "source_encoding": "ascii"}
__M_END_METADATA
"""
