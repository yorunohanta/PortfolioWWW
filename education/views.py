from django.shortcuts import render

# Create your views here.
def education_page(request):
    return render(request, 'education.html')
