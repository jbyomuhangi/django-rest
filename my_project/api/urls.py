from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("products/info/", views.products_info),
    path("products/<int:id>/", views.product_detail),
    path("orders/", views.order_list),
]
