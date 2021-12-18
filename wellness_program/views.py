from django.shortcuts import render

def firstpage(request):
    return render(request, "firstpage.html")
def price(request):
    return render(request, "price.html")
def registration(request):
    return render(request, "registration.html")
def main_input(request):
    return render(request, "main_input.html")
def home(request):
    return render(request, "home.html")
def body_output(request):
    return render(request, "body_output.html")
def exercise(request):
    return render(request, "exercise.html")
# def burn_output(request):
#     return render(request, "burn_output.html")
def food(request):
    return render(request, "food.html")
def food_output(request):
    return render(request, "food_output.html")
def disease(request):
    return render(request, "disease.html")
def yoga(request):
    return render(request, "yoga.html")
# def kriya(request):
#     return render(request, "asans.html")
# def yog_nidra(request):
#     return render(request, "yognidra.html")
# def system_wise(request):
#     return render(request, "system-wise.html")
# def upnishdic(request):
#     return render(request, "upnishdik.html")
# def natal(request):
#     return render(request, "natal.html")
# def more(request):
#     return render(request, "more.html")