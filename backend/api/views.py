from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.


class NoteListCreate(generics.ListCreateAPIView):
    """
    API view for creating new notes.

    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)  # pylint: disable=no-member

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)  # pylint: disable=no-member


class CreateUserView(generics.CreateAPIView):
    # """
    # API view for creating new users.

    # This view allows unauthenticated users to create new user accounts.
    # """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
