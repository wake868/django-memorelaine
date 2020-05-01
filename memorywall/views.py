from django.shortcuts import render

def home(request):
    return render(request, 'memorywall/home.html')
