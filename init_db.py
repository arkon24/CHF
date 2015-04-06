__author__ = 'lukewilliam17'

#!/usr/bin/env python

# initialize django
import os
import datetime
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()


#normal import
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess
import homepage.models as hmod

##### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

##### CREATE PERMISSIONS/GROUPS #####################
Permission.objects.all().delete()
Group.objects.all().delete()

#########Admin
permission = Permission()
permission.codename = 'admin_rights'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'AdminRights'
permission.save()

agroup = Group()
agroup.name = "Admin"
agroup.save()
agroup.permissions.add(permission)
subprocess.call([sys.executable, "manage.py", "migrate"])

###########Manager
permission = Permission()
permission.codename = 'manager_rights'
permission.content_type = ContentType.objects.get(id=5)
permission.name = 'ManagerRights'
permission.save()

mgroup = Group()
mgroup.name = "Manager"
mgroup.save()
mgroup.permissions.add(permission)

##########Guest
permission = Permission()
permission.codename = 'guest_rights'
permission.content_type = ContentType.objects.get(id=2)
permission.name = 'GuestRights'
permission.save()

gugroup = Group()
gugroup.name = "Guest"
gugroup.save()
gugroup.permissions.add(permission)

############ MAKE USERS ####################
u = hmod.Users()
u.username = 'Aaron'
u.set_password('password')
u.first_name = 'Aaron'
u.last_name = 'Stennett'
u.email = 'aaronhalsy@gmail.com'
u.address1 = '364 w 976 N'
u.address2 = '5'
u.city = 'Provo'
u.state = 'UT'
u.zip = '84606'
u.security_question = 'What is your favorite fruit?'
u.security_answer = 'I do not know'
u.is_superuser = True
u.save()

agroup.user_set.add(u)

u = hmod.Users()
u.username = 'Samus'
u.set_password('password')
u.first_name = 'Samus'
u.last_name = 'Aran'
u.email = 'srf.aquila001@gmail.com'
u.address1 = 'Talon Overworld'
u.address2 = '#5'
u.city = 'Aether'
u.state = 'MO'
u.zip = '87847'
u.security_question = 'What is your weakness?'
u.security_answer = 'Nothing'
u.save()

agroup.user_set.add(u)

u = hmod.Users()
u.username = 'Link'
u.set_password('password')
u.first_name = 'Link'
u.last_name = 'Nameless'
u.email = 'linkr@hyrule.com'
u.address1 = 'Hyrule'
u.address2 = '6'
u.city = 'Castle Town'
u.state = 'UT'
u.zip = '84606'
u.security_question = 'Who is your favorite character?'
u.security_answer = 'Happy Mask Salesman'
u.save()

mgroup.user_set.add(u)

u = hmod.Users()
u.username = 'Spiderman'
u.set_password('password')
u.first_name = 'Peter'
u.last_name = 'Parker'
u.email = 'pete@sman.com'
u.address1 = 'broadway'
u.address2 = '34'
u.city = 'New York City'
u.state = 'NY'
u.zip = '88779'
u.security_question = 'What do you like to shoot?'
u.security_answer = 'Webs'
u.save()

gugroup.user_set.add(u)


u = hmod.Users()
u.username = 'Eminem'
u.set_password('password')
u.first_name = 'Marshall'
u.last_name = 'Mathers'
u.email = 'slimshady@fu.com'
u.address1 = '16 Trailer Park'
u.address2 = ''
u.city = 'Detroit'
u.state = 'MI'
u.zip = '44896'
u.security_question = 'What is your movie called?'
u.security_answer = '8 mile'
u.save()

mgroup.user_set.add(u)

u = hmod.Users()
u.username = 'Ridley'
u.set_password('password')
u.first_name = 'Meta'
u.last_name = 'Ridley'
u.email = 'mrid@chozo.com'
u.address1 = '2233 Zebus Way'
u.address2 = ''
u.city = 'Zebus'
u.state = 'BR'
u.zip = '95316'
u.security_question = 'Who is your enemy?'
u.security_answer = 'Samus Aran'
u.save()

gugroup.user_set.add(u)


