from django import forms
from django.forms.widgets import HiddenInput, RadioSelect
from django.forms.models import inlineformset_factory

from .models import UserSubscription
from feeds.models import Feed

class UserSubscriptionForm(forms.ModelForm):
	
	feed_url = forms.CharField(max_length=512, label="Feed URL")

	class Meta:
		model = UserSubscription
		fields = ['feed_url']

	def __init__(self, user=None, *args, **kwargs):
		super(UserSubscriptionForm, self).__init__(*args, **kwargs)
		self._user = user

	def clean(self):
		feed_url = self.cleaned_data['feed_url']
		self._feed = Feed.objects.get_or_create(feed_url=feed_url)[0]

		return super(UserSubscriptionForm, self).clean()
		

	def save(self):
		self.instance.feed = self._feed
		self.instance.user = self._user

		return super(UserSubscriptionForm, self).save()
