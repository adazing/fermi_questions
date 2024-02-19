from django.shortcuts import render
from .models import *
from data.models import *
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.serializers import serialize
from django.db.models import Avg, Max, Min
from django.db.models import F, Sum
from .forms import *
import random
# Create your views here.

'''
plan:
    - generate next question based on randomly chosen, least seen questions
    - store score
    - store previous question
    - display score and next question and previous question answer and previous question guess
    - timer?
    
'''

def game(request, pk):
    repository = get_object_or_404(Repository, id=pk)
    context = {
        "repository":repository,
    }
    return render(request, 'game/game.html', context)

def generate_next_question(request, repository_id):
    # Fetch more questions based on the repository_id and offset
    print(repository_id)
    print(request)
    repository = get_object_or_404(Repository, id=repository_id)
    if Game.objects.filter(repository=repository).exists():
        game = Game.objects.get(repository = repository)
    else:
        game = Game.objects.create(repository = repository, total_score = 0)
    
    # Sort questions by usefulness
    if game.previous_question == None:
        questions = Question.objects.filter(repository=repository).annotate(total_score = Sum(F('experience')) + F('skill'))
        questions = questions.order_by('total_score')
        questions = list(questions)
    else:
        questions = Question.objects.exclude(id=game.previous_question.id).filter(repository=repository).annotate(total_score = Sum(F('experience')) + F('skill'))
        questions = questions.order_by('total_score')
        questions = list(questions)
        questions.append(game.previous_question)
    
    # Shuffle questions with the same total score
    shuffled_questions = []
    start_index = 0
    for end_index in range(1, len(questions) + 1):
        if end_index == len(questions) or questions[end_index].total_score != questions[start_index].total_score:
            partition = questions[start_index:end_index]
            random.shuffle(partition)
            shuffled_questions.extend(partition)
            start_index = end_index
    
    chosen_question = shuffled_questions[0]
    question_data={"query":chosen_question.query, "id":chosen_question.id}
    print(question_data)
    return JsonResponse({'question': question_data})

@require_POST
def check_question_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    game = Game.objects.get(repository = question.repository)
    answer = int(request.POST.get("answer"))
    question.experience+=1
    game.previous_question = question
    print(type(question.answer))
    print(type(answer))
    if question.answer == answer:
        question.skill+=5
        game.total_score += 5
        return JsonResponse({'result':5, 'actual_answer': question.answer})
    elif question.answer-1 <= answer <= question.answer+1:
        question.skill+=3
        game.total_score += 3
        return JsonResponse({'result':3, 'actual_answer': question.answer})
    elif question.answer-2 <= answer <= question.answer+2:
        question.skill+=1
        game.total_score += 1
        return JsonResponse({'result':1, 'actual_answer': question.answer})
    else:
        return JsonResponse({'result':0, 'actual_answer': question.answer})

