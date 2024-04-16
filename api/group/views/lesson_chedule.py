from rest_framework import generics, status
from rest_framework.response import Response
from apps.group.models.lessons_chedule import LessonsChedule
from api.group.serializers.lesson_chedule import LessonsCheduleSerializsr

class LessonsCheduleListAPIView(generics.ListAPIView):
    queryset = LessonsChedule.objects.all()
    serializer_class = LessonsCheduleSerializsr


class LessonsCheduleDestroyAPIView(generics.DestroyAPIView):
    queryset = LessonsChedule.objects.all()
    serializer_class = LessonsCheduleSerializsr


class LessonsCheduleCreateAPIView(generics.CreateAPIView):
    queryset = LessonsChedule.objects.all()
    serializer_class = LessonsCheduleSerializsr

class LessonsCheduleUpdateAPIView(generics.UpdateAPIView):
    queryset = LessonsChedule.objects.all()
    serializer_class = LessonsCheduleSerializsr

class LessonsCheduleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LessonsChedule.objects.all()
    serializer_class = LessonsCheduleSerializsr

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)