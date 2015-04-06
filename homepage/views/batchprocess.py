__author__ = 'lukewilliam17'

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
import datetime
from django.core.mail import send_mail
from time import time
from django.conf import settings

templater = get_renderer('homepage')


#############################
## Shows all items
@view_function
def process_request(request):
    params = {}

    overdueitems = hmod.Rented_Item.objects.filter(date_due__lt=datetime.date.today()).exclude(date_in__isnull=False)

    params['overdueitems'] = overdueitems
    params['sixty'] = []
    params['thirty'] = []
    params['zero'] = []

    for Rented_Item in overdueitems:
        ds = datetime.date.today() - Rented_Item.date_due
        dt = abs(ds.days)

        if dt >= 60:
            sixty = Rented_Item
            params['sixty'].append(Rented_Item)
            print(Rented_Item.renter)

        elif dt < 60 & dt >= 30:
            thirty = Rented_Item
            params['thirty'].append(Rented_Item)

        else:
            zero = Rented_Item
            params['zero'].append(Rented_Item)

        params['overdueitems'] = overdueitems
        print(ds)
        print(dt)


    return templater.render_to_response(request, 'batchprocess.html', params)



@view_function
def email(request):
    params = {

    }
    overdueitems = hmod.Rented_Item.objects.filter(date_due__lt=datetime.date.today()).exclude(date_in__isnull=False)

    for Rented_Item in overdueitems:
        ds = datetime.date.today() - Rented_Item.date_due
        dt = abs(ds.days)

        #email_body = dmp_render(request, 'You have an overdue item that you rented from the Colonial Heritage Foundation. It was due on', params)
        send_mail('Rental Overdue Notice', 'This is to notify you that you have an overdue item. It was due on: %s and is now %s days overdue' % (Rented_Item.date_due, dt), 'shimotsuki.eleven@gmail.com',
            [Rented_Item.renter.email], fail_silently=False)

    return HttpResponseRedirect('/homepage/index2/')





