from django.urls import path
from . import views
from .views import activiteDeleteView, activiteUpdateView, inscrireDeleteView, annonceListView, annonceDeleteView, annonceUpdateView
urlpatterns = [
    #path('', views.home, name='home'),


    path('presentation/', views.presentation, name='presentation'),
    path('annonces/', views.annonces, name='annonces'),
    path('activites/', views.activites, name='activites'),
    path('evenements/', views.evenements, name='evenements'),
    #path('admin_global/',views.ssadmin, name='admin_global'),
    path('addannonce/', views.addannonce, name='addannonce'),
    path('adannonces/', views.adannonces, name='adannonces'),
    path('adactivite/', views.adactivite, name='adactivite'),
    path('addactivite/', views.addactivite, name='addactivite'),
    path('administrateur/', views.ssadmin, name='administrateur'),
    path('table_inscrip_activi/', views.table1, name='table_inscrip_activi'),
    path('ins_laur/', views.tabl, name='ins_laur'),
    path('addevent/', views.addevent, name='addevent'),
    path('sincrire/', views.sinscrire1, name="sincrire"),
    path('My/', views.My, name='My'),
    path('challenge_pfe/', views.pf_ins, name='challenge_pfe'),
    path('addeve/', views.admine, name='addeve'),
    path('sous_admin/', views.ssadmin1, name='sous_admin'),
    path('admin_post/', views.admin_post, name='admin_post'),
    path('admin_commentaire/', views.admin_commentaire, name='admin_commentaire'),
    path('addact/', views.addact, name='addact'),
    path('gereractivites/', views.gereractivites, name='gereractivites'),
    path('activite/delete/<int:pk>', activiteDeleteView.as_view(), name='activite_delete'),
    path('update/<int:pk>', activiteUpdateView.as_view(), name='activite_update'),
    path('inscrire/delete/<int:pk>', inscrireDeleteView.as_view(), name='inscrire_delete'),
    path('annonce_list', annonceListView.as_view(), name='annonce_list'),
    path('annonce/delete/<int:pk>', annonceDeleteView.as_view(), name='annonce_delete'),
    path('annonce/update/<int:pk>', annonceUpdateView.as_view(), name='annonce_update'),
    path('candidat/', views.candidat, name='candidat'),
]
