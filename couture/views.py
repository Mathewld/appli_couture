from django.shortcuts import render

def pattern_list(request):
    return render(request, 'couture/pattern_list.html', {})
