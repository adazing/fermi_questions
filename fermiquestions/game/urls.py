from django.urls import path, re_path
from . import views

urlpatterns = [
   path('game/<str:pk>/', views.game, name="game"),
   path('generate-next-question/<str:repository_id>/', views.generate_next_question, name="generate_next_question"),
   path('check-question-answer/<str:question_id>/', views.check_question_answer, name = "check_question_answer"),
   path('reset-game/<str:repository_id>/', views.reset_game, name = "reset_game"),
   path('get-initial-info/<str:repository_id>/',views.get_initial_info, name="get_initial_info"),
]
