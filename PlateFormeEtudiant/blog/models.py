from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.pk])

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='اNom')
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Commentaire')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'commenté {} sur {}.'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date',)





class club(models.Model):
    club = models.CharField(max_length=40)

    def __str__(self):
        return self.club





class evenement(models.Model):
    titre = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    img = models.ImageField(default='default.png')
    lieu = models.CharField(max_length=50)
    club = models.ForeignKey(club, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(default='defaultText')

    def _str_(self):
        return self.titre


class annonce(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titre


class theme_activ(models.Model):
    titre = models.CharField(max_length=20)
    img = models.ImageField(default='default.png')
    description = models.TextField(default='defaultText')

    def _str_(self):
        return self.titre


GENRE_CHOICES = (
    ('Dance', 'dance'),
    ('Music', 'music'),
    ('Theatre', 'theatre'),
    ('Dessin', 'dessin')
)



class Sous_adm(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    cne = models.CharField(max_length=10)
    theme = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def _str_(self):
        return self.nom


class activite(models.Model):
   sous_adm = models.ForeignKey(Sous_adm, on_delete=models.CASCADE)

   def _str_(self):
        return str(self.sous_adm)




filiere_CHOICES1 = (
    ('DUT-FC2', 'DUT-FC2'),
    ('DUT-GE2-EEI', 'DUT-GE2-EEI'),
    ('DUT-GE2-EII', 'DUT-GE2-EII'),
    ('DUT-GE2-RLI', 'DUT-GE2-RLI'),
    ('DUT-GEA2', 'DUT-GEA2'),
    ('DUT-GI2', 'DUT-GI2'),
    ('DUT-GM2', 'DUT-GM2'),
    ('DUT-TC2', 'DUT-TC2'),
    ('DUT-GP2', 'DUT-GP2')
)


class Con(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    cne = models.CharField(max_length=30)
    sujet = models.CharField(max_length=200)
    filiere = models.CharField(max_length=100, choices=filiere_CHOICES1)
    nom_ancadrant = models.CharField(max_length=30)
    rapport_pfe = models.FileField()
    projet_pfe = models.FileField(upload_to='Pfes/pdfs/')

    def __str__(self):
        return self.sujet





filiere_CHOICES3 = (
    ('DUT-FC2', 'DUT-FC2'),
    ('DUT-GE2-EEI', 'DUT-GE2-EEI'),
    ('DUT-GE2-EII', 'DUT-GE2-EII'),
    ('DUT-GE2-RLI', 'DUT-GE2-RLI'),
    ('DUT-GEA2', 'DUT-GEA2'),
    ('DUT-GI2', 'DUT-GI2'),
    ('DUT-GM2', 'DUT-GM2'),
    ('DUT-TC2', 'DUT-TC2'),
    ('DUT-GP2', 'DUT-GP2'),
    ('LP-GLAASRI', 'LP-GLAASRI'),
    ('LP-CFA', 'LP-CFA'),
    ('LP-GIL', 'LP-GIL'),
    ('LP-GLAASRI', 'LP-GLAASRI'),
    ('LP-LPMECA', 'LP-LPMECA'),
    ('LP-MECA', 'LP-MECA'),
    ('LP-MV', 'LP-MV'),
)

Anne_CHOICES = (

    ('1986', '1986'),
    ('1987', '1987'),
    ('1988', '1988'),
    ('1989', '1989'),
    ('1990', '1990'),
    ('1991', '1991'),
    ('1992', '1992'),
    ('1993', '1993'),
    ('1994', '1994'),
    ('1995', '1995'),
    ('1996', '1996'),
    ('1997', '1997'),
    ('1998', '1999'),
    ('1999', '1999'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),
    ('2029', '2029'),
    ('2030', '2030'),
    ('2031', '2031'),
    ('2032', '2032'),
    ('2033', '2033'),
    ('2034', '2034'),
    ('2035', '2035'),
    ('2036', '2036'),
    ('2037', '2037'),
    ('2038', '2038'),
    ('2039', '2039'),
)


class etudiant(models.Model):
   # username = models.OneToOneField(User, on_delete=models.CASCADE)
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    # Les Champs Optionnel De Le Remplir
    # img = models.ImageField(default='can1.jpg')
    # email = models.CharField(max_length=10, default='email')
    # annedenaissance = models.DateField(default=now)
    complete = models.IntegerField(default=0)

    def _str_(self):
        return self.nom

class etudiant1(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    # Les Champs Optionnel De Le Remplir
    # img = models.ImageField(default='can1.jpg')
    # email = models.CharField(max_length=10, default='email')
    # annedenaissance = models.DateField(default=now)
    #complete = models.IntegerField(default=0)

    def _str_(self):
        return self.user.username





class candidat(models.Model):
    nom = models.CharField(max_length=100)
    #prenom = models.CharField(max_length=30)
    #cne = models.CharField(max_length=30)
    sujet = models.CharField(max_length=200)
    departement = models.CharField(max_length=100, choices=filiere_CHOICES1)
    filiere = models.CharField(max_length=100, choices=filiere_CHOICES3)
    nom_encadrant = models.CharField(max_length=100)
    rapport_pfe = models.FileField()
   # projet_pfe = models.FileField(upload_to='Pfes/pdfs/')

    def _str_(self):
        return self.sujet




















