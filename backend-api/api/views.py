from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(APIView):
    def get(request, self):
        return Response('Hello, World!', status.HTTP_200_OK)