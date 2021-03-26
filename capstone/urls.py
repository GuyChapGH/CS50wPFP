from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_question/", views.create_question, name="create_question"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
