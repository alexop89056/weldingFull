from django.contrib import admin
from django.urls import path, include

import app.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("work/<str:slug>/", views.work_view, name="work_view"),
]