from django.shortcuts import render

# Create your views here.
def register_complant(request):

    return render(request, 'complaint.html')