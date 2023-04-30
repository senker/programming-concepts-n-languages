from django.contrib import admin
from django.urls import path
from catalogue.views import drink_menu, order_drink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', drink_menu, name="drink_menu"),
    path('', order_drink, name="order_drink"),
]
