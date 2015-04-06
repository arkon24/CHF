__author__ = 'lukewilliam17'

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType

templater = get_renderer('homepage')


#############################
## Shows all users
@view_function
def process_request(request):
    params = {}

    params['users'] = hmod.rentals.objects.all().order_by('id')

    return templater.render_to_response(request, 'rentals.detail.html', params)

#############################