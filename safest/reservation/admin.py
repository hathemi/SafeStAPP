from django.contrib import admin

from .models import (
    TypePropriete,
    Propriete,
    Universite,
    Appartement,
    Chambre,
    Lit,
    TypeProprietaire,
    Proprietaire,
    Service,
    ReservationDortoireDemande,
    ReservationDortoireConfirmee,
    ReservationService,
)

# Register your models here.
admin.site.register(TypePropriete)
admin.site.register(Propriete)
admin.site.register(Universite)
admin.site.register(Appartement)
admin.site.register(Chambre)
admin.site.register(Lit)
admin.site.register(TypeProprietaire)
admin.site.register(Proprietaire)
admin.site.register(Service)
admin.site.register(ReservationDortoireDemande)
admin.site.register(ReservationDortoireConfirmee)
admin.site.register(ReservationService)
