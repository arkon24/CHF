from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from .. import dmp_render, dmp_render_to_response
from datetime import datetime
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django import forms
from django.contrib.auth import authenticate, login
from django.conf import settings



templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)

    params['form'] = form
    return templater.render_to_response(request, 'index.html', params)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(label = "Password", widget=forms.PasswordInput )

 #def clean(self):
 #    user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
 #    if user == None:
 #        raise forms.ValidationError("No soup for you! No login for you!")
 #    return self.cleaned_data

@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)

    params['form'] = form
    return templater.render_to_response(request, 'index.loginform.html', params)


@view_function
def check_username(request):
    username = request.REQUEST.get('u')
    print('>>>>>>>>', username)

#@view_function
#def process_request(request):
#  template_vars = {
#    'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
#    'timecolor': random.choice([ 'red', 'blue', 'green', 'brown' ]),
#  }
#  return templater.render_to_response(request, 'index.html', template_vars)

#@view_function
#def gettime(request):
#  template_vars = {
#    'now': datetime.now(),
#  }
#  return templater.render_to_response(request, 'index_time.html', template_vars)