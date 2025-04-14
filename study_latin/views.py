from django.shortcuts import render
from django.core.cache import cache
from . import terms_work

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

def send_term(request):
    if request.method == "POST":

        cache.clear()
        latin_term = request.POST.get("latin_term")
        transcription_term = request.POST.get("transcription_term")
        translation_term = request.POST.get("translation_term")
        category_term = request.POST.get("category_term")
        context = {}
        if len(latin_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        elif len(transcription_term) == 0:
            context["success"] = False
            context["comment"] = "Транскрипция должна быть не пустой"
        elif len(translation_term) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(category_term) == 0:
            context["success"] = False
            context["comment"] = "Категория должна быть не пустой"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят!"
            print(0)
            terms_work.write_term(latin_term, transcription_term, translation_term, category_term)
            print(1)
        if context["success"]:
            context["success-title"] = ""
            print(1)
        return render(request, "term_request.html", context)
    else:
        add_term(request)
