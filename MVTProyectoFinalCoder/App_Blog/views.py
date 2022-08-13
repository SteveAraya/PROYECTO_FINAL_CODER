from django.shortcuts import render

# Create your views here.

def BlogCreate(request):

    return render(request, './BlogCreate.html')