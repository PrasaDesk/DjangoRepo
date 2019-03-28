from rest_framework import viewsets

from userData.models import userData
from .serializer import userSerializer


class userViewSet(viewsets.ModelViewSet):
    queryset = userData.objects.all()
    serializer_class = userSerializer
    print("viewset")
    for obj in (queryset):
        print(obj.firstname, obj.lastname)
