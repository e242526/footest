from django.shortcuts import render
from .models import Biz

# Create your views here.


def index(request):
    """View home page of ft."""

    num_bizs = Biz.objects.all().count()                                       

    return render(
        request,
        'index.html',
        context={'num_bizs': num_bizs},                                        
    )

