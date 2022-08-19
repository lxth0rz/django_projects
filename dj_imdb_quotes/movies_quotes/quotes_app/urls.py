from django.urls import path

from . import views

app_name = 'quotes_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /quotes_app/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /quotes_app/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /quotes_app/5/vote/
    path('<int:keyword_id>/vote/', views.vote, name='vote'),
]