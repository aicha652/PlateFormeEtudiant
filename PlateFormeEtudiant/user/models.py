from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile.'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)




filiere_CHOICES1 = (
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




class laurea(models.Model):
    username = models.CharField(max_length=100, default='', unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    filiere = models.CharField(max_length=60, choices=filiere_CHOICES1)
    email = models.EmailField()
    annee_d_diplome = models.CharField(max_length=60, choices=Anne_CHOICES)
    telefone = models.IntegerField(max_length=13)
    cin = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    etablissement = models.CharField(default='Null', max_length=100)
    Societe = models.CharField(default='Null', max_length=100)
    poste = models.CharField(default='null', max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self. username





departement_CHOICES1 = (
    ('TM','TM'),
    ('GE','GE'),
    ('GI','GI'),
    ('GM','GM'),
    ('GP','GP'),
)





filiere_CHOICES2 = (
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


