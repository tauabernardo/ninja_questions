from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def upload_page(request):
    return render(request, "upload.html")
