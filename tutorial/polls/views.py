from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


# Create your views here.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail_question.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/vote.html')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        c = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        render(request, 'polls/detail_question.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        c.votes = F('votes') + 1
        c.save()
    return render(request, 'polls/vote.html', {'question': question})


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join(q.question for q in latest_question_list)
    # return HttpResponse(output)
    my_name = 'phúc'
    game = {'fo4', 'lmht'}
    context = {'name': my_name, 'game': game}
    return render(request, 'polls/index.html', context)


def list_question(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/question_list.html', context)
