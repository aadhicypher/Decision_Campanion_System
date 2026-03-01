from django.urls import path
from . import views

urlpatterns = [
    path("", views.decision_form, name="decision_form"),
    path("questions/", views.questions_page, name="questions_page"),
]