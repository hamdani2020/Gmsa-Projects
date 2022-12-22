from django.shortcuts import render
from . models import *
import random


# Hadith Models
def index(request):
    hadith = Hadith.objects.all()[0:7]
    try:
        daily = random.choice(Hadith.objects.all())
    except:
        daily = ''
    context = { "hadith":hadith,
                "daily":daily,
                }
    return render(request, 'index.html',context)