from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.category_list),
    re_path(r"^cat/(?P<category_id>\d+)/$", views.products_category),
]