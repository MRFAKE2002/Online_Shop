from django.urls import path

from . import views

app_name = 'category'

urlpatterns = [
    path("<slug>", views.category_list, name="category_list"),
]
