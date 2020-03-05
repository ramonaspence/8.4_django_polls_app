from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        ## returns first five objects with a published date ordered by most recent from the current time.


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) ##get_object_or_404 is well named. it either gets the object or 404s.
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) ## `get`s the choices by the pk
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
    'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1 ##adds vote!
        selected_choice.save() ## and saves it of course
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        ##once the vote is added the user will be redirected to polls:results, which is the 'results' url in the polls app,
        ##with the id of the question that was voted on.
