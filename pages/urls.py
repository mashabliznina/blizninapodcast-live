from django.urls import path
from .views import HomePageView, ContactPageView, EpisodePageView, EpisodesListView

urlpatterns = [
path('contact_page/', ContactPageView.as_view(), name='contact_page'),
path('episodes/', EpisodesListView.as_view(), name='episodes_list'),
path('episodes/<int:pk>/', EpisodePageView.as_view(), name='episode_details'),
path('', HomePageView.as_view(), name='home_page'),
]