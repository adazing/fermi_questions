from django.shortcuts import render
from .forms import *

# Create your views here.

# view to add repository
def create_repository(request):
    form = RepositoryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # create repository
            

# view to add files to repository + process files

# home view to see all repositories

# repository view to see all the files

# file view to see all the questions and what questions get wrong the most

