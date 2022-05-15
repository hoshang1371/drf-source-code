from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Articale
# from django.shortcuts import render

class ArticleList(ListView):
    def get_queryset(self):
        return Articale.objects.filter(status=True)

class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            Articale.objects.filter(status=True),
            pk=self.kwargs.get("pk")
            )