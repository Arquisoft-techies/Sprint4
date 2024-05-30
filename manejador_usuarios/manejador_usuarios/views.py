from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore


class SimpleAPIView(APIView):
    def get(self, request):
      data = {'message': 'Hello from project1'}
      return Response(data, status=status.HTTP_200_OK)