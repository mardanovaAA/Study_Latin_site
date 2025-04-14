from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import phrases_work

def index(request):
    '''
    Function for rendering main page
    '''
    return render(request, "index.html")

def terms_list(request):
    '''
    Function for rendering page with list of latin terms
    '''
    terms = terms_work.get_terms_for_table()
    return render(request, "terms_list.html", context={"terms": terms})
    # return render(request, "terms_list.html")

def phrases_list(request):
    '''
    Function for rendering page with list of latin phrases
    '''
    phrases = phrases_work.get_phrases_for_table()
    return render(request, "phrases_list.html", context={"phrases": phrases})

def add_term(request):
    '''
    Function for rendering page for adding a new latin term
    '''
    return render(request, "add_term.html")

def add_phrase(request):
    '''
    Function for rendering page for adding a new latin phrase
    '''
    return render(request, "add_phrase.html")

def send_term(request):
    '''
    Function for work with request of posting new term
    '''
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
            terms_work.write_term(latin_term, transcription_term, translation_term, category_term)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "adding_request.html", context)
    else:
        add_term(request)

def send_phrase(request):
    '''
    Function for work with request of posting new phrase
    '''
    if request.method == "POST":
        cache.clear()
        latin_phrase = request.POST.get("latin_phrase")
        transcription_phrase = request.POST.get("transcription_phrase")
        translation_phrase = request.POST.get("translation_phrase")
        source_phrase = request.POST.get("source_phrase")
        context = {}
        if len(latin_phrase) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        elif len(transcription_phrase) == 0:
            context["success"] = False
            context["comment"] = "Транскрипция должна быть не пустой"
        elif len(translation_phrase) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(source_phrase) == 0:
            context["success"] = False
            context["comment"] = "Источник должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят!"
            phrases_work.write_term(latin_phrase,transcription_phrase,
                                    translation_phrase,source_phrase)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "adding_request.html", context)
    else:
        add_term(request)
