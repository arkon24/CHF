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
## Shows all items
@view_function
def process_request(request):
    params = {}

    events = hmod.Event.objects.filter(id='3')
    areas = hmod.Area.objects.all()
    exp = hmod.Expected_Sale_Item.objects.all()

    params['areas'] = areas
    params['exp'] = exp
    params['events'] = events

    return templater.render_to_response(request, 'rev_reenact.html', params)

##########################################################################









