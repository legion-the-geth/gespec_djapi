from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from perimetre import views

urlpatterns = [
    path('perimetres/', views.ListePerimetres.as_view()),
    path('perimetres/<int:pk>/', views.DetailPerimetre.as_view()),
    path('annuaires/', views.ListeAnnuaires.as_view()),
    path('annuaires/<int:pk>/', views.DetailAnnuaire.as_view()),
    path('clients/', views.ListeClients.as_view()),
    path('clients/<int:pk>/', views.DetailClient.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)