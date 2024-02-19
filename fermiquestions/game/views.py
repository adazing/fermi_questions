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
        game = Game.objects.create(repository = repository, total_score = 0, questions_done = 0)
    
    # Sort questions by usefulness
    if game.previous_question == None:
        questions = Question.objects.filter(repository=repository).annotate(total_score = Sum(F('experience')) + F('skill'))
        questions = questions.order_by('total_score')
        questions = list(questions)
    else:
        questions = Question.objects.exclude(id=game.previous_question.id).filter(repository=repository).annotate(total_score = Sum(F('experience')) + F('skill'))
        questions = questions.order_by('total_score')
        questions = list(questions)
        questions.append(Question.objects.filter(id=game.previous_question.id).annotate(total_score = Sum(F('experience')) + F('skill'))[0])
    # GAME.PREVIOUS QUESTION DOES NOT HAVE TOTAL SCORE
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

def get_initial_info(request, repository_id):
    repository = get_object_or_404(Repository, id=repository_id)
    if Game.objects.filter(repository = repository).exists():
        game = Game.objects.get(repository = repository)
        return JsonResponse({'questions_done': game.questions_done, 'total_score':game.total_score})
    return JsonResponse({'questions_done': 0, 'total_score':0})

@require_POST
def check_question_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    game = Game.objects.get(repository = question.repository)
    answer = int(request.POST.get("answer"))
    question.experience+=1
    game.previous_question = question
    game.questions_done += 1
    print(type(question.answer))
    print(type(answer))
    if question.answer == answer:
        question.skill+=5
        game.total_score += 5
        color = "#00ff1a"
        game.save()
        question.save()
        return JsonResponse({'result':5, 'actual_answer': question.answer, 'color':color, 'questions_done': game.questions_done, 'total_score':game.total_score})
    elif question.answer-1 <= answer <= question.answer+1:
        question.skill+=3
        game.total_score += 3
        color = "#ffff00"
        game.save()
        question.save()
        return JsonResponse({'result':3, 'actual_answer': question.answer, 'color':color, 'questions_done': game.questions_done, 'total_score':game.total_score})
    elif question.answer-2 <= answer <= question.answer+2:
        question.skill+=1
        game.total_score += 1
        color="#ffa200"
        game.save()
        question.save()
        return JsonResponse({'result':1, 'actual_answer': question.answer, 'color':color, 'questions_done': game.questions_done, 'total_score':game.total_score})
    else:
        color="#ff6554"
        game.save()
        question.save()
        return JsonResponse({'result':0, 'actual_answer': question.answer, 'color': color, 'questions_done': game.questions_done, 'total_score':game.total_score})

@require_POST
def delete_question(request):
    question_id = request.POST.get("question_id")
    print(question_id)
    try:
        question = Question.objects.get(id = question_id)
        question.delete()
        return JsonResponse({"success": True})
    except File.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'File does not exist'}, status = 404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status = 500)


def reset_game(request, repository_id):
    repository = get_object_or_404(Repository, id=repository_id)
    form = ConfirmGameResetForm(request.POST or None)
    if form.is_valid():
        # there is a game already made for the repository
        if Game.objects.filter(repository = repository).exists():
            game = Game.objects.get(repository = repository)
            questions = Question.objects.filter(repository = repository)
            for q in questions:
                q.experience = 0
                q.skill = 0
                q.save()
            game.total_score = 0
            game.questions_done = 0
            game.previous_question = None
            game.save()
            return redirect('game', repository_id)
    context = {
        'form': form,
        'item': repository.name,
    }
    return render(request, 'game/confirm_game_reset.html', context)
