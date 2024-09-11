from django.shortcuts import render

# Create your views here.


def show_main(request):
    context = {
        "npm": "2406394881",
        "name": "Naïm Baziz",
        "class": "PBP KKI",
        "appName": "ecommerce",
    }

    return render(request, "main.html", context)
