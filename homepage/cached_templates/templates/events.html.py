# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427919332.484835
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n<!--<a href ="/homepage/events.create/" class="btn btn-warning">Create New Event</a>-->\n</div>\n\n<table id="events_table" class="table table-striped table-bordered">\n    <tr>\n        <th>Name</th>\n        <th>Type</th>\n        <th>Location</th>\n        <th>Description</th>\n        <th>Start Date</th>\n        <th>End Date</th>\n        <th>Address</th>\n        <th>City</th>\n        <th>State</th>\n        <th>Zip</th>\n<!-- <th>Actions</th> -->\n    </tr>\n')
        for event in events:
            __M_writer('  <tr>\n    <td><a href = "/homepage/rev_reenact/">')
            __M_writer(str(event.name))
            __M_writer('</a></td>\n    <td>')
            __M_writer(str(event.type))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.location))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.description))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.start_date))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.end_date))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.address1))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.city))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.state))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(event.zip))
            __M_writer(' </td>\n <!--   <td>\n  <a href = "/homepage/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit</a>\n    </td>-->\n  </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 29, "65": 29, "66": 30, "67": 30, "68": 31, "69": 31, "70": 32, "71": 32, "72": 33, "73": 33, "74": 34, "75": 34, "76": 36, "77": 36, "78": 40, "84": 78, "27": 0, "35": 1, "40": 42, "46": 3, "53": 3, "54": 23, "55": 24, "56": 25, "57": 25, "58": 26, "59": 26, "60": 27, "61": 27, "62": 28, "63": 28}, "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/events.html", "uri": "events.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
