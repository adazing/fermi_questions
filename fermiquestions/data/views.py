from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.serializers import serialize
# Create your views here.

# home view to see all repositories
def home(request):
    repositories = Repository.objects.all()
    context = {"repositories": repositories}
    return render(request, "data/home.html", context)

@require_POST
def delete_file(request):
    file_id = request.POST.get("file_id")
    try:
        file = File.objects.get(id = file_id)
        file.delete()
        return JsonResponse({"success": True})
    except File.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'File does not exist'}, status = 404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status = 500)
    
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

# view to add repository
def create_repository(request):
    form = RepositoryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # create repository
            Repository.objects.create(name=form.cleaned_data.get("name"))
    context = {"form":form}
    return render(request, "data/create_repository.html", context)

# confirm delete of repository
def delete_repository(request, pk):
    repository = get_object_or_404(Repository, id=pk)
    form = ConfirmDeleteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            repository.delete()
            return redirect("home")
    context = {
        "item" : "Repository "+repository.name,
        "form" : form,
    }
    return render(request, "data/confirm_delete.html", context)

# view to add files to repository + process files / repository view with files
def repository_view(request, pk):
    # repository
    repository = get_object_or_404(Repository, id=pk)
    # files
    repository_files = File.objects.filter(repository = repository)
    print(repository_files)
    
    form = AddFilesToRepositoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        files = request.FILES.getlist('file_field')
        # print(files)
        for f in files: # for all the files
            # create file object
            file = File.objects.create(repository = repository, name = f.name)
            # try:
            lines = f.read().splitlines() # read all the lines
            # print(lines)
            lines.pop(0) # pop the first line (title)
            lines.pop(0) # pop the second line (number of questions)
            
            index = 0
            while index<len(lines):
                # make question model
                question = Question.objects.create(file = file, query = lines[index].decode('utf-8'), answer = int(lines[index+1]), repository=repository)
                # increment index by 2
                index += 2
            # except:
            #     # if something goes wrong while reading the file, delete it!
            #     file.delete()
    context = {
        "repository" : repository,
        "repository_files" : repository_files,
        "form" : form,
    }
    return render(request, "data/repository_view.html", context)

# view to add questions to repository + question files / repository view
def repository_view_w_questions(request, pk):
    # repository
    repository = get_object_or_404(Repository, id=pk)
    
    # questions
    repository_questions = Question.objects.filter(file__repository = repository)
    
    # form to add question
    form = QuestionForm(request.POST or None)
    print("hi")
    print(form)

    if form.is_valid():
        # create question object
        question = Question.objects.create(query = form.cleaned_data.get("query"), answer = form.cleaned_data.get("answer"), repository=repository)

    context = {
        "repository" : repository,
        "repository_questions" : repository_questions,
        "form" : form,
    }
    return render(request, "data/wquestions_repository_view.html", context)

# def add_question(question, pk):
#     repository = request.POST.get("repository_id")
#     if form.is_valid():
#         # create question object
#         question = Question.objects.create(query = form.cleaned_data.get("query"), answer = form.cleaned_data.get("answer"), repository=form.cleaned_data.get("repository"))

# def add_question(request, pk):
#     if request.method == 'POST':
#         repository = get_object_or_404(Repository, id=pk)
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             query = form.cleaned_data.get("query")
#             answer = form.cleaned_data.get("answer")
#             question = Question.objects.create(query=query, answer=answer, repository=repository)
#             return JsonResponse({'success': True, 'question': {'query': question.query, 'answer': question.answer, 'id':question.id}})
#         else:
#             return JsonResponse({'success': False, 'errors': form.errors})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'})


def load_more_questions(request, repository_id, offset):
    # Fetch more questions based on the repository_id and offset
    print(repository_id)
    print(offset)
    repository = get_object_or_404(Repository, id=repository_id)
    print(repository)
    questions = Question.objects.filter(repository=repository)[offset:offset+30]  # Assuming you want to fetch 10 more questions
    # [offset:offset+10]
    print(questions)
    question_data=[]
    for q in questions:
        color = '#4a4a4a'
        if q.experience<0:
            color = '#de3737'
        elif q.experience>0:
            color = '#429654'
        
        question_data.append({"query":q.query, "color":color, "answer":q.answer, "id":q.id})
    # Serialize questions (convert queryset to JSON)
    print(question_data)
    return JsonResponse({'questions': question_data})

# delete files

# file view to see all the questions and what questions get wrong the most

