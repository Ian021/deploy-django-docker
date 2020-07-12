from django.shortcuts import render

# Create your views here.

def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')