u = hmod.Users()
u.username = 'Ike'
u.set_password('password')
u.first_name = 'Ike'
u.last_name = 'Greil'
u.email = 'ikeg@greilm.com'
u.address1 = '2838 Sergate'
u.address2 = ''
u.city = 'Kalo'
u.state = 'Crimea'
u.zip = '76454'
u.security_question = 'What sword do you use?'
u.security_answer = 'Ragnell'
u.save()

agroup.user_set.add(u)


ag = hmod.Agent()
ag.username = 'Tuomas'
ag.set_password('password')
ag.first_name = 'Tuomas'
ag.last_name = 'Holopainen'
ag.email = 'tuo@holo.com'
ag.address1 = 'Nightwish Lane'
ag.address2 = ''
ag.city = 'Kitee'
ag.state = 'FI'
ag.zip = '87654'
ag.security_question = 'What is your favorite movie??'
ag.security_answer = 'The village'
ag.appointmentDate = datetime.datetime.now()
ag.save()

mgroup.user_set.add(u)


ag = hmod.Agent()
ag.username = 'Marco'
ag.set_password('password')
ag.first_name = 'Marco'
ag.last_name = 'Hietala'
ag.email = 'mar@hie.com'
ag.address1 = 'Nightwish Lane'
ag.address2 = ''
ag.city = 'Kitee'
ag.state = 'FI'
ag.zip = '87272'
ag.security_question = 'What instrument do you play??'
ag.security_answer = 'Bass Guitar'
ag.appointmentDate = datetime.datetime.now()
ag.save()

mgroup.user_set.add(u)


ag = hmod.Agent()
ag.username = 'Jukka'
ag.set_password('password')
ag.first_name = 'Jukka'
ag.last_name = 'Nevalainen'
ag.email = 'juk@nev.com'
ag.address1 = 'Oceanborn Lane'
ag.address2 = ''
ag.city = 'Oulu'
ag.state = 'WW'
ag.zip = '44354'
ag.security_question = 'What do you play?'
ag.security_answer = 'Drums'
ag.appointmentDate = datetime.datetime.now()
ag.save()

mgroup.user_set.add(u)


s = hmod.Session()
s.expire_date = '2015-02-20'
s.session_date = datetime.datetime.now()
s.user = hmod.Users.objects.get(username='Samus')
s.save()

s = hmod.Session()
s.expire_date = '2015-02-21'
s.session_date = datetime.datetime.now()
s.user = hmod.Users.objects.get(username='Link')
s.save()


sc = hmod.Shopping_Cart()
sc.session = hmod.Session.objects.get(expire_date='2015-02-20')
sc.save()

sc = hmod.Shopping_Cart()
sc.session = hmod.Session.objects.get(expire_date='2015-02-21')
sc.save()

p = hmod.Product()
p.name = 'Colonial Hat'
p.price = '20.99'
p.description = 'A tricorn hat used in the late 1700s'
p.manufacturer = 'Hatco'
p.average_cost = '15.99'
p.sku = '1110'
p.order_form_name = ''
p.production_time = ''
p.category = ''
p.save()

p = hmod.Product()
p.name = 'Miniature Liberty Bells'
p.price = '8.99'
p.description = 'Small Replica Liberty Bells'
p.manufacturer = 'ministatues'
p.average_cost = '3.25'
p.sku = '1111'
p.order_form_name = ''
p.production_time = ''
p.category = ''
p.save()

p = hmod.Product()
p.name = 'Printer Breeches'
p.price = '30.99'
p.description = 'size 36x32 magenta colonial style'
p.manufacturer = 'Korby'
p.average_cost = '20.99'
p.sku = '1112'
p.order_form_name = ''
p.production_time = ''
p.category = ''
p.save()

p = hmod.Product()
p.name = 'Personal Wood Burning'
p.price = '15.99'
p.description = 'Recieve orders of words or drawing to burn into a piece of wood'
p.manufacturer = 'Stan Lee'
p.average_cost = '5.99'
p.sku = '1113'
p.order_form_name = ''
p.production_time = ''
p.category = ''
p.save()

sp = hmod.Stocked_Product()
sp.name = 'Rifle'
sp.price = '45.99'
sp.description = 'A non-functional replica rifle of revolutionary era rifle'
sp.manufacturer = 'RevTime'
sp.average_cost = '35.99'
sp.sku = '1114'
sp.order_form_name = ''
sp.production_time = ''
sp.category = ''
sp.quantity_on_hand = '10'
sp.order_field = ''
sp.save()

