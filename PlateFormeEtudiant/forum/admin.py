from django.contrib import admin
from forum.models import Question, Solutions, Comment, BlogPost, BlogComment

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question', 'author', 'datetime']
	search_fields = ['question', 'author']
	list_filter = ['datetime', 'author']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Solutions)
admin.site.register(Comment)
admin.site.register(BlogPost)
admin.site.register(BlogComment)
