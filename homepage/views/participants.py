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
## Shows all participants
@view_function
def process_request(request):
    params = {}

    params['participants'] = hmod.Participant.objects.all().order_by('id')

    return templater.render_to_response(request, 'participants.html', params)

##########################################################################
### Edit a participant
@view_function
@permission_required('homepage.change_participant')
def edit(request):
    params = {}

    try:
      participant = hmod.Participant.objects.get(id=request.urlparams[0])
    except hmod.Participant.DoesNotExist:
      return HttpResponseRedirect('/homepage/participants/')

    form = ParticipantEditForm(initial={
      'username': participant.username,
      'password': participant.password,
      'first_name': participant.first_name,
      'last_name': participant.last_name,
      'email': participant.email,
      'address1': participant.address1,
      'city': participant.city,
      'state': participant.state,
      'zip': participant.zip,
      'security_question': participant.security_question,

       })


    if request.method == 'POST':
       form = ParticipantEditForm(request.POST)
       form.participantid = participant.id
       if form.is_valid():
           participant.username = form.cleaned_data['username']
           participant.set_password(form.cleaned_data['password'])
           participant.first_name = form.cleaned_data['first_name']
           participant.last_name = form.cleaned_data['last_name']
           participant.email = form.cleaned_data['email']
           participant.address1 = form.cleaned_data['address1']
           participant.city = form.cleaned_data['city']
           participant.state = form.cleaned_data['state']
           participant.zip = form.cleaned_data['zip']
           participant.security_question = form.cleaned_data['security_question']
           participant.biographicalSketch = form.cleaned_data['biographicalSketch']
           participant.contactRelationship = form.cleaned_data['contactRelationship']
           participant.role = form.cleaned_data['role']
           participant.save()
           return HttpResponseRedirect('/homepage/participants/')

    params['form'] = form
    params['participant'] = participant

    return templater.render_to_response(request, 'participants.edit.html', params)

##############################################################################
#########Create a participant
@view_function
@permission_required('homepage.create_participant')
def create(request):
    participant = hmod.Participant()
    participant.username= "Enter Username",
    participant.email="",
    participant.password="",
    participant.last_name="",
    participant.first_name="",
    participant.address1="",
    participant.zip= "",
    participant.city="",
    participant.state="",
    participant.biographicalSketch="",
    participant.contactRelationship="",
    participant.role="",
    participant.save()

    return HttpResponseRedirect('/homepage/participants.edit/{}'.format(participant.id))

#####################################################################
###Delete a participant
@view_function
@permission_required('homepage.delete_participant')
def delete(request):
     try:
        participant = hmod.Participant.objects.get(id=request.urlparams[0])
     except hmod.Participant.DoesNotExist:
        return HttpResponseRedirect('/homepage/participants/')

     participant.delete()
     return HttpResponseRedirect('/homepage/participants/'.format(participant.id))

#####################################################################
###Participant form

class ParticipantEditForm(forms.Form):
  participants = hmod.Participant.objects.all()

  username = forms.CharField(required=True, max_length= 100 )
  password = forms.CharField(required=True, max_length= 100 )
  first_name = forms.CharField(required=True, max_length= 100 )
  last_name = forms.CharField(required=True, max_length= 100 )
  email = forms.EmailField(required=True, max_length= 100 )
  address1 = forms.CharField(required=True, max_length= 100 )
  city = forms.CharField(required=True, max_length= 100 )
  state = forms.CharField(required=True, max_length= 100 )
  zip = forms.CharField(required=True, max_length= 100 )
  security_question = forms.CharField(required=True, max_length= 100 )
  biographicalSketch = forms.CharField(required=True, max_length= 100 )
  contactRelationship = forms.CharField(required=True, max_length= 100 )
  role = forms.CharField(required=True, max_length= 100 )

  def clean_username(self):
     if len(self.cleaned_data['username']) < 5:
        raise forms.ValidationError("Please enter at least 5 characters.")

     user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.participantid).count()
     if user_count >= 1:
        raise forms.ValidationError("That username is already taken.")
     return self.cleaned_data['username']



