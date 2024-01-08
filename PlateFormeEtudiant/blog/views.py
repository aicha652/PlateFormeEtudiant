from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, evenement, annonce, theme_activ,activite,Sous_adm,etudiant, club,Con,candidat
from .forms import  Sous_admForm ,ConcForm,candidat
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
#from django.contrib.auth import login, authenticate, logout
from user.models import laurea
from user.forms import LaureaForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .forms import  AnnoncetForm,theme_activForm




def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title': 'Acceuil',
        'posts': posts,
        'page': page,
    }
    return render(request, 'blog/index.html', context)





def presentation(request):
    return render(request, 'blog/presentation.html')


def challenge(request):
    return render(request, 'blog/challenge.html')



def adannonces(request):
    return render(request, 'blog/adannonces.html')

def adactivite(request):
    return render(request, 'blog/adactivite.html')

def evenements(request):
    titre = 'Evenements'
    evenements = evenement.objects.all().order_by('date').reverse()
    return render(request, 'blog/evenements.html', {'titre': titre, 'evenements': evenements})




#def admin(request):
   # return render(request, 'blog/admin_global.html', {'title': ''})

def annonces(request):
    annonces = annonce.objects.all()
    return render(request, 'blog/annonces.html', {'annonces': annonces})





def activites(request):
    context = ''
    titre = 'activites'
    theme_activs = theme_activ.objects.all()
    if request.method == "POST":
        form =Sous_admForm(request.POST)
        if form.is_valid():

            for e1 in Sous_adm.objects.all():
                if e1.cne == form.cleaned_data['cne']:
                    if e1.theme == form.cleaned_data['theme']:
                        context = 'vous ete deja inscrit dans ce theme choisir un autre theme '
                        return render(request, 'blog/activites.html',
                                      {'form': form, 'titre': titre, 'theme_activs': theme_activs, 'context': context})

            for e in etudiant.objects.all():
                if e.cne == form.cleaned_data['cne']:
                    form.save()
                    sous_adm = Sous_adm()
                    sous_adm.nom = form.cleaned_data['nom']
                    sous_adm.prenom = form.cleaned_data['prenom']
                    sous_adm.cne = form.cleaned_data['cne']
                    sous_adm.theme = form.cleaned_data['theme']
                    request.session['sous_adm'] = form.cleaned_data
                    return render(request, 'blog/confirmer.html',
                                  {'sous_adm': sous_adm, 'titre': titre, 'theme_activs': theme_activs,
                                   'context': 'vous etes inscrit, si vous voulez vous pouvez s inscrire dans un voveau theme  '})
            return render(request, 'blog/activites.html',
                          {'form': form, 'titre': titre, 'theme_activs': theme_activs, 'context': 'ce cne n existe pas '})

    else:
        form = Sous_admForm()

        return render(request, 'blog/activites.html', {'form': form, 'titre': titre, 'theme_activs': theme_activs})

    return render(request, 'blog/activites.html', {'form': form, 'titre': titre, 'theme_activs': theme_activs})


def confirmation(request):
    data = request.session.get('sous_adm')
    sous_adm = Sous_adm()
    sous_adm.nom = data['nom']
    sous_adm.prenom = data['prenom']
    sous_adm.cne = data['cne']
    sous_adm.theme = data['theme']
    sous_adm.save()
    insc = activite(sous_adm=sous_adm)
    insc.save()
    return render(request, 'blog/Succes.html', {'sous_adm': request.session.get('sous_adm')})


#def adevenements(request):
    #return render(request, 'blog/adevenements.html')



def admine(request):
    if request.user.is_superuser or request.user.is_staff:
        clubs = club.objects.all()
        return render(request, 'blog/addeve.html', {'clubs': clubs})
    else:
        return redirect('evenements')




def addevent(request):
    titre = 'evenements'
    if request.method == 'POST':
        titre = request.POST.get('titre')
        lieu = request.POST.get('lieu')
        Description = request.POST.get('description')
        club_recup = request.POST.get('club')
        club_id = club.objects.get(club=club_recup).id
        print(club_recup)
        print(club_id)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        evenement.objects.create(titre=titre, lieu=lieu, description=Description, img=filename, club=club(club_id))
       # return redirect('evenements')
        return redirect('blog/evenements')

    else:
          return redirect('blog/evenements')



def admine(request):
    if request.user.is_superuser :
        clubs = club.objects.all()
        return render(request, 'blog/addeve.html', {'clubs': clubs})
    else:
        #return render(request, 'evenements')

         return redirect('evenements')


def addannonce(request):
    titre = 'Annonces'
    if request.method == 'POST':
        titre = request.POST.get('titre')
        Description = request.POST.get('description')
        annonce.objects.create(titre=titre, description=Description)
        return redirect('annonces')
    else:

     return redirect('annonces')



def addactivite(request):
    titre = 'activites'
    if request.method == 'POST':
        titre = request.POST.get('titre')
        Description = request.POST.get('description')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        theme_activ.objects.create(titre=titre,  img=filename, description=Description)
        return redirect('activites')
    else:
       return redirect('activites')


def ssadmin(request):
    return render(request, 'blog/administrateur.html')

def ssadmin1(request):
    return render(request, 'blog/sous_admin.html')


def table1(request):
   sous_adms = Sous_adm.objects.all()
   return render(request, 'blog/table_inscrip_activi.html', {'sous_adms': sous_adms})


