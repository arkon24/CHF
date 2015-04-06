__author__ = 'lukewilliam17'

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.conf import settings

templater = get_renderer('homepage')


##########################################################################
## Shows all personal products
@view_function
def process_request(request):
    params = {}

    params['personal_products'] = hmod.Item.objects.all()

    return templater.render_to_response(request, 'items.html', params)

##########################################################################
### Edit an item
@view_function
def edit(request):
    params = {}

    try:
      item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
      return HttpResponseRedirect('/homepage/items/')


    form = ItemEditForm(initial={
      'name': item.name,
      'description': item.description,
      'value': item.value,
      'standardRentalPrice': item.standardRentalPrice,
     #'Users_id': item.Users_id,
    })

    if request.method == 'POST':
       form = ItemEditForm(request.POST)
       if form.is_valid():
           item.name = form.cleaned_data['name']
           item.description = form.cleaned_data['description']
           item.value = form.cleaned_data['value']
          #item.Users_id = form.cleaned_data['Users_id']

           item.save()
           return HttpResponseRedirect('/homepage/items/')

    params['form'] = form
    params['item'] = item

    return templater.render_to_response(request, 'items.edit.html', params)

##########################################################################
#########Create a personal product
@view_function
def create(request):
    item = hmod.Item()
    item.name = ''
    item.description = ''
    item.value = '0.00'
    item.standardRentalPrice ='0.00'
   #item.Users_id = ''

    item.save()

    return HttpResponseRedirect('/homepage/items.edit/{}'.format(item.id))

##########################################################################
###Delete a personal product
@view_function
def delete(request):
     try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
     except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/items/')

     item.delete()
     return HttpResponseRedirect('/homepage/items/'.format(item.id))

##########################################################################
###Personal product form

class ItemEditForm(forms.Form):
  name = forms.CharField(required=True, max_length= 100 )
  description = forms.CharField(required=True, max_length= 100 )
  value = forms.DecimalField(required=True,max_digits = 10, decimal_places=2)
  standardRentalPrice = forms.DecimalField(required=True,max_digits = 10, decimal_places=2)
 #Users_id = forms.CharField(required=True, max_length= 100)







