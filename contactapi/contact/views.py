from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ContactCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = "pk"

