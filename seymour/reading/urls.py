from django.conf.urls import patterns, url

from .views import FeedCreateView, FeedDetailView, FeedDeleteView, FeedListView

urlpatterns = patterns('',
	url(
		regex=r'add/$',
		view=FeedCreateView.as_view(),
		name='subscription_create'
	),
	url(
		regex=r'delete/(?P<pk>\d+)/$',
		view=FeedDeleteView.as_view(),
		name='subscription_delete'
	),
	url(
		regex=r'(?P<pk>\d+)/$',
		view=FeedDetailView.as_view(),
		name='subscription_detail'
	),
	url(
		regex=r'^$',
		view=FeedListView.as_view(),
		name='subscription_list'
	),
)
