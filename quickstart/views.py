

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, LocalitySerializer, StatusSerializer
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LocalityViewSet(viewsets.ModelViewSet):

		queryset = Locality.objects.all()
		serializer_class = LocalitySerializer    

class StatusViewSet(viewsets.ModelViewSet):

		queryset = Status.objects.all()
		serializer_class = StatusSerializer		

		