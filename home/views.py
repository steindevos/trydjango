from django.shortcuts import render
from .models import Contact

# Create your views here.
def get_home(request):
    contacts = Contact.objects.all()
    return render(request, "home/index.html", {"contacts": contacts})
    