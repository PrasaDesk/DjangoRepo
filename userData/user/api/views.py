# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

# from user.models import User_data

# from .serializer import UserSerializer, Use


# class UserRecordView(ListAPIView):
#     queryset = User_data.objects.all()
#     serializer_class = User_data


# class UserRecordRetriveView(RetrieveAPIView):
#     queryset = User_data.objects.all()
#     serializer_class = User_data


# class UserCreateView(CreateAPIView):
#     queryset = User_data.objects.all()
#     serializer_class = User_data

from rest_framework.generics import ListAPIView, CreateAPIView
from user.models import User_data
from .serializer import UserSerializer, UserDataSerializer


class UserRecordView(ListAPIView):
    queryset = User_data.objects.all()
    serializer_class = UserDataSerializer


class UserCreateView(CreateAPIView):
    queryset = User_data
    serializer_class = UserDataSerializer
