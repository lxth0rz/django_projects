from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /quotes_app/5/
    path('<int:keyword_id>/', views.detail, name='detail'),
    # ex: /quotes_app/5/results/
    path('<int:keyword_id>/results/', views.results, name='results'),
    # ex: /quotes_app/5/vote/
    path('<int:keyword_id>/vote/', views.vote, name='vote'),
]