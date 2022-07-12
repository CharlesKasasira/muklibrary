from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path("login", views.login_user, name="login"),
  path("logout", views.logout_user, name="logout"),
  path("register", views.register_user, name="register"),
  # path("", views.home, name="home"),
  path("", login_required(login_url='login')(views.BookListView.as_view()), name="book-list"),
  path(

        "book/<int:pk>",

        login_required(login_url='login')(views.BookDetailView.as_view()),

        name="book-detail"

    ),
]