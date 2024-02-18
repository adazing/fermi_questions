from django.urls import path, re_path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('create-repository/', views.create_repository, name="create_repository"),
   path('delete-repository/<str:pk>/', views.delete_repository, name='delete_repository'),
   path('view-repository/<str:pk>/', views.repository_view, name='repository_view'),
   path('view-repository/<str:pk>/questions', views.repository_view_w_questions, name='repository_view_w_questions'),
   path('delete-file/', views.delete_file, name='delete_file'),
   path('delete-question/', views.delete_question, name="delete_question"),
   path('load-more-questions/<int:repository_id>/<int:offset>/', views.load_more_questions, name='load_more_questions'),
#    path('add-question/<str:pk>/', views.add_question, name='add_question'),
]