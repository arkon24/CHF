from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
import datetime
from django.core.mail import send_mail
from time import time
from django.conf import settings
from django import forms
# Import the reverse shortcut to get the URLs of URL patterns using just their name.
from django.core.urlresolvers import reverse

# Import the built-in password reset view and password reset confirmation view.
from django.contrib.auth.views import password_reset, password_reset_confirm

# Import the render shortcut to render the templates in response.
from django.shortcuts import render

# This view handles the password reset form URL /.
@view_function
def reset(request):
    # Wrap the built-in password reset view and pass it the arguments
    # like the template name, email template name, subject template name
    # and the url to redirect after the password reset is initiated.
    return password_reset(request, template_name='reset.html',
        email_template_name='reset_email.html',
        subject_template_name='reset_subject.txt',
        post_reset_redirect=reverse('success'))


@view_function
def process_request(request):
    params = {}

    params['phones'] = hmod.Phone.objects.all().order_by('type')

    return templater.render_to_response(request, 'phones.html', params)


# This view handles password reset confirmation links. See urls.py file for the mapping.
# This view is not used here because the password reset emails with confirmation links
# cannot be sent from this application.
def reset_confirm(request, uidb64=None, token=None):
    # Wrap the built-in reset confirmation view and pass to it all the captured parameters like uidb64, token
    # and template name, url to redirect after password reset is confirmed.
    return password_reset_confirm(request, template_name='reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('success'))

# This view renders a page with success message.
def success(request):
  return render(request, "success.html")