sp = hmod.Stocked_Product()
sp.name = 'Chair'
sp.price = '39.99'
sp.description = 'A classic chair used in colonial times'
sp.manufacturer = 'Chair guys'
sp.average_cost = '18.99'
sp.sku = '1115'
sp.order_form_name = ''
sp.production_time = ''
sp.category = ''
sp.quantity_on_hand = '35'
sp.order_field = ''
sp.save()

cl = hmod.Cart_Line_Item()
cl.quantity = '2'
cl.stocked_product = hmod.Stocked_Product.objects.get(name='Chair')
cl.save()

cl = hmod.Cart_Line_Item()
cl.quantity = '2'
cl.stocked_product = hmod.Stocked_Product.objects.get(name='Rifle')
cl.save()

sep = hmod.Serialized_Product()
sep.name = 'CHF Keychain'
sep.price = '5.99'
sep.description = 'A keychain with the CHF logo'
sep.manufacturer = 'ChainGang'
sep.average_cost = '3.99'
sep.sku = '1115'
sep.order_form_name = ''
sep.production_time = ''
sep.category = ''
sep.quantity_on_hand = '35'
sep.order_field = ''
sep.serial_number = '0001'
sep.date_acquired = '2011-06-17'
sep.cost = '3.99'
sep.status = 'good'
sep.for_sale = False
sep.condition_new = 'unused'
sep.notes = 'brand new ready for individual sale'
sep.save()

sep = hmod.Serialized_Product()
sep.name = 'Replica Canon'
sep.price = '200.99'
sep.description = 'Replica canon of Revolutionary War canon'
sep.manufacturer = 'Revar'
sep.average_cost = '150.99'
sep.sku = '1118'
sep.order_form_name = ''
sep.production_time = ''
sep.category = ''
sep.quantity_on_hand = '4'
sep.order_field = ''
sep.serial_number = '0002'
sep.date_acquired = '2009-09-23'
sep.cost = '130.99'
sep.status = 'good'
sep.for_sale = True
sep.condition_new = 'used'
sep.notes = 'owned since 2010'
sep.save()

w = hmod.WardrobeItem()
w.name = 'Revolutionary Era Shoes'
w.price = '50.99'
w.description = 'Penny Loafer Shoes'
w.manufacturer = 'Shoe Specialists'
w.average_cost = '45.99'
w.sku = '1120'
w.order_form_name = ''
w.production_time = ''
w.category = ''
w.quantity_on_hand = '2'
w.order_field = ''
w.serial_number = '0003'
w.date_acquired = '2012-05-06'
w.cost = '30.99'
w.status = 'used'
w.for_sale = True
w.condition_new = 'used'
w.notes = 'used'
w.size = 'mens 10'
w.size_modifier = 'narrow'
w.gender = 'male'
w.color = 'brown'
w.pattern = ''
w.start_year = '1710'
w.end_year = '1780'
w.save()

tr = hmod.Transaction()
tr.customer = hmod.Users.objects.get(username='Samus')
tr.date = '2015-03-02'
tr.phone = '201-889-4587'
tr.date_packed = '2015-03-02'
tr.date_shipped = '2015-03-02'
tr.packed_by = hmod.Agent.objects.get(username='Tuomas')
tr.shipped_by = hmod.Agent.objects.get(username='Jukka')
tr.tracking_number = '10'
tr.save()

tr = hmod.Transaction()
tr.customer = hmod.Users.objects.get(username='Link')
tr.date = '2015-03-01'
tr.phone = '720-554-6851'
tr.date_packed = '2015-03-01'
tr.date_shipped = '2015-03-01'
tr.packed_by = hmod.Agent.objects.get(username='Jukka')
tr.shipped_by = hmod.Agent.objects.get(username='Marco')
tr.tracking_number = '15'
tr.save()

li = hmod.Line_Item()
li.amount = '23.75'
li.transaction = hmod.Transaction.objects.get(tracking_number='10')
li.save()

li = hmod.Line_Item()
li.amount = '5.99'
li.transaction = hmod.Transaction.objects.get(tracking_number='15')
li.save()

