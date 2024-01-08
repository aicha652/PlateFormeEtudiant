from django.shortcuts import render, redirect
from .forms import UserCreationForm,  UserUpdateForm, ProfileUpdateForm, LaureaForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import club, etudiant1
from django.contrib.auth.models import User
from user.models import laurea


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    return render(request, 'user/profile.html', {
        'title': 'Mon compte',
        'posts': posts,
        'page': page,
        'post_list': post_list,
    })
   # try :
     #   l = etudiant.objects.get(cin=request.user)
   # except etudiant.DesNotExist:
    #    l = None
   # if  l :
      #  profile = etudiant.objects.get(cin=request.user)
       # return render(request,'user/profile.html',{'profile': profile})
   # else:
      #  profile2 = User.object.get(username=request.user)
       # profile1 =



@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
           # messages.success(
             #   request, 'Vos informations à été modifié.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'Modification du compte',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)




def MyObj(request):
    return HttpResponse(request,'bravoooooo')


def ins(request):
    if request.method == 'POST':
        form = LaureaForm(request.POST)
        if form.is_valid():
            form.save()
            # on execute seulement si tout est ok dans la form
            myObj = MyObj(request)  # Definition d'un objet modele
            myObj.username = form.cleaned_data['username']
            myObj.nom = form.cleaned_data['nom']
            myObj.prenom = form.cleaned_data['prenom']
            myObj.filiere = form.cleaned_data['filiere']
            myObj.email = form.cleaned_data['email']
            myObj.annee_d_diplome = form.cleaned_data['annee_d_diplome']
            myObj.telefone = form.cleaned_data['telefone']
            myObj.pays = form.cleaned_data['pays']
            myObj.etablissement = form.cleaned_data.get('etablissement ')
            myObj.Societe  = form.cleaned_data.get('Societe ')
            myObj.poste  = form.cleaned_data.get('poste ')

           #return HttpResponseRedirect('/bravo')  # Redirection vers une url
           # return redirect('forum:home')
            messages.warning(
                request, 'Votre formulaire est bien reçu .')
            return render(request, 'user/lauréats.html', {'form': form})
           # return HttpResponse('Votre formulaireb est bien reçu ,attendez acceptation administrateur')
    else:
        form = LaureaForm()
    return render(request, 'user/lauréats.html', {'form': form})


def loginadmin(request):
    if request.method == 'POST':
        user1='administrateur'
        pass1 = 'administrateur1234'
        user2 = 'ssadministrateur'
        pass2 = 'ssadministrateur1234'
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user1 == username and pass1 == password:

            return redirect('administrateur')
        if user2 == username and pass2 == password:
            return redirect('sous_admin')

        else:
            messages.warning(
                request, 'username ou password est incorrect.')

    return render(request, 'user/admin_login.html', {
        'title': 'Connexion',
    })

