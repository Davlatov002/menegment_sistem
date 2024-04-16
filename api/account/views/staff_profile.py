from rest_framework import status, generics
from rest_framework.response import Response
from apps.account.models.staff_profile import StaffProfile
from api.account.serializers.staff_profile import (
    StaffProfileSerializer,
)

class StaffProfileListAPIView(generics.ListAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer


class StaffProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer


class StaffProfileCreateAPIView(generics.CreateAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer

class StaffProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer

class StaffProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)