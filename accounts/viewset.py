from rest_framework import viewsets
from . import models, serializers


class EnterpriseViewset(viewsets.ModelViewSet):
    queryset = models.Enterprise.objects.all()
    serializer_class = serializers.EnterpriseSerializer