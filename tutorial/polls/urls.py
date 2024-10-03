from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('results/<int:question_id>/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('list/', views.list_question, name='list_question'),
    path('<int:question_id>/results', views.results, name='results'),
]
