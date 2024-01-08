from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .models import Sousadmins
from .forms import SousadminsForm
from  blog.forms import theme_activForm
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from blog.models import annonce
from blog.models import Sous_adm
from blog.models import theme_activ
from forum.models import Solutions
from forum.models import Comment
from forum.models import Question
from forum.models import BlogPost
from forum.models import BlogComment
from .models import Sousadmins
from django.urls import reverse_lazy

# Create your views here.






def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return redirect('indesc')
        else:
            messages.warning(
                request, 'username ou password est incorrect.')

    return render(request, 'interface_admin/connexion.html', {
        'title': 'Connexion'
    })


def Logout_view(request):
    logout(request)
    return render(request, 'interface_admin/out.html', {
        'title': 'Déconnexion'
    })


class DashboardView(TemplateView):
    template_name = "interface_admin/indesc.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['annonces'] = annonce.objects.count()
        context['Solutions'] = Solutions.objects.count()
        context['Comment'] = Comment.objects.count()
        context['Question'] = Question.objects.count()
        context['BlogPost'] = BlogPost.objects.count()
        context['BlogComment'] = BlogComment.objects.count()
        context['activites'] = theme_activ.objects.count()
        context['Sousadmins'] = Sousadmins.objects.count()
        return context


class PswdChangeView(PasswordChangeView):
    success_url = reverse_lazy('indesc')
    template_name = 'interface_admin/pswd_change_form.html'






def login_ssadmin(request):
    model = Sousadmins
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return redirect('indes')
        else:
            messages.warning(
                request, 'username ou password est incorrect.')

    return render(request, 'interface_admin/connescion.html', {
        'title': 'Connexion'
    })




class SousadminsCreateView(CreateView):
    model = Sousadmins
    form_class = SousadminsForm
    success_url = reverse_lazy('sousadmins_list')

    def get_context_data(self, **kwargs):
        context = super(SousadminsCreateView, self).get_context_data(**kwargs)
        context['panel_title'] = 'Ajouter un sous admin'
        return context


class SousadminsListView(ListView):
    model = Sousadmins
    field_list = [
        'username', 'nom', 'prenom', 'email'
    ]


class SousadminsDeleteView(DeleteView):
    model = Sousadmins
    template_name_suffix = '_delete'
    success_url = reverse_lazy('sousadmins_list')


class SousadminsUpdateView( UpdateView):
    model = Sousadmins
    template_name_suffix = '_form'
    form_class = SousadminsForm
    success_url = reverse_lazy('sousadmins_list')



class dashboardView(TemplateView):
    template_name = "interface_admin/indes.html"

    def get_context_data(self, **kwargs):
        context = super(dashboardView, self).get_context_data(**kwargs)
        context['activites'] = theme_activ.objects.count()
        context['inscrits'] = Sous_adm.objects.count()
        return context


def ssadminsactivites(request):
    object_list= theme_activ.objects.all()
    return render(request, 'interface_admin/ssadminsactivites.html', {'object_list':object_list})


class activityDeleteView( DeleteView):
    model = theme_activ
    template_name_suffix = '_deletee'
    success_url = reverse_lazy('ssadminsactivites')


class activityUpdateView( UpdateView):
    model = theme_activ
    template_name_suffix = '_forme'
    form_class = theme_activForm
    success_url = reverse_lazy('ssadminsactivites')


def  Deconnexion_view(request):
    logout(request)
    return render(request, 'interface_admin/deconnexion.html', {
        'title': 'Déconnexion'
    })



class PwdChangeView(PasswordChangeView):
    success_url = reverse_lazy('indesc')
    template_name = 'interface_admin/pwd_change_form.html'