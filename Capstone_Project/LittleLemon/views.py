from django.shortcuts import render
from rest_framework.views import APIView
import rest_framework.viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .models import *
from LittleLemon.serializers import bookingSerializer, menuSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer
        return Response(serializer.data)
    def post(self, request):
        serializer = bookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': "success", "data": serializer.data})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer
    permission_classes = [IsAuthenticated]


