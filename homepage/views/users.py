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
@permission_required('homepage.add_users')
def process_request(request):
    params = {}

    params['users'] = hmod.Users.objects.all().order_by('id')

    return templater.render_to_response(request, 'users.html', params)

#############################
## Edit a user
@view_function
@permission_required('homepage.change_users')
def edit(request):
    params = {}

    try:
      user = hmod.Users.objects.get(id=request.urlparams[0])
    except hmod.Users.DoesNotExist:
      return HttpResponseRedirect('/homepage/users/')

    form = UserEditForm(initial={
      'username': user.username,
      'password': user.password,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'email': user.email,
      'address1': user.address1,
      'city': user.city,
      'state': user.state,
      'zip': user.zip,
      'security_question': user.security_question,

    })

    if request.method == 'POST':
       form = UserEditForm(request.POST)
       form.userid = user.id
       if form.is_valid():
           user.username = form.cleaned_data['username']
           user.set_password(form.cleaned_data['password'])
           user.first_name = form.cleaned_data['first_name']
           user.last_name = form.cleaned_data['last_name']
           user.email = form.cleaned_data['email']
           user.address1 = form.cleaned_data['address1']
           user.city = form.cleaned_data['city']
           user.state = form.cleaned_data['state']
           user.zip = form.cleaned_data['zip']
           user.security_question = form.cleaned_data['security_question']
           user.save()
           return HttpResponseRedirect('/homepage/users/')

    params['form'] = form
    params['user'] = user

    return templater.render_to_response(request, 'users.edit.html', params)

##############################################################################
#########Create a user
@view_function
@permission_required('homepage.add_users')
def create(request):
    user = hmod.Users.objects.create_user(
        username= "Enter Username",
        email="",
        password="",
        last_name="",
        first_name="",
        address1="",
        zip= "",
        city="",
        state="",
       #securityQuestion=""
   #securityAnswer=''
   #phoneNumber=
    )

    return HttpResponseRedirect('/homepage/users.edit/{}'.format(user.id))


#####################################################################
###Delete a user
@view_function
@permission_required('homepage.delete_users')
def delete(request):
     try:
        user = hmod.Users.objects.get(id=request.urlparams[0])
     except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

     user.delete()
     return HttpResponseRedirect('/homepage/users/'.format(user.id))

#####################################################################
###User form

class UserEditForm(forms.Form):
  username = forms.CharField(required=True, max_length= 100 )
  password = forms.CharField(required=True, max_length= 100, widget = forms.PasswordInput)
  first_name = forms.CharField(required=True, max_length= 100 )
  last_name = forms.CharField(required=True, max_length= 100 )
  email = forms.EmailField(required=True, max_length= 100 )
  address1 = forms.CharField(required=True, max_length= 100 )
  city = forms.CharField(required=True, max_length= 100 )
  state = forms.CharField(required=True, max_length= 100 )
  zip = forms.CharField(required=True, max_length= 100 )
  security_question = forms.CharField(required=True, max_length= 100 )

  def clean_username(self):
     if len(self.cleaned_data['username']) < 5:
        raise forms.ValidationError("Please enter at least 5 characters.")

     user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
     if user_count >= 1:
        raise forms.ValidationError("That username is already taken.")
     return self.cleaned_data['username']






