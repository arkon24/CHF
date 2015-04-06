# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427922707.108644
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/rev_reenact.html'
_template_uri = 'rev_reenact.html'
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
        areas = context.get('areas', UNDEFINED)
        exp = context.get('exp', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        exp = context.get('exp', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-right">\n<!--<a href ="/homepage/events.create/" class="btn btn-warning">Create New Event</a>-->\n</div>\n\n<table id="events_table" class="table table-striped table-bordered">\n    <center><h4>Main Event</h4></center>\n    <tr>\n        <th>Name</th>\n        <th>Type</th>\n        <th>Location</th>\n        <th>Description</th>\n        <th>Start Date</th>\n        <th>End Date</th>\n        <th>Address</th>\n        <th>City</th>\n        <th>State</th>\n        <th>Zip</th>\n    </tr>\n')
        for event in events:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(event.name))
            __M_writer('</td>\n    <td>')
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
            __M_writer(' </td>\n  </tr>\n')
        __M_writer('</table>\n\n\n<div class="text-right">\n</div>\n\n<table id="events_table" class="table table-striped table-bordered">\n    <center><h4>Event Areas</h4></center>\n    <tr>\n        <th>Areas for the event</th>\n        <th>Description</th>\n    </tr>\n')
        for area in areas:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(area.aname))
            __M_writer('</td>\n    <td>')
            __M_writer(str(area.description))
            __M_writer(' </td>\n  </tr>\n')
        __M_writer('</table>\n\n\n\n<div class="text-right">\n</div>\n\n<table id="events_table" class="table table-striped table-bordered">\n    <tr>\n        <center><h4>Expected Sale Items</h4></center>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Area</th>\n    </tr>\n')
        for expected_sale_item in exp:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(expected_sale_item.name))
            __M_writer('</td>\n    <td>')
            __M_writer(str(expected_sale_item.description))
            __M_writer(' </td>\n    <td>')
            __M_writer(str(expected_sale_item.area))
            __M_writer('</td>\n  </tr>\n')
        __M_writer('</table>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/rev_reenact.html", "uri": "rev_reenact.html", "line_map": {"27": 0, "37": 1, "42": 79, "48": 3, "57": 3, "58": 23, "59": 24, "60": 25, "61": 25, "62": 26, "63": 26, "64": 27, "65": 27, "66": 28, "67": 28, "68": 29, "69": 29, "70": 30, "71": 30, "72": 31, "73": 31, "74": 32, "75": 32, "76": 33, "77": 33, "78": 34, "79": 34, "80": 37, "81": 49, "82": 50, "83": 51, "84": 51, "85": 52, "86": 52, "87": 55, "88": 69, "89": 70, "90": 71, "91": 71, "92": 72, "93": 72, "94": 73, "95": 73, "96": 76, "102": 96}}
__M_END_METADATA
"""
