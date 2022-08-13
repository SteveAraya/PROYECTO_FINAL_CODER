from django.shortcuts import render

# Create your views here.

def ContactUs(request):

    return render(request, './SendMessage.html')