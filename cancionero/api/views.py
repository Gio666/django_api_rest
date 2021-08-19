from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Cancion
from .serializers import CancionSerializer
from rest_framework import viewsets


# Create your views here.
class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nombre', 'artista', 'banda']
    ordering_fields = ['nombre', 'artista', 'banda']