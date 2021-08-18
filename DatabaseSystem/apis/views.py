from django.shortcuts import render
from rest_framework import viewsets

from .serializers import RecordSerializer
from EnvergaDB.models import Records

# Create your views here.


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer
