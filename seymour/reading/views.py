from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.http import HttpResponseRedirect

from braces.views import LoginRequiredMixin, UserFormKwargsMixin

from .models import UserSubscription, UserPage
from .forms import UserSubscriptionForm

from feeds.tasks import TaskFetchFeed


class FeedCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
	model = UserSubscription
	form_class = UserSubscriptionForm

	def form_valid(self, form):

		subscription = UserSubscription.objects.get(feed=form._feed, user=form._user)
		if (subscription):
			return HttpResponseRedirect(subscription.get_absolute_url())

		self._feed = feed

		return super(FeedCreateView, self).form_valid()

class FeedDeleteView(LoginRequiredMixin, DeleteView):
	model = UserSubscription


class FeedDetailView(LoginRequiredMixin, DetailView):
	model = UserSubscription

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()

		feed = self.object.feed
		feed.fetch()
			
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)

class FeedListView(LoginRequiredMixin, ListView):
	model = UserSubscription
	context_object_name = 'subscriptions'

	def get_queryset(self):
		feeds = UserSubscription.objects.filter(user=self.request.user)
		UserPage
		return feeds