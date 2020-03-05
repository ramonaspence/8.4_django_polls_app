from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), ## <int:pk>, is called a value capture, with int specifying
    ## that it's looking for an integer, pk the 'key' it's looking for.
    ## it can be more specific like the path below. PK stands for primary key, but pk in this case is a variable(sort of).
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
]
