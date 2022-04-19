from rest_framework.serializers import ModelSerializer

from reservation.models import (
    Appartement,
    Service,
    Universite,
    ReservationDortoireDemande,
    Propriete,
)


class AppartementSerializer(ModelSerializer):
    class Meta:
        model = Appartement
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class UniversiteSerializer(ModelSerializer):
    class Meta:
        model = Universite
        fields = "__all__"


class DemandeReservationDortoireSerializer(ModelSerializer):
    class Meta:
        model = ReservationDortoireDemande
        fields = "__all__"


class ProprieteSerializer(ModelSerializer):
    class Meta:
        model = Propriete
        fields = "__all__"
