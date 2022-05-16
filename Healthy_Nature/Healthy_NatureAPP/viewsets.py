from rest_framework import viewsets
from . import models
from . import serializers

class PersonnelsViewsets(viewsets.ModelViewSet):
    queryset = models.Personnels.objects.all()
    serializer_class = serializers.PersonnelsSerializer