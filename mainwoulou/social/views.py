from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
  

from rest_framework import generics

class HomeView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.'
        }
        return Response(response, status=200)
    

'''class HomeView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Welcome to the Social Authentication (Email) page using React Js and Django!'}
        return Response(content)

        '''