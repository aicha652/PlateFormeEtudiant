from django import forms
from .models import Comment, Post, annonce, Sous_adm,Con,theme_activ,candidat


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='titre du sujet')
    content = forms.CharField(label='Sujet de discussion', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content']



class AnnonceCreateForm(forms.ModelForm):
    title = forms.CharField(label='Titre de poste')
    content = forms.CharField(label='Annonce', widget=forms.Textarea)

    class Meta:
        model = annonce
        fields = ['title', 'content']


class Sous_admForm(forms.ModelForm):
   class Meta:
       model = Sous_adm
       fields = ['nom', 'prenom', 'cne', 'theme']




class ConcForm(forms.ModelForm):
            nom = forms.CharField(label='nom ')
            prenom = forms.CharField(label=' prenom ')
            cne = forms.CharField(label=' cne')
            sujet = forms.CharField(label='sujet')
          #  departement = forms.CharField(label='departement')
            filiere = forms.CharField(label='filiere')
            nom_ancadrant = forms.CharField(label='nom_ancadrant')
            rapport_pfe = forms.FileField(label=' rapport_pfe')
            projet_pfe = forms.FileField(label=' projet_pfe')

            class Meta:
                model = Con
                fields = ('nom', 'prenom', 'cne', 'sujet',  'filiere', 'nom_ancadrant', 'rapport_pfe',
                          'projet_pfe')


class theme_activForm(forms.ModelForm):
    class Meta:
        model = theme_activ
        fields = ('titre', 'img', 'description')

class AnnoncetForm(forms.ModelForm):
    class Meta:
        model = annonce
        fields ='__all__'
        widgets = {
            'title'  :   forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),

        }
class candidat(forms.ModelForm):
            nom = forms.CharField(label='nom ')
            # prenom = forms.CharField(label=' prenom ')
            # cne = forms.CharField(label=' cne')
            sujet = forms.CharField(label='sujet')
            departement = forms.CharField(label='departement')
            filiere = forms.CharField(label='filiere')
            nom_encadrant = forms.CharField(label='nom_encadrant')
            rapport_pfe = forms.FileField(label=' rapport_pfe')
          #  projet_pfe = forms.FileField(label=' projet_pfe')

            class Meta:
                model = candidat
                fields = ('nom', 'sujet', 'departement', 'filiere', 'nom_encadrant', 'rapport_pfe'
                          )