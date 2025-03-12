from django.urls import path
from .views import add_item, get_items, home
urlpatterns = [
    path("item/add/<str:name>",add_item),
    path("item/get",get_items),
    path("home",home),
]