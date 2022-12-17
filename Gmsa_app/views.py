from django.shortcuts import render
from . models import *
import random


# Hadith Models
def index(request):
    hadith = Hadith.objects.all()[1:7]
    daily = random.choice(Hadith.objects.all())
    context = { "hadith":hadith,
                "daily":daily,
                }
    return render(request, 'index.html',context)