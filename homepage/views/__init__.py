DJANGO_MAKO_PLUS = True

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from . import templater, prepare_params
import homepage.models as hmod
import random
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.conf import settings

#templater = get_renderer('homepage')

#@view_funciton
#def process_request(request)
# params = {}

# return templater.render_to_response(request, 'users.html', params)

