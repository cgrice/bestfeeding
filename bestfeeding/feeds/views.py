# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Feed
from .forms import FeedForm

from datetime import datetime

def home(request):
	feeds = Feed.objects.all().order_by('-start_time')

	if request.method == 'POST': # If the form has been submitted...
		form = FeedForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			new_feed = Feed()
			new_feed.side = form.cleaned_data['side']
			new_feed.shield = form.cleaned_data['shield']
			new_feed.save()
			new_feed.start_time = new_feed.round_time(
				new_feed.start_time,
				15*60
			)
			new_feed.save()
			# Process the data in form.cleaned_data
	    		# ...
			return HttpResponseRedirect('/') # Redirect after POST
	else:
		form = FeedForm() # An unbound form

	diff = (datetime.now() - feeds[0].start_time).seconds / 60

	return render(request, 'feeds/feed_form.html', {
		'diff': diff,
		'form': form,
		'feeds': feeds,
	})

class FeedCreateView(CreateView):
	model = Feed
	form_class = FeedForm
