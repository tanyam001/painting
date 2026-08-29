from django.shortcuts import render
from .models import Painting
from django.views.generic import ListView, DetailView


class PaintingListView(ListView):
    model = Painting
    template_name = "painting_list.html"

class PaintingDetailView(DetailView):
    model = Painting
    template_name = "painting_detail.html"

