from django import forms
from django.contrib.auth.models import User
from .models import Profile,laurea


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=30,
                               help_text='Eviter les espaces.')
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='اlast_name')
    password1 = forms.CharField(
        label='password1', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='password2', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password est incorrecte')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('ily a un utilisateur avec ce nom.')
        return cd['username']




class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)




class LaureaForm(forms.ModelForm):
    username = forms.CharField(label=' username')
    nom = forms.CharField(label=' Nom')
    prenom  = forms.CharField(label=' Prénom')
    filiere = forms.CharField(label=' filiere')
    email = forms.EmailField(label='email')
    annee_d_diplome = forms.CharField(label=' annee_d_diplome')
    telefone = forms.IntegerField(label=' Telephone')
    cin = forms.CharField(label='cin')
    pays = forms.CharField(label=' pays')
    etablissement = forms.CharField(label='etablissement')
    Societe = forms.CharField(label='Societe')
    poste = forms.CharField(label=' poste')


    class Meta:
        model = laurea
        fields = ('nom', 'prenom', 'filiere', 'email', 'annee_d_diplome', 'telefone', 'cin', 'pays', 'etablissement', 'Societe', 'poste')
