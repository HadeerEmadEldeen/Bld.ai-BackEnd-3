from django.core.exceptions import ValidationError
from django.urls import is_valid_path
from .models import *
from turtle import st
from django.shortcuts import render
# from django.views import View
from rest_framework.views import APIView
# from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
#from .pagination import *
# Create your views here.

class Product(APIView):
    def get(self, request):
        return Response(data = {'name': 'hadeer'})
    def post(self, request):
        serializer = FileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


