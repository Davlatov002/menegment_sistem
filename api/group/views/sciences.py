from rest_framework import generics, status
from rest_framework.response import Response
from apps.group.models.sciences import Scienc
from api.group.serializers.sciences import SciencesSerializer

class SciencesListAPIView(generics.ListAPIView):
    queryset = Scienc.objects.all()
    serializer_class = SciencesSerializer


class SciencesDestroyAPIView(generics.DestroyAPIView):
    queryset = Scienc.objects.all()
    serializer_class = SciencesSerializer


class SciencesCreateAPIView(generics.CreateAPIView):
    queryset = Scienc.objects.all()
    serializer_class = SciencesSerializer

class SciencesUpdateAPIView(generics.UpdateAPIView):
    queryset = Scienc.objects.all()
    serializer_class = SciencesSerializer

class SciencesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Scienc.objects.all()
    serializer_class = SciencesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)