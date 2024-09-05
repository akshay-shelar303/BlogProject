from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(["GET", "POST"])
def create_user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data["username"])
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": str(token)})
        return Response(serializer.errors)
    return Response(serializer.data)


# @api_view(["POST"])
# def create_user_token(request):
#     print(request.data)
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.data['username']
#         print(user)
#         token = Token.objects.create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#          })
#     return Response(serializer.errors)
