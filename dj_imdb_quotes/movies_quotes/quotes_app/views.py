from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Keyword, Quote
from django.urls import reverse


def index(request):
    latest_keyword_list = Keyword.objects.order_by('-pub_date')[:5]
    context = {'latest_keyword_list': latest_keyword_list}
    return render(request, 'quotes_app/index.html', context)


def detail(request, keyword_id):
    keyword = get_object_or_404(Keyword, pk=keyword_id)
    return render(request, 'quotes_app/detail.html', {'keyword': keyword})


def results(request, keyword_id):
    keyword = get_object_or_404(Keyword, pk=keyword_id)
    return render(request, 'quotes_app/results.html', {'keyword': keyword})


def vote(request, keyword_id):
    keyword = get_object_or_404(Keyword, pk=keyword_id)

    try:
        selected_quote = keyword.quote_set.get(pk=request.POST['quote'])
    except (KeyError, Quote.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quotes_app/detail.html', {
            'keyword': keyword,
            'error_message': "You didn't select a quote.",
        })
    else:
        selected_quote.votes += 1
        selected_quote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quotes_app:results', args=(keyword.id,)))