def tabl(request):
   laureats = Lauréat.objects.all()
   return render(request, 'blog/ins_laur.html', {'laureats': laureats})


def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ssadmin')
        else:
            messages.warning(
                request, 'username ou password est incorrect.')

    return render(request, 'blog/loginadmin.html', {
        'title': 'Connexion',
    })

#def logout_user(request):
    #logout(request)
    #return render(request, 'blog/logoutadmin.html', {
        #'title': 'Déconnexion'
    #})



def My(request):
    return HttpResponse(request,'goood')


def sinscrire1(request):
    if request.method == 'POST':
        form = Sous_admForm(request.POST)
        if form.is_valid():
            form.save()
            # on execute seulement si tout est ok dans la form
            my = My(request)  # Definition d'un objet modele
            my.nom = form.cleaned_data['nom']
            my.prenom = form.cleaned_data['prenom']
            my.cne = form.cleaned_data['cne']
            my.theme = form.cleaned_data['theme']

           #return HttpResponseRedirect('/bravo')  # Redirection vers une url
           # return redirect('forum:home')
            messages.warning(
                request, 'Félicitaions!!! vous étes incrits aux activités')
            return render(request, 'blog/sincrire.html', {'form': form})
           # return HttpResponse('Félicitaions!!! vous étes incrits aux activités')
    else:
        form = Sous_admForm()
    return render(request, 'blog/sincrire.html', {'form': form})





   # return render(request, 'PE/concourpfe.html', {'form': form, 'contextpfe': 'test2'})

def m(request):
    return HttpResponse ('good')

def pf_ins(request):
    if request.method == 'POST':
        form = ConcForm(request.POST)
        if form.is_valid():
            form.save()
            # on execute seulement si tout est ok dans la form
            m = M(request)  # Definition d'un objet modele

            m.nom = form.cleaned_data['nom']
            m.prenom = form.cleaned_data['prenom']
            m.cne = form.cleaned_data['cne']
            m.sujet = form.cleaned_data['sujet']
            m.departement = form.cleaned_data['departement']
            m.filiere = form.cleaned_data['filiere']
            m.nom_ancadrant = form.cleaned_data['nom_ancadrant']
            m.rapport_pfe = form.cleaned_data['rapport_pfe']
            m.projet_pfe = form.cleaned_data['projet_pfe']

           #return HttpResponseRedirect('/bravo')  # Redirection vers une url
           # return redirect('forum:home')
            return HttpResponse('Félicitaions!!! vous étes incrits au challenge')
    else:
        form = ConcForm()
    return render(request, 'blog/challenge_pfe_estc.html', {'form': form})

def admin_post(request):
    base= Post.objects.all()
    return render(request, 'blog/admin_post.html', {'base':base})

def admin_commentaire(request):
    detail= Comment.objects.all()
    return render(request, 'blog/admin_commentaire.html', {'detail':detail})

def addact(request):
    titre = 'activites'
    if request.method == 'POST':
        titre = request.POST.get('titre')
        Description = request.POST.get('description')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        theme_activ.objects.create(titre=titre,  img=filename, description=Description)
        return redirect('activites')
    else:
       return redirect('activites')


class activiteUpdateView( UpdateView):
    model = theme_activ
    template_name_suffix = '_form'
    form_class =  theme_activForm
    success_url = reverse_lazy('gereractivites')


class activiteDeleteView( DeleteView):
    model = theme_activ
    template_name_suffix = '_delete'
    success_url = reverse_lazy('gereractivites')


class inscrireDeleteView( DeleteView):
    model = Sous_adm
    template_name_suffix = '_delete'
    success_url = reverse_lazy('table_inscrip_activi')

class annonceListView(ListView):
    model = annonce
    field_list = [
        'titre', 'description', 'date'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage annonces'
        context['panel_name']   =   'annonces'
        context['panel_title']  =   'View annonces Info'
        context['field_list']   =   self.field_list
        return context


def gereractivites(request):
    object_list= theme_activ.objects.all()
    return render(request, 'blog/gereractivites.html', {'object_list':object_list})

class annonceDeleteView( DeleteView):
    model = annonce
    template_name_suffix = '_delete'
    success_url = reverse_lazy('annonce_list')


class annonceUpdateView( UpdateView):
    model = annonce
    template_name_suffix = '_form'
    form_class = AnnoncetForm
    success_url = reverse_lazy('annonce_list')

    def m(request):
        return HttpResponse('good')


def candidat(request):
    if request.method == 'POST':
        form = candidat(request.POST)
        if form.is_valid():
            form.save()
            # on execute seulement si tout est ok dans la form
           # m = M(request)  # Definition d'un objet modele

            m.nom = form.cleaned_data['nom']
            #m.prenom = form.cleaned_data['prenom']
            #m.cne = form.cleaned_data['cne']
            m.sujet = form.cleaned_data['sujet']
            m.departement = form.cleaned_data['departement']
            m.filiere = form.cleaned_data['filiere']
            m.nom_encadrant = form.cleaned_data['nom_encadrant']
            m.rapport_pfe = form.cleaned_data['rapport_pfe']
         #   m.projet_pfe = form.cleaned_data['projet_pfe']

           #return HttpResponseRedirect('/bravo')  # Redirection vers une url
           # return redirect('forum:home')
            return HttpResponse('Félicitaions!!! vous étes incrits au challenge')

    return render(request, 'blog/candidat.html')