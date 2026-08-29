from django.urls import path
from django.views.generic import TemplateView
from .views import PaintingDetailView, PaintingListView

urlpatterns = [
    path("", PaintingListView.as_view(), name="painting_list"),
    path("painting/<int:pk>/", PaintingDetailView.as_view(), name="painting_detail"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
]