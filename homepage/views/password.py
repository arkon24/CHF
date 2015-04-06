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

    params['users'] = hmod.Users.objects.all().order_by('id')

    return templater.render_to_response(request, 'password.html', params)

#############################
## Edit a user
@view_function
def edit(request):
    params = {}

    try:
      user = hmod.Users.objects.get(id=request.urlparams[0])
    except hmod.Users.DoesNotExist:
      return HttpResponseRedirect('/homepage/index2/')

    form = UserEditForm(initial={
      'username': user.username,
      'password': user.password,
    })

    if request.method == 'POST':
       form = UserEditForm(request.POST)
       form.userid = user.id
       if form.is_valid():
           user.username = form.cleaned_data['username']
           user.set_password(form.cleaned_data['password'])
           user.save()
           return HttpResponseRedirect('/homepage/index2/')

    params['form'] = form
    params['user'] = user

    return templater.render_to_response(request, 'account.edit.html', params)

###User form

class UserEditForm(forms.Form):
  username = forms.CharField(required=True, max_length= 100 )
  password = forms.CharField(required=True, max_length= 100, widget = forms.PasswordInput)

#####################################################################
###Delete a user
@view_function
def delete(request):
     try:
        user = hmod.Users.objects.get(id=request.urlparams[0])
     except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/index2/')

     user.delete()
     return HttpResponseRedirect('/homepage/index2/'.format(user.id))

#####################################################################
###User form
