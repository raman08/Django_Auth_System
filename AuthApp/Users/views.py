from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Seceret(APIView):

	permission_classes=[IsAuthenticated]

	def get(self, request):
		data = {
			'message': f'Welcome {request.user.username}'
		}
		return Response(data, status.HTTP_200_OK)