from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:id>/", views.article_detail, name="article_detail"),
    path("articles", views.articles_list, name="articles_list"),
]