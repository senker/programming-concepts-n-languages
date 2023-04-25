from django.shortcuts import render

def drink(request):
    return render(request, 'url/my_new_page.html')