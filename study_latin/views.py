from django.shortcuts import render
from django.core.cache import cache


def index(request):
    return render(request, "index.html")

def terms_list(request):
    return render(request, "terms_list.html")

def phrases_list(request):
    return render(request, "phrases_list.html")

def add_term(request):
    return render(request, "add_term.html")

def add_phrase(request):
    return render(request, "add_phrase.html")