sai = hmod.Sale_Item()
li.amount = '21.99'
li.transaction = hmod.Transaction.objects.get(tracking_number='15')
sai.quantity = '6'
sai.product = hmod.Stocked_Product.objects.get(name='Chair')
sai.save()

sai = hmod.Sale_Item()
li.amount = '5.99'
li.transaction = hmod.Transaction.objects.get(tracking_number='15')
sai.quantity = '6'
sai.product = hmod.Stocked_Product.objects.get(name='Rifle')
sai.save()

rp = hmod.Rental_Product()
rp.name = 'Colonial Vest'
rp.price = '40.99'
rp.description = 'A Paul Revere replica vest'
rp.manufacturer = '4Fathers'
rp.average_cost = '35.99'
rp.sku = '1125'
rp.order_form_name = ''
rp.production_time = ''
rp.category = ''
rp.quantity_on_hand = '1'
rp.order_field = ''
rp.serial_number = '0005'
rp.date_acquired = '2014-05-24'
rp.cost = '20.99'
rp.status = 'used'
rp.for_sale = True
rp.condition_new = 'used'
rp.notes = 'used since 2009'
rp.size = 'large'
rp.size_modifier = ''
rp.gender = 'male'
rp.color = 'magenta'
rp.pattern = ''
rp.start_year = '1725'
rp.end_year = '1795'
rp.is_wardrobe_item = True
rp.times_rented = '11'
rp.price_per_day = '2.59'
rp.replacement_price = '30.99'
rp.save()

rp = hmod.Rental_Product()
rp.name = 'Colonial Pantaloons'
rp.price = '38.99'
rp.description = 'Revolutionary era pantaloons'
rp.manufacturer = '4Fathers'
rp.average_cost = '33.99'
rp.sku = '1127'
rp.order_form_name = ''
rp.production_time = ''
rp.category = ''
rp.quantity_on_hand = '1'
rp.order_field = ''
rp.serial_number = '0006'
rp.date_acquired = '2015-04-23'
rp.cost = '19.99'
rp.status = 'used'
rp.for_sale = True
rp.condition_new = 'used'
rp.notes = 'used since 2011'
rp.size = 'large'
rp.size_modifier = ''
rp.gender = 'male'
rp.color = 'beige'
rp.pattern = ''
rp.start_year = '1700'
rp.end_year = '1800'
rp.is_wardrobe_item = True
rp.times_rented = '9'
rp.price_per_day = '2.90'
rp.replacement_price = '30.99'
rp.save()

ri = hmod.Rented_Item()
ri.amount = '12.99'
ri.transaction = hmod.Transaction.objects.get(tracking_number='10')
ri.date_out = '2015-03-01'
ri.date_due = '2015-03-05'
ri.date_in = None
ri.discount_percent = '0.00'
ri.rental_product = hmod.Rental_Product.objects.get(serial_number='0005')
ri.renter = hmod.Users.objects.get(username='Aaron')
ri.save()

ri = hmod.Rented_Item()
ri.amount = '5.99'
ri.transaction = hmod.Transaction.objects.get(tracking_number='15')
ri.date_out = '2015-03-09'
ri.date_due = '2015-01-1'
ri.date_in = None
ri.discount_percent = '0.00'
ri.rental_product = hmod.Rental_Product.objects.get(serial_number='0006')
ri.renter = hmod.Users.objects.get(username='Aaron')
ri.save()

f = hmod.Fee()
f.amount = '23.75'
f.transaction = hmod.Transaction.objects.get(tracking_number='10')
f.waived = False
f.rented_item = hmod.Rented_Item.objects.get(amount='5.99')
f.save()

f = hmod.Fee()
f.amount = '18.00'
f.transaction = hmod.Transaction.objects.get(tracking_number='15')
f.waived = False
f.rented_item = hmod.Rented_Item.objects.get(amount='12.99')
f.save()

lf = hmod.Late_Fee()
lf.amount = '23.75'
lf.transaction = hmod.Transaction.objects.get(tracking_number='10')
lf.waived = False
lf.rented_item = hmod.Rented_Item.objects.get(amount='12.99')
lf.days_late = '2'
lf.save()

