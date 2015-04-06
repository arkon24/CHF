__author__ = 'lukewilliam17'

from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from .. import dmp_render, dmp_render_to_response
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import requests




templater = get_renderer('homepage')


#############################
## Shows all items
#@view_function
#def process_request(request):
#   params = {}

#   return templater.render_to_response(request, 'shoppingcart.html', params)

@view_function
def process_request(request):
    rows = []
    cart = request.session["shopping_cart"]
    for key, qty in cart.items():
        product = hmod.Product.objects.get(id=key)
        price = product.price * qty
        name = product.name
        rows.append('''
        <div class='cart-item'>
            <div class="cart-left">%s</div>
            <div class='cart-middle'>Quantity: <input class='product-quantity' name="%s" type='number' required max='200' min='1' value='%d'/></div>
            <div class="cart-right">
                <span class="glyphicon glyphicon-usd" aria-hidden="true"></span> %s
                <a href ="/homepage/shoppingcart.delete?id=%s">
                <span class="glyphicon glyphicon-minus cart-delete" aria-hidden="true"></span>
                </a>

            </div>
        </div>
        ''' % (name, key, qty, "{:,}".format(price), key))
    rows.append('''<a href="/homepage/shoppingcart.checkout/"class="btn btn-default">Checkout</a> ''')
    html = "\n"
    html = html.join(rows)
    return HttpResponse(html)


@view_function
def add(request):

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    cart = request.session["shopping_cart"]
    pid = request.urlparams[0]
    qty = request.urlparams[1]
    if pid in cart:
        cart[pid] += int(qty)
    else:
        cart[pid] = int(qty)

    request.session["shopping_cart"] = cart
    print(cart)

    return HttpResponseRedirect('/homepage/shoppingcart/')



@view_function
def delete(request):
    if request.method != "GET":
        return HttpResponse(0)

    cart = request.session["shopping_cart"]
    item = request.GET.get("id")
    print("XXXXXXXXX"+str(item))
    if item in cart:
        cart.pop(item, None)
    request.session["shopping_cart"] = cart
    html = process_request(request)
    print(str(cart))
    return HttpResponseRedirect('/homepage/product_catalog/')

@view_function
def update(request):
    if request.method != "POST":
        return HttpResponse(0)

    cart = request.session["shopping_cart"]
    for item, qty in dict(request.POST).items():
        quantity = int(qty[0])
        cart[item] = quantity
    request.session["shopping_cart"] = cart
    html = process_request(request)
    return HttpResponseRedirect





@view_function
def checkout(request):
    template_vars = {}

    form = checkoutform()
    if request.method == 'POST':
        form = checkoutform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '1590aa3e49fd96f344bbc4d4198cd1aa'
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])

            #Get shopping cart info to get total price and send receipt
            cart = request.session["shopping_cart"]
            print(str(cart))

            template_vars['productlist'] = []
            template_vars['pricelist'] = []
            totalprice = 0

            for key, qty in cart.items():
                product = hmod.Product.objects.get(id=key)
                price = product.price * qty
                totalprice = totalprice + price
                name = product.name
                print(name)
                print(price)
                template_vars['productlist'].append([name, price])
                template_vars['pricelist'].append(price)

            #for loop to take out each product in productlist
            template_vars['tp'] = totalprice

            # do form.cleaned data, instead of hard coding it in
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': totalprice,
                'type': form.cleaned_data['type'],
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
                'name': 'Cosmo Limesandal',
                'description': 'Charge for cosmo@is411.byu.edu'
            })

            print(r.text)

            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])

            else:
                print(resp.keys())
                print(resp['ID'])

            body = dmp_render(request, 'email_receipt.html', template_vars)

            send_mail('CHF Receipt', body, 'shimotsuki.eleven@gmail.com',
            [user.email], fail_silently=False, html_message=body)

            return dmp_render_to_response(request, 'purchase.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'checkout.html', template_vars)


class checkoutform(forms.Form):
    username = forms.CharField()
    #currency = 'usd'
    amount = '3.99' #get this from session?
    type = forms.CharField(label="Card Type")
    number = forms.CharField(label="Credit Card Number", max_length=16, min_length=10)
    exp_month = forms.CharField(max_length=2, min_length=2)
    exp_year = forms.CharField(max_length=2, min_length=2)
    cvc = forms.CharField(max_length=4, label="CVC", min_length=3)
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data