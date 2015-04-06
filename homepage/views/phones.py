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
## Shows all phones
@view_function
def process_request(request):
    params = {}

    params['phones'] = hmod.Phone.objects.all().order_by('type')

    return templater.render_to_response(request, 'phones.html', params)

##########################################################################
### Edit a phone
@view_function
@permission_required('homepage.change_phone')
def edit(request):
    params = {}

    try:
      phone = hmod.Phone.objects.get(id=request.urlparams[0])
    except hmod.Phone.DoesNotExist:
      return HttpResponseRedirect('/homepage/phones/')


    form = PhoneEditForm(initial={
      'number': phone.number,
      'extension': phone.extension,
      'type': phone.type,
      'user': phone.user
    })

    if request.method == 'POST':
       form = PhoneEditForm(request.POST)
       if form.is_valid():
           phone.number = form.cleaned_data['number']
           phone.extension = form.cleaned_data['extension']
           phone.type = form.cleaned_data['type']
           phone.user = form.cleaned_data['user']
           phone.save()
           return HttpResponseRedirect('/homepage/phones/')

    params['form'] = form
    params['phone'] = phone

    return templater.render_to_response(request, 'phones.edit.html', params)

##############################################################################
#########Create a phone
@view_function
@permission_required('homepage.create_phone')

def create(request):

    phone = hmod.Phone()
    phone.number = ''
    phone.extension = ''
    phone.type = ''
    phone.save()

    return HttpResponseRedirect('/homepage/phones.edit/{}'.format(phone.id))

#####################################################################
###Delete a phone
@view_function
@permission_required('homepage.delete_phone')
def delete(request):
     try:
        phone = hmod.Phone.objects.get(id=request.urlparams[0])
     except hmod.Phone.DoesNotExist:
        return HttpResponseRedirect('/homepage/phones/')

     phone.delete()
     return HttpResponseRedirect('/homepage/phones/'.format(phone.id))

#####################################################################
###Phone form

class PhoneEditForm(forms.Form):
  users = hmod.Users.objects.all()
  number = forms.CharField(required=True, max_length= 100)
  extension = forms.CharField(required=True, max_length= 100)
  type = forms.CharField(required=True, max_length= 100)
  user = forms.ModelChoiceField(queryset=users)
 #Users_id = forms.CharField(required=True, max_length= 100)







