from django import forms
from django.forms.widgets import HiddenInput, RadioSelect
from django.forms.models import inlineformset_factory

from .models import Feed

class FeedForm(forms.ModelForm):

	class Meta:
		model = Feed


class FeedEntryForm(forms.ModelForm):
	
    date = models.CharField(max_length=16)
    time = models.CharField(max_length=16)

	class Meta:
		model = Feed
        fields = ['side']
