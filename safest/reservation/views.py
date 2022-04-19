from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from reservation.models import (
    Appartement,
    Service,
    Universite,
    ReservationDortoireDemande,
    Propriete,
)
from reservation.serializers import (
    AppartementSerializer,
    ServiceSerializer,
    UniversiteSerializer,
    DemandeReservationDortoireSerializer,
    ProprieteSerializer,
)

# retrieves a list of all rooms


class AppartementListCreateAPIView(ListCreateAPIView):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer


class AppartementRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer


# retrieves a list of all services


class ServiceListCreateAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# retrieves a list of all university


class UniversiteListCreateAPIView(ListCreateAPIView):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer


class UniversiteRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer


# retrieves a list of all reservations demand


class DemandeReservationDortoireListCreateAPIView(ListCreateAPIView):
    queryset = ReservationDortoireDemande.objects.all()
    serializer_class = DemandeReservationDortoireSerializer


class DemandeReservationDortoireRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = ReservationDortoireDemande.objects.all()
    serializer_class = DemandeReservationDortoireSerializer


# retrieves a list of all propriete


class ProprieteListCreateAPIView(ListCreateAPIView):
    queryset = Propriete.objects.all()
    serializer_class = ProprieteSerializer


class ProprieteRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Propriete.objects.all()
    serializer_class = ProprieteSerializer
