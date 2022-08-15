from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.http import HttpResponse
from django.template import loader

from .models import Keyword


def index(request):
    latest_keyword_list = Keyword.objects.order_by('-pub_date')[:5]
    context = {'latest_keyword_list': latest_keyword_list}
    return render(request, 'quotes_app/index.html', context)


def detail(request, keyword_id):
    keyword = get_object_or_404(Keyword, pk=keyword_id)
    return render(request, 'quotes_app/detail.html', {'keyword': keyword})


def results(request, keyword_id):
    response = "You're looking at the results of keyword %s."
    return HttpResponse(response % keyword_id)


def vote(request, keyword_id):
    return HttpResponse("You're voting on keyword %s." % keyword_id)
