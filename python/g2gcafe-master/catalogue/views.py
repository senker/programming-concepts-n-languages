from django.shortcuts import render
from catalogue.models import Catalogue


def drink_menu(request):
    drink = Catalogue()
    menu = drink.display_menu()
    context = {"menu": menu}
    return render(request, "menu.html", context)


def order_drink(request):
    drink = Catalogue()
    if request.method == "POST":
        drink_kind = request.POST.get("drink_kind")
        drink_size = request.POST.get("drink_size")
        quantity = int(request.POST.get("quantity"))
        drink.set_price(drink_kind, drink_size, quantity)
    menu = drink.display_menu()
    context = {"menu": menu, "price": drink.price}
    return render(request, "order.html", context)
