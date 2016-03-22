from rest_framework import viewsets
from .models import Film
from filmlist.quickstart.serializers import FilmSerializer

class FilmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows films to be viewed or edited.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
