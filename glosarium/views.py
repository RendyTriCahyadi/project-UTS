from django.shortcuts import render

# Create your views here.
def glosarium(request):
    return render(request, 'glosarium/index.html')
