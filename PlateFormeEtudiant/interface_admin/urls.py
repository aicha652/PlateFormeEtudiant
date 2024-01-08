from django.urls import path
from . import views
from .views import login_view, Logout_view, Deconnexion_view,  SousadminsCreateView, SousadminsListView, SousadminsDeleteView, SousadminsUpdateView, \
    activityDeleteView, activityUpdateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('indesc/', views.DashboardView.as_view(), name='indesc'),
    path('connexion/', login_view, name="connexion"),
    path("out", Logout_view, name="out"),
    path('change-pswd/', views.PswdChangeView.as_view(), name='change_pswd'),
    path('indes/', views.dashboardView.as_view(), name='indes'),
    path('connescion/', views.login_ssadmin, name='connescion'),
    path("deconnexion/", Deconnexion_view, name="deconnexion"),
    path('create/', SousadminsCreateView.as_view(), name='sousadmins_create'),
    path('Sousadmins_list', SousadminsListView.as_view(), name='sousadmins_list'),
    path('sousadmins/delete/<int:pk>', SousadminsDeleteView.as_view(), name='Sousadmins_delete'),
    path('sousadmins/update/<int:pk>', SousadminsUpdateView.as_view(), name='Sousadmins_update'),
    path('ssadminsactivites/', views.ssadminsactivites, name='ssadminsactivites'),
    path('activity/delete/<int:pk>', activityDeleteView.as_view(), name='activity_delete'),
    path('activity/update/<int:pk>', activityUpdateView.as_view(), name='activity_update'),
    path('change-pwd/', views.PwdChangeView.as_view(), name='change_pwd'),
]
