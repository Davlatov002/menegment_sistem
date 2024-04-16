from rest_framework import generics, status
from rest_framework.response import Response
from apps.group.models.group import Group
from api.group.serializers.group import GroupSerializer

class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDestroyAPIView(generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupCreateAPIView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupUpdateAPIView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)