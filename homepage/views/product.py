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
## Shows all products
@view_function
def process_request(request):
    params = {}

    params['products'] = hmod.Product.objects.all()

    return templater.render_to_response(request, 'product.html', params)

#####################################################################
###Product form

class ProductEditForm(forms.Form):
  name = forms.CharField(required=True, max_length= 100 )
  description = forms.CharField(required=True, max_length= 100 )
  price = forms.DecimalField(required=True,max_digits = 10, decimal_places=2)







