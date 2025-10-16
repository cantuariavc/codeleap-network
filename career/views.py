from django.shortcuts import render
from rest_framework import viewsets
from .models import Career
from .serializers import CareerSerializer


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all().order_by("-created_datetime")
    serializer_class = CareerSerializer
