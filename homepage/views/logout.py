__author__ = 'lukewilliam17'

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, logout
from django.conf import settings

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}
    logout(request)
    return HttpResponse('''
          <script>
            window.location.href = '/homepage/index2/   ';
          </script>
        ''')