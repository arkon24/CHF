from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    catalog_items = hmod.Product.objects.all();

    params['catalog_items'] = catalog_items
    return templater.render_to_response(request, 'product_catalog.html', params)