from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Opus

class IndexView(generic.ListView):
    template_name = 'catalogue/index.html'

    def get_queryset(self):
        return Opus.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Opus
    template_name = 'catalogue/detail.html'
