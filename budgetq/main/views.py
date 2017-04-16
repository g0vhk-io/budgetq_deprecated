from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.core import serializers
# Create your views here.
from main.models import Reply
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.html import strip_tags
import json

def reply_view(request, key):
    r = Reply.objects.get(key=key)
    return render(request, 'reply.html', {'reply': r})

def index_view(request):
    return render(request, 'index.html')


def search_api_view(request):
    result = SearchQuerySet().filter(content=request.GET.get('q', ''))
    for x in result:
        print x.object
    return HttpResponse(json.dumps([{'key': x.object.key, 'director': x.object.director, 'year': x.object.year, 'question_short': strip_tags(x.object.question)[0:100] + "...", "answer_short": strip_tags(x.object.answer)[0:100] + "...", "member": x.object.member} for x in result][0:10]))
