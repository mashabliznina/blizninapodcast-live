from os import name
from django.urls import path
from .views import HomePageView, ContactPageView, EpisodePageView, EpisodesListView, FeedbackPageView, SubscribePageView

urlpatterns = [
path('feedback/', FeedbackPageView.as_view(), name='feedback'),
path('subscribe/', SubscribePageView.as_view(), name='subscribe'),
path('contact_page/', ContactPageView.as_view(), name='contact_page'),
path('episodes/', EpisodesListView.as_view(), name='episodes_list'),
path('episodes/<int:pk>/', EpisodePageView.as_view(), name='episode_details'),
path('', HomePageView.as_view(), name='home_page'),
]