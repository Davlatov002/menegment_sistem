from django.urls import path
from api.group.views.group import (
    GroupCreateAPIView,
    GroupDestroyAPIView,
    GroupListAPIView,
    GroupRetrieveAPIView,
    GroupUpdateAPIView,
)
from api.group.views.sciences import (
    SciencesCreateAPIView,
    SciencesDestroyAPIView,
    SciencesListAPIView,
    SciencesRetrieveAPIView,
    SciencesUpdateAPIView,
)
from api.group.views.lesson_chedule import (
    LessonsCheduleCreateAPIView,
    LessonsCheduleUpdateAPIView,
    LessonsCheduleDestroyAPIView,
    LessonsCheduleRetrieveAPIView,
    LessonsCheduleListAPIView,
)

urlpatterns = [

    path('groups/', GroupListAPIView.as_view(), name='group_all'),
    path('group/<int:pk>/', GroupRetrieveAPIView.as_view(), name='group_retrieve'),
    path('group-create/', GroupCreateAPIView.as_view(), name='group_create'),
    path('group-update/<int:pk>/', GroupUpdateAPIView.as_view(), name='group_update'),
    path('group-delete/<int:pk>/', GroupDestroyAPIView.as_view(), name='group_delete'),

    path('sciences/', SciencesListAPIView.as_view(), name='science_all'),
    path('science/<int:pk>/', SciencesRetrieveAPIView.as_view(), name='scienche_retrieve'),
    path('science-create/', SciencesCreateAPIView.as_view(), name='science_creatr'),
    path('science-update/<int:pk>/', SciencesUpdateAPIView.as_view(), name='science_update'),
    path('science-delete/<int:pk>/', SciencesDestroyAPIView.as_view(), name='science_delete'),

    path('lessonchedules/', LessonsCheduleListAPIView.as_view(), name='lessonchedule_all'),
    path('lessonchedule/<int:pk>/', LessonsCheduleRetrieveAPIView.as_view(), name='lessonchedule_retrieve'),
    path('lessonchedule-create/', LessonsCheduleCreateAPIView.as_view(), name='lessonchedule_create'),
    path('lessonchedule-update/<int:pk>/', LessonsCheduleUpdateAPIView.as_view(), name='lessonchedule_update'),
    path('lessonchedule-delete/<int:pk>/', LessonsCheduleDestroyAPIView.as_view(), name='lessonchedule_delete'),


]