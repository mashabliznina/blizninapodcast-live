from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Episode


class HomePageView(ListView):
    template_name = 'home_page.html'
    model = Episode
    queryset = Episode.objects.order_by("-pk")[:4]

class ContactPageView(TemplateView):
    template_name = 'contacts_page.html'

class EpisodePageView(DetailView):
    model = Episode
    template_name = 'episode.html'

class EpisodesListView(ListView):
    model = Episode
    template_name = 'episodes.html'

class SubscribePageView(TemplateView):
    template_name = 'subscribe.html'

class FeedbackPageView(TemplateView):
    template_name = 'feedback.html'