from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mouvement import views

urlpatterns = [
    path('', views.api_root),
    path('mouvements/', views.ListeMouvements.as_view(), name='liste-mouvements'),
    path('mouvements/<int:pk>/', views.DetailMouvement.as_view(), name='detail-mouvement'),
    # path('mouvements/<int:pk>/personne/', views.DetailPerimetreHtml.as_view()),
    path('machines/', views.ListeAnnuaires.as_view()),
    path('machines/<int:pk>/', views.DetailAnnuaire.as_view()),
    path('mobiles/', views.ListeClients.as_view()),
    path('mobiles/<int:pk>/', views.DetailClient.as_view()),
    path('personnes/', views.ListeUsers.as_view(), name='liste-users'),
    path('personnes/<int:pk>/', views.DetailUser.as_view(), name='detail-user'),
    path('projets/', views.ListeUsers.as_view(), name='liste-users'),
    path('projets/<int:pk>/', views.DetailUser.as_view(), name='detail-user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)