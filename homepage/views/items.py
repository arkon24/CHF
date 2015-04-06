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

    params['items'] = hmod.Item.objects.all().order_by('id')

    return templater.render_to_response(request, 'items.html', params)

##########################################################################
### Edit an item
@view_function
@permission_required('homepage.change_item')
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
      'user': item.user
     #'Users_id': item.Users_id,
    })

    if request.method == 'POST':
       form = ItemEditForm(request.POST)
       if form.is_valid():
           item.name = form.cleaned_data['name']
           item.description = form.cleaned_data['description']
           item.value = form.cleaned_data['value']
           item.user = form.cleaned_data['user']
          #item.Users_id = form.cleaned_data['Users_id']
           item.save()
           return HttpResponseRedirect('/homepage/items/')

    params['form'] = form
    params['item'] = item

    return templater.render_to_response(request, 'items.edit.html', params)

##############################################################################
#########Create an item
@view_function
@permission_required('homepage.create_item')
def create(request):
    item = hmod.Item()
    item.name = ''
    item.description = ''
    item.value = '0.00'
    item.standardRentalPrice ='0.00'
   #item.Users_id = ''

    item.save()

    return HttpResponseRedirect('/homepage/items.edit/{}'.format(item.id))

#####################################################################
###Delete an item
@view_function
@permission_required('homepage.delete_item')
def delete(request):
     try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
     except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/items/')

     item.delete()
     return HttpResponseRedirect('/homepage/items/'.format(item.id))

#####################################################################
###Item form

class ItemEditForm(forms.Form):
  users = hmod.Users.objects.all()
  name = forms.CharField(required=True, max_length= 100 )
  description = forms.CharField(required=True, max_length= 100 )
  value = forms.DecimalField(required=True,max_digits = 10, decimal_places=2)
  standardRentalPrice = forms.DecimalField(required=True,max_digits = 10, decimal_places=2)
  user = forms.ModelChoiceField(queryset=users)
 #Users_id = forms.CharField(required=True, max_length= 100)







