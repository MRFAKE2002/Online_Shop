from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path("", views.product_list_view, name="product_list"),
    path("detail/<int:product_id>/", views.product_detail_view, name="product_detail"),
    path("search/", views.search_view, name="search"),
]
