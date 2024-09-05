from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import Auther, ThreadPost
from .serializers import AutherSerializer, ThreadPostSerializer


class AutherView(APIView):

    def get(self, request):
        authers = Auther.objects.all()
        serializer = AutherSerializer(authers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AutherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutherUpdate(APIView):

    def get(self, request, i):
        try:
            auther = Auther.objects.get(id=i)
        except ObjectDoesNotExist as e:
            return Response(
                {"error": f"{e}", 
                "details": f"Auther with id {i} does not exist"}
            )
        serializer = AutherSerializer(auther)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, i):
        try:
            auther = Auther.objects.get(id=i)
        except ObjectDoesNotExist as e:
            return Response(
                {"error": f"{e}", 
                "details": f"Auther with id {i} does not exist"}
            )
        serializer = AutherSerializer(instance=auther, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, i):
        try:
            auther = Auther.objects.get(id=i)
        except ObjectDoesNotExist as e:
            return Response({"details": f"Auther with id {i} does not exist {e}"})
        auther.delete()
        return Response({"details": "Record deleted successfully"})
