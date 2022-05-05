from django.db import models
from django_extensions.db.fields import ShortUUIDField

# from django.contrib.auth.models import User
from django.conf import settings
import datetime

User = settings.AUTH_USER_MODEL


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        abstract = True


class TypePropriete(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Propriete(CommonInfo):
    name = models.CharField(max_length=255, unique=True)
    tel = models.BigIntegerField(unique=True)
    fax = models.BigIntegerField(default=0)
    email = models.EmailField()
    nbre_etage = models.IntegerField()
    descripion = models.CharField(max_length=500)
    adresse = models.CharField(max_length=500)
    matricule_fiscale = models.CharField(max_length=500)
    type = models.ForeignKey(TypePropriete, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


CITY_CHOICES = (
    ("tunis", "tunis"),
    ("ariana", "ariana"),
    ("benArous", "benArous"),
    ("manouba", "manouba"),
    ("nabeul", "nabeul"),
    ("zaghouan", "zaghouan"),
    ("bizerte", "bizerte"),
    ("béja", "béja"),
    ("jendouba", "jendouba"),
    ("siliana", "siliana"),
    ("sousse", "sousse"),
    ("monastir", "monastir"),
    ("mahdia", "mahdia"),
    ("sfax", "sfax"),
    ("kairouan", "kairouan"),
    ("kasserine", "kasserine"),
    ("sidiBouzid", "sidiBouzid"),
    ("gabès", "gabès"),
    ("mednine", "mednine"),
    ("tataouine", "tataouine"),
    ("gafsa", "gafsa"),
    ("tozeur", "tozeur"),
    ("kebili", "kebili"),
)

TYPE_CHOICES = (
    ("public", "public"),
    ("prive", "prive"),
)


class Universite(CommonInfo):
    name = models.CharField(max_length=255, unique=True)
    tel = models.BigIntegerField(unique=True)
    fax = models.BigIntegerField(default=0)
    email = models.EmailField()
    adresse = models.CharField(max_length=500)
    site_web = models.URLField(max_length=200, blank=True)
    ville = models.CharField(max_length=50, choices=CITY_CHOICES, default="tunis")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="public")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Appartement(CommonInfo):
    propriete = models.ForeignKey(
        Propriete,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    etage = models.IntegerField()
    nbre_lit = models.IntegerField()
    nbre_chambre = models.IntegerField()
    nbre_douche = models.IntegerField()
    nbre_places_reservees = models.IntegerField()
    espace_m2 = models.FloatField()
    meuble = models.BooleanField(default=False, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="reservation/photos", null=True, blank=True)

    def __str__(self):
        return str(self.prix) + ": DT"


class Chambre(CommonInfo):
    appartement = models.ForeignKey(
        Appartement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    etage = models.IntegerField()
    nbre_lit = models.IntegerField()
    description = models.CharField(max_length=500)
    nbre_places_reservees = models.IntegerField()
    espace_m2 = models.FloatField()
    meuble = models.BooleanField(default=False, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="reservation/photos", null=True, blank=True)

    def __str__(self):
        return str(self.prix) + ": DT"


class Lit(CommonInfo):
    chambre = models.ForeignKey(
        Chambre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    code_lit = models.CharField(max_length=250)
    est_reserve = models.BooleanField(default=False)

    def __str__(self):
        return self.code_lit


class TypeProprietaire(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Proprietaire(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    propriete = models.ForeignKey(
        Propriete,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    type = models.ForeignKey(
        TypeProprietaire,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=500)
    raison_social = models.CharField(max_length=500)
    email = models.EmailField(blank=True)
    tel_num = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.raison_social


class Service(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    propriete = models.ForeignKey(
        Propriete,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    titre = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titre


class ReservationDortoireDemande(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    appartement = models.ForeignKey(
        Appartement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    nom = models.CharField(max_length=500, blank=True)
    prenom = models.CharField(max_length=500, blank=True)
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(("Male", "Masculin"), ("Female", "Feminin")),
    )
    date_naissance = models.DateField(null=True, blank=True)
    ville = models.CharField(max_length=500, blank=True)
    universite = models.ForeignKey(
        Universite,
        related_name="universite_reservation",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    specialite = models.CharField(max_length=500, blank=True)
    message = models.TextField(blank=True)

    dete_debut = models.DateField(null=True, blank=True)
    period = models.CharField(max_length=500, blank=True)
    nbre_lit = models.IntegerField()
    status = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ("Waiting", "En attente"),
            ("Closed", "Clôturée"),
            ("Accepted", "Acceptée"),
        ),
    )

    def __str__(self):
        return self.period


class ReservationDortoireConfirmee(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    demande_reservation = models.ForeignKey(
        ReservationDortoireDemande,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.demande_reservation


class ReservationService(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    service = models.ForeignKey(
        Chambre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    period = models.DurationField(default=datetime.timedelta())
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.period
