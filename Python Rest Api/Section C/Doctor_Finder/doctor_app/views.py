from django.shortcuts import render, redirect
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from django.db import transaction
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'specialization', 'city', 'fee']

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

def home(request):
    doctors = Doctor.objects.all().order_by('name')[:6]
    return render(request, 'home.html', {'doctors': doctors})