import imp
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def ApiView(request):
    return JsonResponse(
        {"slackUsername": "Neon-jeff", "backend": True, "bio": "Free thinker, Robotic enthusiast, Andrew Tate"},
        safe=False
    )