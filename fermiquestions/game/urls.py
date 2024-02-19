from django.urls import path, re_path
from . import views

urlpatterns = [
   path('game/<str:pk>/', views.game, name="create_repository"),
   path('generate-next-question/<str:repository_id>/', views.generate_next_question, name="generate_next_question"),
   path('check-question-answer/<str:question_id>/', views.check_question_answer, name = "check_question_answer"),
]