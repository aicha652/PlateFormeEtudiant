from django.contrib import admin
from .models import Profile
#from .models import utilisateur1


admin.site.register(Profile)
from .models import laurea

# Register your models here.

admin.site.register(laurea)
#admin.site.register(utilisateur1)