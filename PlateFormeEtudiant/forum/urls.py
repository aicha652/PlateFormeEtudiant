from . import views
from django.urls import path
from .views import CommentListView, CommentDeleteView, SolutionsListView, SolutionsDeleteView, QuestionListView, QuestionDeleteView,BlogPostListView ,BlogPostDeleteView, BlogCommentListView, BlogCommentDeleteView

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup' ),
     path('discussion/', views.post_question, name='post_question'),


    path('logout/', views.signout, name='signout'),
    path('question/<int:qid>/',views.question_page, name='question_page' ),
    path('upvote/<int:aid>/', views.upvote, name='upvote'),
    path('comment/<int:aid>/', views.comment, name='comment'),
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('post/<int:post_id>',views.post_page, name='post_page' ),
    path('blogcomment/<int:post_id>/', views.blogcomment, name='blogcomment'),
    path('comment_list/', CommentListView.as_view(), name='comment_list'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),
    path('solutions_list/', SolutionsListView.as_view(), name='solutions_list'),
    path('solutions/delete/<int:pk>', SolutionsDeleteView.as_view(), name='solutions_delete'),
    path('question_list/', QuestionListView.as_view(), name='question_list'),
    path('question/delete/<int:pk>',QuestionDeleteView.as_view(), name='question_delete'),
    path('blogpost_list/', BlogPostListView.as_view(), name='blogpost_list'),
    path('BlogPost/delete/<int:pk>',BlogPostDeleteView.as_view(), name='BlogPost_delete'),
    path('blogcomment_list/', BlogCommentListView.as_view(), name='blogcomment_list'),
    path('BlogComment/delete/<int:pk>',BlogCommentDeleteView.as_view(), name='BlogComment_delete'),
]