from rest_framework.generics import ListAPIView
from user.models import User, User_data
from .serializer import UserSerializer, UserDataSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import authenticate
from .tokenJWT import get_tokens_for_user
from django.contrib.auth.hashers import make_password


class UserRecordView(ListAPIView):
    """
    User list view
    It show's all user data
    (nested object)
    """

    queryset = User_data.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = (permissions.AllowAny,)


class UserRecord_View(ListAPIView):
    """Temp api
    It show the auth user data
    (single object)
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(['POST'])
@permission_classes((AllowAny,))
def register_user(request):
    """
    this api is store Only (username, password, fisrt_name, last_name, email)
    this is a temp api for testing (to frontend side)
    """

    pswd = request.data['password']
    request.data['password'] = make_password(pswd)

    serialized = UserSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save()

        obj = User.objects.exclude().get(username=request.data['username'])
        token = get_tokens_for_user(obj)

        return Response({'token': token}, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def register_user_alldata(request):
    """
    this api store all data with nested object in database
    """
    serialized = UserDataSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save()

        req_data = request.data['user']

        obj = User.objects.exclude().get(
            username=req_data['username'])

        token = get_tokens_for_user(obj)

        return Response({'token': token}, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    login api
    accept Username and Password
    authenticate the user
    return JWT token (access and refresh)
    """

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Please enter valid username or password'},
                        status=HTTP_400_BAD_REQUEST)

    obj = User.objects.exclude().get(username=username)
    print(obj.id)
    token = get_tokens_for_user(obj)

    return Response(token,
                    status=HTTP_200_OK)
