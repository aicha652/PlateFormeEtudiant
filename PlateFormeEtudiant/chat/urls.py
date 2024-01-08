from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [

    path('index1/', views.index, name='index1'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    #path('messages/', views.message_view, name='messages'),

    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
 #   path('api/users/<int:pk>', views.user_list, name='user-detail'),
      path('api/users', views.user_list, name='user-list'),
   ]
