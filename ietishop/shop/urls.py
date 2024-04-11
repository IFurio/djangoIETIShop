from django.urls import path
from . import views, api

urlpatterns = [
    path("", views.product_list),
    path("api/prods", api.getProducts),
    path("api/prods/<int:id_cat>", api.getProductsByCategory),
]