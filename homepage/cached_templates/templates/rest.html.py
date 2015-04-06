# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428079793.263062
_enable_loop = True
_template_filename = '/Users/lukewilliam17/test_dmp/homepage/templates/rest.html'
_template_uri = 'rest.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\n<html>\n<head>\n<title>REST API Example</title>\n<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\n<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n<script src="//netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n</head>\n<body style="padding: 2em;">\n<h1>REST API Example</h1>\n<pre>\nEndpoint: http://dithers.cs.byu.edu/iscore/api/v1/charges\nValid credit card: Visa, 4732817300654, Exp. 10/15, CVC 411, Cardholder Name: Cosmo Limesandal\nSample Charge Creation:\ncurl http://dithers.cs.byu.edu/iscore/api/v1/charges \\ -d apiKey=YOUR_API_KEY ')
        __M_writer('-d currency=usd ')
        __M_writer('-d amount=5.99 \\ -d type=Visa ')
        __M_writer('-d number=4732817300654 ')
        __M_writer('-d exp_month=10 \\ -d exp_year=15 ')
        __M_writer('-d cvc=411 ')
        __M_writer('-d "name=Cosmo Limesandal" \\ -d "description=Charge for cosmo@is411.byu.edu"\nQuery Charges:\ncurl --get http://dithers.cs.byu.edu/iscore/api/v1/charges ')
        __M_writer('-d apiKey=YOUR_API_KEY\n</pre>\n<button type="button" class="btn btn-primary" id="charge">Charge</button>\n<button type="button" class="btn btn-success" id="queryCharges">Query Charges</button>\n<input type="text" id="chargeId">\n<br />\n<div id="message"></div>\n<script type="text/javascript">\n\n    $(function () {\n         $(\'#charge\').click(function () {\n             $.ajax({\n                    url: \'http://dithers.cs.byu.edu/iscore/api/v1/charges\',\n                    type: \'post\',\n                    data: {\n                            //apiKey:1590aa3e49fd96f344bbc4d4198cd1aa,\n                             apiKey: \'bd4c3e68deac00a9d76b8646e02eb328\',\n                             currency: \'usd\',\n                             amount: \'5.99\',\n                             type: \'Visa\',\n                             number: \'4732817300654\',\n                             exp_month: \'10\',\n                             exp_year: \'15\',\n                             cvc: \'411\',\n                             name: \'Cosmo Limesandal\',\n                             description: \'Charge for cosmo@is411.byu.edu\',\n\n                    },\n                    dataType: \'json\',\n                    success: function (data) {\n                         if (typeof(data[\'error\']) !== \'undefined\') {\n                                $(\'#message\').html(\'<font style="color: red;">\' + \'Failure: \' + data[\'error\'] + \'</font>\');\n                            }\n                         else {\n                                $(\'#message\').html(\'<font style="color: green;">\' + \'New charge: \' + JSON.stringify(data) + \'</font>\');\n                              }\n                            },\n                    error: function (data) {\n                            $(\'#message\').html(\'<font style="color: red;">\' + \'Error: \' + JSON.stringify(data) + \'</font>\');\n\n                    }\n             });\n\n\n         });\n\n\n\n        $(\'#queryCharges\').click(function () {\n        var queryUrl = \'http://dithers.cs.byu.edu/iscore/api/v1/charges\';\n            if (typeof($(\'#chargeId\').val()) !== \'undefined\') {\n            queryUrl = queryUrl + \'/\' + $(\'#chargeId\').val();\n }\n\n\n\n\n            $.ajax({\n                    url: queryUrl,\n                    type: \'get\',\n                    data: {\n                            //apiKey:1590aa3e49fd96f344bbc4d4198cd1aa,\n                             apiKey: \'bd4c3e68deac00a9d76b8646e02eb328\',\n                    },\n                    dataType: \'json\',\n                    success: function (data) {\n                         if (typeof(data[\'error\']) !== \'undefined\') {\n                                $(\'#message\').html(\'<font style="color: red;">\' + \'Failure: \' + data[\'error\'] + \'</font>\');\n                            }\n                         else {\n                                $(\'#message\').html(\'<font style="color: green;">\' + \'New charge: \' + JSON.stringify(data) + \'</font>\');\n                              }\n                            },\n                    error: function (data) {\n                            $(\'#message\').html(\'<font style="color: red;">\' + \'Error: \' + JSON.stringify(data) + \'</font>\');\n\n                    }\n             });\n\n\n         });\n\n\n\n\n\n\n\n\n\n         });\n\n    });\n</script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "34": 28, "21": 1, "22": 17, "23": 18, "24": 19, "25": 20, "26": 21, "27": 22, "28": 25}, "source_encoding": "ascii", "filename": "/Users/lukewilliam17/test_dmp/homepage/templates/rest.html", "uri": "rest.html"}
__M_END_METADATA
"""
