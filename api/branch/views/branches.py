from rest_framework import generics, status
from rest_framework.response import Response
from api.branch.serializers.branches import BranchesSerializer
from apps.branch.models.branches import Branch


class BranchesListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchesSerializer


class BranchesDestroyAPIView(generics.DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchesSerializer


class BranchesCreateAPIView(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchesSerializer

class BranchesUpdateAPIView(generics.UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchesSerializer

class BranchesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)