from django.shortcuts import render
from django.utils import timezone
from .models import Pattern

def pattern_list(request):
    patterns = Pattern.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'couture/pattern_list.html', {'patterns' : patterns})
