from django.shortcuts import render

# Create your views here.
def latihan(request):
    return render(request, 'latihan/index.html')