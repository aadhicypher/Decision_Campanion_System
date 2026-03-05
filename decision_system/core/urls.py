from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("questions/", views.questions_page, name="questions_page"),
    path("result/", views.result_page, name="result_page"),
    path("", views.home_page, name="home_page"),
    path("decision/", views.decision_form, name="decision_form"),
    path("history/<int:decision_id>/", views.decision_history, name="decision_history"),

]
