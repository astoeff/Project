from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, Category
import random


class IndexView(generic.ListView):
    # template_name = 'polls/index.html'
    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Category.objects.all().order_by('price')


# class QuestionsView(generic.ListView):
#     model = Category
#     template_name = 'polls/questions.html'
#     # context_object_name = 'latest_question_list'

#     # def get_queryset(self):
#     #     """
#     #     Return the last five published questions (not including those set to be
#     #     published in the future).
#     #     """
#     #     return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = 'polls/detail.html'

    # def get_queryset(self):
    #     """
    #     Excludes any questions that aren't published yet.
    #     """
    #     items = Question.objects.all()
    #     random_item = random.choice(items)
    #     return random_item
    #     # return render(request, 'polls/detail.html', {
    #     #     'question': question,
    #     #     'error_message': "You didn't select a choice.",
    #     # })


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/q_detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/q_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id, selected_choice.id)))
        return render(request, 'polls/results.html', {'question': question, 'choice': selected_choice})


def choose_random(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    try:
        selected_choice = random.choice(category.question_set.all())
    except (KeyError, Category.DoesNotExist):
        # return render(request, 'polls/index.html', {})
        pass
    else:
        return HttpResponseRedirect(reverse('polls:q_detail', args=(selected_choice.id,)))


def result(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, 'polls/results', {'question': question, 'choice': choice})



# def home(request):
#     # question = get_object_or_404(Question, pk=question_id)
#     # try:
#     #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     # except (KeyError, Choice.DoesNotExist):
#     #     # Redisplay the question voting form.
#     #     return render(request, 'polls/detail.html', {
#     #         'question': question,
#     #         'error_message': "You didn't select a choice.",
#     #     })
#     # else:
#     #     selected_choice.votes += 1
#     #     selected_choice.save()
#     #     # Always return an HttpResponseRedirect after successfully dealing
#     #     # with POST data. This prevents data from being posted twice if a
#     #     # user hits the Back button.
#     return HttpResponseRedirect(reverse('polls:index'))