df = hmod.Damage_Fee()
df.amount = '18.00'
df.transaction = hmod.Transaction.objects.get(tracking_number='15')
df.waived = False
df.rented_item = hmod.Rented_Item.objects.get(amount='12.99')
df.description = 'additional signs of wear and tear'
df.save()

e = hmod.Event()
e.name = 'Boston Reenactment'
e.type = 'Large Reenactment'
e.location = 'Orem Park'
e.description = '6 areas and lots of roles'
e.start_date = '2015-06-01'
e.end_date = '2015-06-15'
e.address1 = '145 State St.'
e.address2 = ''
e.city = 'Orem'
e.state = 'UT'
e.zip = '84606'
e.save()

e = hmod.Event()
e.name = 'Declaration of Independence Reenactment'
e.type = 'Event Reenactment'
e.location = 'Provo Library'
e.description = 'A reenactment of the meeting where congress declared independence from England'
e.start_date = '2015-08-15'
e.end_date = '2015-09-05'
e.address1 = '544 University Ave'
e.address2 = ''
e.city = 'Provo'
e.state = 'UT'
e.zip = '84606'
e.save()

e = hmod.Event()
e.name = 'Revolutionary Era Reenactment'
e.type = 'Era Reenactment'
e.location = 'Kiwanis Park'
e.description = 'A reenactment of the general lifestyle during the revolutionary time period'
e.start_date = '2015-10-14'
e.end_date = '2015-10-28'
e.address1 = '800 N'
e.address2 = ''
e.city = 'Provo'
e.state = 'UT'
e.zip = '84606'
e.save()

a = hmod.Area()
a.aname = 'Home1'
a.description = 'Example of a standard home setup of the time period'
a.coordinator = hmod.Agent.objects.get(username='Jukka')
a.supervisor = hmod.Agent.objects.get(username='Tuomas')
a.event = hmod.Event.objects.get(name='Revolutionary Era Reenactment')
a.save()

a = hmod.Area()
a.aname = 'Church'
a.description = 'A standard church setup and reenactment for the time period'
a.coordinator = hmod.Agent.objects.get(username='Tuomas')
a.supervisor = hmod.Agent.objects.get(username='Marco')
a.event = hmod.Event.objects.get(name='Revolutionary Era Reenactment')
a.save()

a = hmod.Area()
a.aname = 'Fake Lighthouse'
a.description = 'A standard church setup and reenactment for the time period'
a.coordinator = hmod.Agent.objects.get(username='Tuomas')
a.supervisor = hmod.Agent.objects.get(username='Marco')
a.event = hmod.Event.objects.get(name='Revolutionary Era Reenactment')
a.save()

es = hmod.Expected_Sale_Item()
es.name = 'Tomahawk'
es.description = 'A replica indian tomahawk'
es.low_price = '15.99'
es.high_price = '30.99'
es.area = hmod.Area.objects.get(aname='Home1')
es.save()

es = hmod.Expected_Sale_Item()
es.name = 'Model Lighthouse'
es.description = 'A miniature lighthouse replica'
es.low_price = '19.99'
es.high_price = '35.99'
es.area = hmod.Area.objects.get(aname='Fake Lighthouse')
es.save()

es = hmod.Expected_Sale_Item()
es.name = 'Old Tome'
es.description = 'A dusty, old tome'
es.low_price = '10.99'
es.high_price = '20.99'
es.area = hmod.Area.objects.get(aname='Church')
es.save()

hf = hmod.Historical_Figure()
hf.name = 'Paul Revere'
hf.birthdate = '1720-06-26'
hf.birthplace = 'Boston'
hf.deathdate = '1789-12-08'
hf.is_functional = True
hf.bio = 'Paul Revere was a member of the Sons of Liberty that is famous for riding his horse to warn the Americans that the British were coming'
hf.save()

hf = hmod.Historical_Figure()
hf.name = 'John Adams'
hf.birthdate = '1735-08-22'
hf.birthplace = 'Boston'
hf.deathdate = '1805-07-07'
hf.is_functional = True
hf.bio = 'A lawyer who was always a controversial figure but ended up becoming the 3rd US President'
hf.save()

ro = hmod.Role()
ro.name = 'Lawyer John Adams'
ro.type = 'Real Person'
ro.historical_figure = hmod.Historical_Figure.objects.get(name='John Adams')
ro.save()