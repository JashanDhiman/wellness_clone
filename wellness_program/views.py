from django.shortcuts import render

# Create your views here.
def firstpage(request):
    return render(request, "firstpage.html")
