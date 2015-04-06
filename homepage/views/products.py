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
@permission_required('homepage.change_product')
def process_request(request):
    params = {}

    params['products'] = hmod.Product.objects.all()

    return templater.render_to_response(request, 'products.html', params)

##########################################################################
### Edit a product
@view_function
@permission_required('homepage.change_product')
def edit(request):
    params = {}

    try:
      product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
      return HttpResponseRedirect('/homepage/products/')


    form = ProductEditForm(initial={
      'name': product.name,
      'description': product.description,
      'category': product.category,
      'price': product.price,
    })

    if request.method == 'POST':
       form = ProductEditForm(request.POST)
       if form.is_valid():
           product.name = form.cleaned_data['name']
           product.description = form.cleaned_data['description']
           product.price = form.cleaned_data['price']
           product.save()
           return HttpResponseRedirect('/homepage/products/')

    params['form'] = form
    params['product'] = product

    return templater.render_to_response(request, 'products.edit.html', params)

##############################################################################
#########Create an product
@view_function
@permission_required('homepage.create_product')
def create(request):
    product = hmod.Product()
    product.name = ''
    product.description = ''
    product.price ='0.00'

    product.save()

    return HttpResponseRedirect('/homepage/products.edit/{}'.format(product.id))

#####################################################################
###Delete an product
@view_function
@permission_required('homepage.delete_product')
def delete(request):
     try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
     except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/products/')

     product.delete()
     return HttpResponseRedirect('/homepage/products/'.format(product.id))

#####################################################################
###Product form

class ProductEditForm(forms.Form):
  name = forms.CharField(required=True, max_length= 100 )
  description = forms.CharField(required=True, max_length= 100 )
  price = forms.DecimalField(required=True,max_digits = 10, decimal_places=2)







