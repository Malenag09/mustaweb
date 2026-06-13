
from django import forms
from .models import Song, Booking, Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SongForm(forms.ModelForm):
 class Meta:
    model=Song
    fields='__all__'
class SignupForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','password1', 'password2','email']
class BookingForm(forms.ModelForm):
  class Meta:
      model=Booking
      fields=['phone_number','event_date','event_location','message',
      'customer_name']
class ArtistForm(forms.ModelForm):
  class Meta:
    model=Artist
    fields=['stage_name', 'profile_image','bio', 'whatsapp_number']
    widgets={
      'stage_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Artist Name'}),
      'bio':forms.Textarea(attrs={'class':'form-control', 'rows':10, 'placeholer':'Tell fans about yourself'}),
      'genre':forms.TextInput(attrs={'class':'form-control', 'rows':5,'placeholder':'hiphop, gospel, dancehall,afrobeats, etc' }),
      'whatsapp_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':+256}),
      
    }