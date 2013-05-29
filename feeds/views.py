# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Feed
from .forms import FeedForm, FeedEntryForm

from datetime import datetime, timedelta

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

    if len(feeds) > 0:
        if feeds[0].start_time < datetime.now():
            diff = readable_delta((datetime.now() - feeds[0].start_time).seconds)
        else:
            diff = False
    else:
        diff = False

    return render(request, 'feeds/home.html', {
        'diff': diff,
        'form': form,
        'feeds': feeds,
    })

def create(request):
    form = FeedEntryForm()
    return render(request, 'feeds/feed_form.html', {
        'form': form,
    })

def delete(request, feed_id):
    feed = Feed.objects.get(pk=feed_id)
    feed.delete()
    return HttpResponseRedirect('/') # Redirect after POST

def readable_delta(seconds):
    '''Returns a nice readable delta.

    readable_delta(1, 2)           # 1 second ago
    readable_delta(1000, 2000)     # 16 minutes ago
    readable_delta(1000, 9000)     # 2 hours, 133 minutes ago
    readable_delta(1000, 987650)   # 11 days ago
    readable_delta(1000)           # 15049 days ago (relative to now)
    '''

    delta = timedelta(seconds=seconds)

    # deltas store time as seconds and days, we have to get hours and minutes ourselves
    delta_minutes = delta.seconds // 60
    delta_hours = delta_minutes // 60

    ## show a fuzzy but useful approximation of the time delta
    if delta.days:
        return '%d day%s ago' % (delta.days, plur(delta.days))
    elif delta_hours:
        delta_minutes = delta_minutes % 60
        return '%d hour%s, %d minute%s ago' % (delta_hours, plur(delta_hours), delta_minutes, plur(delta_minutes))
    elif delta_minutes:
        return '%d minute%s ago' % (delta_minutes, plur(delta_minutes))
    else:
        return '%d second%s ago' % (delta.seconds, plur(delta.seconds))

def plur(it):
    '''Quick way to know when you should pluralize something.'''
    try:
        size = len(it)
    except TypeError:
        size = int(it)
    return '' if size==1 else 's'
