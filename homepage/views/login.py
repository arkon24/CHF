__author__ = 'lukewilliam17'

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login
from django.conf import settings

from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO

       #s = Server('colheritagefoundation.info', port = 8889, get_info = GET_ALL_INFO)
       #c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC,
       #user='aaron@colheritagefoundation.local',password = 'aaron24', authentication = AUTH_SIMPLE)
       #print('***************************************')
       #print('***************************************')
       #print('***************************************')
       #print('***************************************')
       #print(c)
       #print(c.user)


templater = get_renderer('homepage')

#############################
## Login
@view_function
def process_request(request):
    params = {}


    form = LoginForm()
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():

        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)

        return HttpResponseRedirect('/homepage/users/')

    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(label = "Password", widget=forms.PasswordInput )

  def clean(self):
      user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
      if user == None:
          raise forms.ValidationError("No soup for you! No login for you!")
      return self.cleaned_data








