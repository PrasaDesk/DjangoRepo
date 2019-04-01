from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from userData.models import userData

from .serializer import userSerializer, userSerializerLogin


class RegisterUserListView(ListAPIView):
    queryset = userData.objects.all()
    serializer_class = userSerializer


class RegisterUserDetailView(RetrieveAPIView):
    queryset = userData.objects.all()
    serializer_class = userSerializer


class RegisterUserCreateView(CreateAPIView):
    queryset = userData.objects.all()
    serializer_class = userSerializer


class RegisterUserUpdateView(UpdateAPIView):
    queryset = userData.objects.all()
    serializer_class = userSerializer


class RegisterUserDeleteView(DestroyAPIView):
    queryset = userData.objects.all()
    serializer_class = userSerializer


# from rest_framework import viewsets

# from userData.models import userData
# from .serializer import userSerializer


# class userViewSet(viewsets.ModelViewSet):
#     queryset = userData.objects.all()
#     serializer_class = userSerializer
#     print("viewset")
#     for obj in (queryset):
#         print(obj.firstname, obj.lastname)
